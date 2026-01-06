# AI/ML Automation Roadmap

To scale the Brand Protection workflow, I am developing models for:

1. **NLP (Lexical Analysis):** Using Random Forest or XGBoost to analyze URL entropy and detect "typosquatting" (e.g., `brnd-site.com`).
2. **Computer Vision (Logo Detection):** Implementing a YOLOv8 or CNN model to scan marketplace images for unauthorized brand logo usage.
3. **Automated Triage:** Using the risk scores to trigger the `legal_template` automatically via API, reducing time-to-takedown from hours to seconds.

## Phase 2: Feature Engineering for Brand Abuse

To move from a simple script to a real ML model, I am focusing on these features:

1. **Visual Similarity (Computer Vision):** Using Perceptual Hashing (pHash) to compare a suspicious site's favicon/logo against official corporate assets.
2. **Lexical Entropy:** Measuring how "random" a URL is. High entropy often correlates with DGA (Domain Generation Algorithms) used by malware.
3. **Sentiment & Intent (NLP):** Analyzing the text on the landing page to distinguish between a "Fan Site" (Low Risk) and a "Credential Harvesting Portal" (High Risk).
