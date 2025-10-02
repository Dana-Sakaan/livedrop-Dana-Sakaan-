# Shoplite Ground Truth Q&A

### Q01: How do I create a seller account on Shoplite?
**Expected retrieval context:** Document 8: Seller Account Setup and Management
**Authoritative answer:** To create a seller account, visit the Shoplite seller registration page, provide business information including tax ID and business registration, and complete the verification process which takes 2-3 business days.
**Required keywords in LLM response:** ["seller registration", "business verification", "2-3 business days", "tax ID"]
**Forbidden content:** ["instant approval", "no verification required", "personal accounts only"]

### Q02: What are Shoplite's return policies and how do I track my order status?
**Expected retrieval context:** Document 6: Return and Refund Policies + Document 5: Order Tracking and Delivery
**Authoritative answer:** Shoplite offers a 30-day return window for most items from delivery date. Items must be unused in original packaging. For order tracking, you can monitor progress through your Shoplite account or via email updates including order confirmation, processing, shipping, and delivery completion.
**Required keywords in LLM response:** ["30-day return window", "original packaging", "order tracking", "delivery confirmation"]
**Forbidden content:** ["60-day returns", "no returns accepted", "phone calls for tracking"]

### Q03: What payment methods does Shoplite accept and how secure are they?
**Expected retrieval context:** Document 4: Payment Methods and Security
**Authoritative answer:** Shoplite accepts Visa, MasterCard, American Express, Discover, PayPal, Apple Pay, Google Pay, and Shoplite Wallet. All payments are processed with PCI DSS Level 1 compliance, end-to-end encryption, and tokenization for security.
**Required keywords in LLM response:** ["Visa", "MasterCard", "PayPal", "PCI DSS", "encryption", "tokenization"]
**Forbidden content:** ["cash payments", "bitcoin", "unsecured payments"]

### Q04: How does the shopping cart work and what features does it have?
**Expected retrieval context:** Document 2: Shoplite Shopping Cart Features
**Authoritative answer:** The Shoplite shopping cart allows adding items from multiple sellers, applying promotional codes, and saving items for later. It preserves contents across sessions, shows real-time price updates, and includes a 10-minute reservation system for limited stock items.
**Required keywords in LLM response:** ["multiple sellers", "promotional codes", "save for later", "real-time updates", "reservation system"]
**Forbidden content:** ["single seller only", "no saving feature", "immediate expiration"]

### Q05: What are the steps in the Shoplite checkout process?
**Expected retrieval context:** Document 3: Shoplite Checkout Process
**Authoritative answer:** The checkout process has four steps: shipping information selection, payment method entry, order review, and confirmation. Users must be logged in, though guest checkout is available for one-time purchases.
**Required keywords in LLM response:** ["shipping information", "payment method", "order review", "confirmation", "guest checkout"]
**Forbidden content:** ["one-step checkout", "no login required", "skip review"]

### Q06: How can sellers manage their inventory on Shoplite?
**Expected retrieval context:** Document 9: Inventory Management for Sellers
**Authoritative answer:** Sellers can manage inventory through the seller dashboard with features for single items, product variants, bulk editing, low stock alerts, and automated replenishment. Integration with accounting software and fulfillment options including SFS are available.
**Required keywords in LLM response:** ["seller dashboard", "bulk editing", "low stock alerts", "automated replenishment", "fulfillment options"]
**Forbidden content:** ["manual updates only", "no alerts", "single fulfillment method"]

### Q07: What commission fees does Shoplite charge sellers?
**Expected retrieval context:** Document 10: Commission and Fee Structure
**Authoritative answer:** Commission rates vary by category: Electronics 8%, Clothing 15%, Home & Garden 12%, Books & Media 10%, Other 12%. Additional payment processing fees apply, and monthly store subscriptions range from $29.99 to $79.99.
**Required keywords in LLM response:** ["commission", "8% electronics", "15% clothing", "payment processing fees", "monthly subscription"]
**Forbidden content:** ["flat 10% commission", "no additional fees", "free subscription"]

### Q08: How does customer support work and what are the response times?
**Expected retrieval context:** Document 11: Customer Support Procedures
**Authoritative answer:** Support is available 24/7 via live chat (under 2 minutes), email (under 4 hours), and phone (under 5 minutes). Multilingual support in 12 languages and escalation procedures for complex issues are provided.
**Required keywords in LLM response:** ["24/7 support", "live chat", "2 minutes", "email", "4 hours", "multilingual"]
**Forbidden content:** ["business hours only", "24-hour response", "single language"]

### Q09: What special features does the Shoplite mobile app offer?
**Expected retrieval context:** Document 12: Mobile App Features
**Authoritative answer:** The mobile app includes push notifications, barcode scanning, augmented reality previews, voice search, biometric login, offline browsing, app-exclusive deals, and one-touch checkout.
**Required keywords in LLM response:** ["push notifications", "barcode scanning", "augmented reality", "biometric login", "app-exclusive deals"]
**Forbidden content:** ["website features only", "no mobile benefits", "same as website"]

### Q10: How can developers integrate with Shoplite using the API?
**Expected retrieval context:** Document 13: API Documentation for Developers
**Authoritative answer:** The RESTful API uses OAuth 2.0 authentication with rate limits of 1000 requests/hour. Available endpoints include product search, order management, and payment processing with SDKs for Python, JavaScript, Java, and PHP.
**Required keywords in LLM response:** ["RESTful API", "OAuth 2.0", "rate limits", "endpoints", "SDKs"]
**Forbidden content:** ["SOAP API", "unlimited requests", "no authentication"]

