import csv
import random

# Function to simulate a "Risk Score" for training data
def generate_mock_data(records=100):
    headers = ['url', 'contains_brand_name', 'domain_age_days', 'has_ssl', 'risk_label']
    
    with open('triage_training_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(records):
            brand = random.choice([True, False])
            age = random.randint(1, 3650)
            ssl = random.choice([0, 1]) # 0 for No SSL, 1 for SSL
            
            # Simple logic: New domains with brand names and no SSL are "High Risk" (1)
            if brand and age < 30 and ssl == 0:
                label = 1 # High Risk
            else:
                label = 0 # Low Risk
                
            writer.writerow([f"suspicious-site-{random.randint(100,999)}.com", brand, age, ssl, label])

generate_mock_data()
print("Success: triage_training_data.csv generated for ML model training.")
