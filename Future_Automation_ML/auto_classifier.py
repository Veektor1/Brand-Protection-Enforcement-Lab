# Automated Brand Protection Triage Script (Prototype)
# Purpose: Demonstrate how NLP-based lexical analysis can automate risk scoring.

def calculate_risk_score(url, has_brand_name, days_active):
    score = 0
    
    # 1. Lexical Analysis (NLP logic: check for 'look-alike' strings)
    suspicious_keywords = ['login', 'secure', 'verify', 'update', 'account']
    for word in suspicious_keywords:
        if word in url:
            score += 20
            
    # 2. Brand Impersonation Check
    if has_brand_name:
        score += 50 # High weight: Brand names in non-official domains are high risk
        
    # 3. Domain Age (New domains are riskier)
    if days_active < 30:
        score += 25
        
    return score

# Example Targets
targets = [
    {"url": "brand-login-secure.net", "brand": True, "age": 2},
    {"url": "officialbrandsite.com", "brand": True, "age": 3650}
]

print("--- Automated Risk Triage Report ---")
for site in targets:
    risk = calculate_risk_score(site['url'], site['brand'], site['age'])
    status = "HIGH RISK (Automate Takedown)" if risk > 70 else "Low Risk (Monitor)"
    print(f"URL: {site['url']} | Score: {risk} | Action: {status}")