### Q11: What security measures protect user data on Shoplite?
**Expected retrieval context:** Document 14: Security and Privacy Policies
**Authoritative answer:** Security includes 256-bit SSL encryption, regular security audits, intrusion detection, encrypted data storage, and compliance with GDPR and CCPA. Users control data through privacy settings.
**Required keywords in LLM response:** ["256-bit SSL encryption", "security audits", "intrusion detection", "GDPR", "CCPA", "privacy settings"]
**Forbidden content:** ["basic security", "no encryption", "data selling"]

### Q12: What types of promotional codes are available and how do they work?
**Expected retrieval context:** Document 15: Promotional Codes and Discounts
**Authoritative answer:** Promotional codes include percentage discounts (10-50% off), fixed amount discounts, free shipping, and BOGO deals. Automatic discounts include first-order welcome discounts and birthday discounts, with maximum two codes stackable per order.
**Required keywords in LLM response:** ["percentage discounts", "fixed amount", "free shipping", "welcome discounts", "stacking rules"]
**Forbidden content:** ["unlimited stacking", "no expiration", "always 50% off"]

### Q13: How do user registration and account management work?
**Expected retrieval context:** Document 1: Shoplite User Registration Process
**Authoritative answer:** Registration requires email, password, and basic profile with email verification within 24 hours. Password requirements include 8+ characters with uppercase, number, and special character. Accounts can be deactivated and restored within 30 days.
**Required keywords in LLM response:** ["email verification", "password requirements", "account deactivation", "30-day restoration"]
**Forbidden content:** ["no verification", "simple passwords", "immediate deletion"]

### Q14: Can I leave product reviews and how does the rating system work?
**Expected retrieval context:** Document 7: Product Reviews and Ratings
**Authoritative answer:** Customers can leave reviews within 90 days of purchase with 1-5 star ratings. Verified purchase badges distinguish real buyers, and sellers can respond professionally. Separate scores for quality, value, and description accuracy are included.
**Required keywords in LLM response:** ["90 days", "1-5 stars", "verified purchase", "seller responses", "separate scores"]
**Forbidden content:** ["unlimited time", "10-star system", "seller removal"]

### Q15: What shipping options are available and how long do they take?
**Expected retrieval context:** Document 3: Shoplite Checkout Process + Document 5: Order Tracking and Delivery
**Authoritative answer:** Shipping options include standard (5-7 business days), expedited (2-3 business days), and express (1-2 business days). Digital products deliver immediately, and costs vary by seller, weight, and destination.
**Required keywords in LLM response:** ["standard shipping", "expedited", "express", "digital immediate", "costs vary"]
**Forbidden content:** ["same-day shipping", "flat rates", "physical only"]

### Q16: What happens if my package is lost or delayed?
**Expected retrieval context:** Document 5: Order Tracking and Delivery
**Authoritative answer:** For delays, contact support after 48 hours past estimated delivery. Lost package claims can be filed after 7 business days with resolution in 3-5 business days. Two delivery attempts are made before return to seller.
**Required keywords in LLM response:** ["48 hours delay", "7 business days lost", "3-5 day resolution", "two delivery attempts"]
**Forbidden content:** ["immediate claims", "no investigation", "one attempt"]

### Q17: How do I apply for a refund and how long does it take?
**Expected retrieval context:** Document 6: Return and Refund Policies
**Authoritative answer:** Obtain return authorization through the returns center, then use prepaid shipping labels for items under 50 pounds. Refunds process within 3-5 business days of receiving returned items to original payment method.
**Required keywords in LLM response:** ["return authorization", "prepaid shipping", "3-5 business days", "original payment method"]
**Forbidden content:** ["automatic refunds", "immediate processing", "store credit only"]

### Q18: What are the requirements to maintain a seller account in good standing?
**Expected retrieval context:** Document 8: Seller Account Setup and Management
**Authoritative answer:** Sellers must maintain at least 4.0 overall rating and 95% on-time shipping. Performance metrics include order defect rate and customer satisfaction scores. Premium status requires meeting these standards consistently.
**Required keywords in LLM response:** ["4.0 rating", "95% on-time shipping", "order defect rate", "customer satisfaction", "premium status"]
**Forbidden content:** ["no requirements", "automatic good standing", "minimum sales"]

### Q19: What happens if I enter wrong payment information during checkout?
**Expected retrieval context:** Document 4: Payment Methods and Security
**Authoritative answer:** The system validates payment information in real-time and will decline invalid entries. For repeated failures, temporary account holds may be placed due to fraud detection monitoring. Users should verify information and contact support if issues persist.
**Required keywords in LLM response:** ["real-time validation", "declined payments", "fraud detection", "account holds", "contact support"]
**Forbidden content:** ["manual review", "no validation", "permanent bans"]

### Q20: How do I contact customer support for international orders?
**Expected retrieval context:** Document 11: Customer Support Procedures + Document 5: Order Tracking and Delivery
**Authoritative answer:** International orders can use the same 24/7 support channels with multilingual support in 12 languages. Specific international support includes customs clearance assistance and import fee clarification beyond standard order tracking.
**Required keywords in LLM response:** ["24/7 support", "multilingual", "customs clearance", "import fees", "international tracking"]
**Forbidden content:** ["domestic only", "single language", "no customs help"]