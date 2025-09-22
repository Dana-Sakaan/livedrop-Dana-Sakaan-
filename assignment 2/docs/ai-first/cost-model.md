# AI Cost Model

## Model and Pricing Assumptions
We'll use GPT-4o-mini priced at $0.15 per 1,000 prompt tokens and $0.60 per 1,000 completion tokens. For the search typeahead, we estimate average inputs of 50 tokens and outputs of 100 tokens. The support assistant typically uses 200 input tokens and 300 output tokens per interaction.

## Traffic and Caching Assumptions
The search typeahead handles 50,000 daily requests with a 70% cache hit rate, meaning only 30% of queries require AI processing. The support assistant receives 1,000 daily requests with a 30% cache hit rate.

## Cost Calculations

### Smart Search Typeahead
Each AI-assisted search costs approximately $0.0675 calculated as (50 tokens × $0.00015) + (100 tokens × $0.00060). With 50,000 daily requests and 70% caching, we process 15,000 AI queries daily, resulting in $1,012.50 per day.

### Support Assistant
Each support interaction costs about $0.21 computed as (200 tokens × $0.00015) + (300 tokens × $0.00060). Handling 1,000 daily requests with 30% caching means 700 AI interactions daily, totaling $147 per day.

## Summary Results
- Search typeahead: $0.0675 per action, $1,012.50 daily cost
- Support assistant: $0.21 per action, $147 daily cost

## Cost Optimization Strategies
If costs exceed budget, we can reduce search output tokens to 50 (33% savings) or use lighter models for non-critical queries. For support, we can implement more aggressive caching or use smaller context windows for simple questions. Both systems can benefit from a tiered model approach where simpler queries use more cost-effective models.