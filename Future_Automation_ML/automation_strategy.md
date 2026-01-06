# AI/ML Automation Roadmap

To scale the Brand Protection workflow, I am developing models for:

1. **NLP (Lexical Analysis):** Using Random Forest or XGBoost to analyze URL entropy and detect "typosquatting" (e.g., `brnd-site.com`).
2. **Computer Vision (Logo Detection):** Implementing a YOLOv8 or CNN model to scan marketplace images for unauthorized brand logo usage.
3. **Automated Triage:** Using the risk scores to trigger the `legal_template` automatically via API, reducing time-to-takedown from hours to seconds.
