# RAG System Evaluation. 

## Retrieval Quality Tests (10 tests)
| Test ID | Question | Expected Documents | Pass Criteria |
|---------|----------|-------------------|---------------|
| R01 | How do I create a seller account on Shoplite? | Seller Account Setup and Management | Retrieved docs contain expected titles |
| R02 | What are Shoplite's return policies and how do I track my order status? | Return and Refund Policies, Order Tracking and Delivery | Retrieved docs are relevant to question |
| R03 | What payment methods are supported on Shoplite? | Checkout and Payment Methods | Retrieved docs contain expected titles |
| R04 | How can sellers manage their inventory? | Inventory Management for Sellers | Retrieved docs contain expected titles |
| R05 | How do I apply promotional codes during checkout? | Promotional Codes and Discounts | Retrieved docs contain expected titles |
| R06 | What security measures does Shoplite use to protect user data? | Security and Privacy Policies, Account Security Best Practices | Retrieved docs contain expected titles |
| R07 | How do I leave a product review on Shoplite? | Product Reviews and Ratings | Retrieved docs contain expected titles |
| R08 | What is the Shoplite buyer protection program? | Buyer Protection Program | Retrieved docs contain expected titles |
| R09 | How do I contact Shoplite customer support? | Customer Support Procedures | Retrieved docs contain expected titles |
| R10 | What features does the Shoplite mobile app offer? | Mobile App Features | Retrieved docs contain expected titles |

## Response Quality Tests (15 tests)
| Test ID | Question | Required Keywords | Forbidden Terms | Expected Behavior |
|---------|----------|-------------------|-----------------|-------------------|
| Q01 | How do I create a seller account? | ["seller registration", "business verification"] | ["instant approval"] | Direct answer with citation |
| Q02 | What are Shoplite's return policies? | ["30-day return window"] | ["lifetime returns"] | Direct answer with citation |
| Q03 | What payment methods are supported? | ["credit/debit cards", "PayPal"] | ["cash on delivery"] | Direct answer with citation |
| Q04 | How can sellers manage inventory? | ["inventory levels", "bulk upload"] | ["manual tracking only"] | Direct answer with citation |
| Q05 | How do I apply promo codes? | ["promo code", "checkout"] | ["unlimited use"] | Direct answer with citation |
| Q06 | What security measures are used? | ["encryption", "security audits"] | ["data sold"] | Direct answer with citation |
| Q07 | How do I leave a review? | ["leave reviews", "moderated"] | ["anonymous reviews"] | Direct answer with citation |
| Q08 | What is buyer protection? | ["buyer protection", "claims"] | ["no protection"] | Direct answer with citation |
| Q09 | How do I contact support? | ["chat", "AI-powered assistants"] | ["no support"] | Direct answer with citation |
| Q10 | What features does the mobile app offer? | ["push notifications", "barcode scanning"] | ["no app"] | Direct answer with citation |
| Q11 | How do developers access APIs? | ["RESTful APIs", "API keys"] | ["open access"] | Direct answer with citation |
| Q12 | How are seller fees calculated? | ["commission", "fee breakdown"] | ["no fees"] | Direct answer with citation |
| Q13 | What analytics are available to sellers? | ["sales trends", "analytics dashboard"] | ["manual reports only"] | Direct answer with citation |
| Q14 | What shipping options do sellers have? | ["integrated shipping partners"] | ["pickup only"] | Direct answer with citation |
| Q15 | How do users recover their account? | ["account recovery", "email"] | ["phone only"] | Direct answer with citation |

## Edge Case Tests (5 tests)
| Test ID | Scenario | Expected Response Type |
|---------|----------|----------------------|
| E01 | Question not in knowledge base | Refusal with explanation |
| E02 | Ambiguous question | Clarification request |
| E03 | Multi-document required | Synthesis from multiple docs |
| E04 | Forbidden term detected | Exclude forbidden info |
| E05 | No context retrieved | Refusal with explanation |

