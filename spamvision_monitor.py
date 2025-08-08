import imaplib
import email
from email.header import decode_header
import joblib
from plyer import notification
import time

# Load your ML model
spamvision_model = joblib.load("spamvision_model.pkl")

# Email credentials
username = "vaishnaviteja8052@zohomail.in"
password = "AEHEKFjGqDMZ"

# Connect to IMAP server
def connect_mail():
    mail = imaplib.IMAP4_SSL("imap.zoho.in")
    mail.login(username, password)
    mail.select("inbox")
    return mail

# Extract text from email
def extract_email_content(msg):
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8", errors="ignore")

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and part.get('Content-Disposition') is None:
                try:
                    body = part.get_payload(decode=True).decode(errors="ignore")
                except:
                    body = ""
                break
    else:
        try:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        except:
            body = ""

    return subject, body

# Main monitor loop
def monitor_inbox():
    mail = connect_mail()
    last_seen_id = None

    while True:
        try:
            mail.select("inbox")
            status, messages = mail.search(None, "ALL")
            email_ids = messages[0].split()

            if not email_ids:
                continue

            latest_id = email_ids[-1]

            # Only process if new
            if latest_id != last_seen_id:
                last_seen_id = latest_id

                status, msg_data = mail.fetch(latest_id, "(RFC822)")
                msg = email.message_from_bytes(msg_data[0][1])

                subject, body = extract_email_content(msg)
                email_text = subject + " " + body
                prediction = spamvision_model.predict([email_text])[0]

                print(f"📧 New Email: {subject}")
                print(f"🧠 Prediction: {prediction}")

                notification.notify(
                    title=f"SpamVision: {prediction.upper()} Email",
                    message=f"From: {msg.get('From')}\nSubject: {subject}",
                    timeout=10
                )

        except Exception as e:
            print("⚠️ Error:", e)

        time.sleep(10)  # Check every 10 seconds

# Run
monitor_inbox()
