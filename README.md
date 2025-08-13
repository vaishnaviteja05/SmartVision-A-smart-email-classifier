# SmartVision-A-smart-email-classifier
Smart Vision Email Threat Classifier is an AI-powered tool that detects and categorizes emails as spam, phishing, promotional, or safe using NLP and ML, enhancing email security and user awareness.

## 📜 About
Spam Vision is a smart email classification system designed to filter and categorize emails into four main types:
- **Spam** — Unwanted or junk emails  
- **Phishing** — Malicious attempts to steal sensitive information  
- **Promotional** — Marketing and advertising content  
- **Safe** — Legitimate, personal, or business emails  

The system supports multiple email providers (**Gmail, Yahoo, Outlook, Zoho**), integrates with email APIs, and uses **ML algorithms + NLP techniques** to ensure real-time detection and classification.

## 🚀 Features
- Detects **Spam**, **Phishing**, **Promotional**, and **Safe** emails  
- Works with **multiple email services** (Gmail, Yahoo, Outlook, Zoho)  
- Supports **real-time monitoring** of incoming emails  
- Integrates with **custom API keys** for security  
- Lightweight and fast deployment  
- Scalable for enterprise use  

## 🛠️ Technologies
- **Language:** Python  
- **Libraries & Frameworks:** scikit-learn, Pandas, NumPy, NLTK, Flask  
- **Email APIs:** Gmail API, IMAP, SMTP  
- **Other Tools:** JSON, Regex, Matplotlib (for visualization)  

## Files Included:
- spamvision_model.pkl : The trained ML model 
- spamvision_monitor.py : The actual code script
- requirements.txt : The python libraries used
- vectorizer.pkl : It converts the email text into numerical form
- train_model.py : Trains the ML model using labeled datasets, processes text with NLP, and saves the model for Spam Vision.
- train_spamvision.py : Fetches emails, updates the dataset, retrains the Spam Vision model, and saves the updated version
- ZohoMailbox.png : Screenshot of Zoho mail inbox
- NotificationDetected.jpg : A desktop notification has been detected after running the application
- ProjectDemo.mp4 : A demo video on how this application works 

  ```plaintext
spam-vision/
├── spamvisionmonitor.py
├── train_model.py
├── train_spamvision.py
└── requirements.txt

## 📂 Installation
```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/spam-vision.git
cd spam-vision

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Set up your API credentials
# Create a config.json file with your email API keys and passwords (generated app passwords recommended)

# 4️⃣ Run the application
python spamvisionmonitor.py
