# AI Capability Map

## Selected Capabilities

### Smart Search Typeahead
- **User Intent**: Find products faster using natural language instead of exact keywords
- **Inputs Available**: Product catalog (10k SKUs), historical search logs
- **Risk Level**: Low (2/5) - falls back to existing keyword search
- **Latency Target**: 300ms p95
- **Cost Estimate**: $0.002 per query
- **Fallback**: Current keyword matching system

### Support Assistant  
- **User Intent**: Get instant answers to common policy questions without waiting for human support
- **Inputs Available**: FAQ markdown, return policies, shipping information
- **Risk Level**: Medium (3/5) - escalates to human agents when needed
- **Latency Target**: 1200ms p95
- **Cost Estimate**: $0.015 per interaction
- **Fallback**: Direct transfer to human support queue

## Rejected Capabilities

### Product Description Enhancer
- **User Intent**: Automatically generate SEO-optimized product descriptions
- **Inputs Available**: Basic product attributes and specifications
- **Risk Level**: High (4/5) - requires manual review to maintain quality
- **Reason for Rejection**: Lower immediate business impact compared to customer-facing features

### Cart Abandonment Predictor
- **User Intent**: Identify at-risk purchases before customers leave
- **Inputs Available**: Session behavior, cart contents, user history
- **Risk Level**: Very High (5/5) - complex integration and data requirements
- **Reason for Rejection**: High implementation risk for first AI sprint

## Why These Two Selections

We chose the smart search typeahead and support assistant because they directly address key business metrics with minimal integration risk. The search enhancement targets conversion rate improvement by reducing friction in product discovery, while the support assistant aims to decrease ticket volume by handling repetitive inquiries. Both capabilities leverage existing data sources that are readily available and have clear fallback mechanisms to ensure no degradation in customer experience. The latency targets are achievable with current infrastructure, and the cost estimates fall within reasonable bounds for the expected business value.