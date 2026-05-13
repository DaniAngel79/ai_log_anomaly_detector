# AI Log Anomaly Detector (PoC)

### Technical Description
Proof of Concept (PoC) for automated anomaly detection in system logs using **Transformer-based** language models. This project implements a hybrid analysis engine that combines the power of AI with a **signature-based fallback** system to ensure analysis availability and accuracy even in restricted environments.

### Key Features
*   **Intelligent Detection**: Uses `Sequence Classification` models to identify suspicious patterns that bypass traditional filters.
*   **Hybrid Engine**: In case of AI model loading failure, the system automatically switches to high-criticity keyword (signature) scanning.
*   **Modular Architecture**: Designed to be integrated into web auditing workflows and infrastructure monitoring.
### Usage
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the detector:
   `python anomaly_detector.py --file your_system.log`
