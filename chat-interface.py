#!/usr/bin/env python3
"""
Shoplite RAG Chat Interface
Connects to the deployed LLM API and provides a command-line chat interface
"""

import requests
import json
import sys
import time
from typing import Dict, List, Optional

class ShopliteChatInterface:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.conversation_history = []
        
    def test_connection(self) -> bool:
        """Test connection to the API"""
        try:
            response = requests.get(f"{self.base_url}/health", timeout=10)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False
    
    def send_message(self, message: str, use_rag: bool = True) -> Dict:
        """Send a message to the API and return the response"""
        endpoint = "/chat" if use_rag else "/ping"
        
        payload = {
            "message": message,
            "conversation_history": self.conversation_history
        }
        
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {
                    "error": f"API returned status code {response.status_code}",
                    "response": "Sorry, I'm having trouble connecting to the service."
                }
                
        except requests.exceptions.Timeout:
            return {
                "error": "Request timeout",
                "response": "Sorry, the request timed out. Please try again."
            }
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "response": "Sorry, I couldn't connect to the service. Please check the URL and try again."
            }
    
    def format_response(self, response_data: Dict) -> str:
        """Format the API response for display"""
        if "error" in response_data:
            return f"❌ Error: {response_data['error']}\n"
        
        formatted = []
        
        if "response" in response_data:
            formatted.append(f"🤖 {response_data['response']}")
        
        if "sources" in response_data and response_data["sources"]:
            sources = ", ".join(response_data["sources"])
            formatted.append(f"📚 Sources: {sources}")
        
        if "confidence" in response_data:
            confidence = response_data["confidence"]
            confidence_icon = "🟢" if confidence == "high" else "🟡" if confidence == "medium" else "🔴"
            formatted.append(f"{confidence_icon} Confidence: {confidence}")
        
        if "processing_time" in response_data:
            time_ms = response_data["processing_time"] * 1000
            formatted.append(f"⏱️  Response time: {time_ms:.0f}ms")
        
        return "\n".join(formatted) + "\n"
    
    def chat_loop(self):
        """Main chat loop"""
        print("=" * 60)
        print("🛍️  Shoplite Customer Service Assistant")
        print("=" * 60)
        print("Type your questions about Shoplite features, policies, and support")
        print("Commands: 'quit' to exit, 'rag off' to disable RAG")