import openai
import smtplib
from email.message import EmailMessage
import schedule
import time

# 1. Set up your credentials
openai.api_key = "your-openai-api-key"
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_ADDRESS = "your_email@gmail.com"

# 2. Generate affirmations using ChatGPT
def generate_affirmations():
    prompt = (
        "Generate 6 short, powerful affirmations that boost confidence, wealth mindset, and daily motivation."
        " Each one should be a single sentence, present tense, no more than 15 words."
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.9
    )
    return response.choices[0].message.content.strip()

# 3. Send the affirmations via email
def send_email(affirmations):
    msg = EmailMessage()
    msg["Subject"] = "Your Daily Affirmations 🌞"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_ADDRESS
    msg.set_content(affirmations)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("✅ Affirmations sent!")

# 4. Combine generation + sending
def generate_and_send():
    affirmations = generate_affirmations()
    send_email(affirmations)

# 5. Schedule for every day at 8:00 AM
schedule.every().day.at("08:00").do(generate_and_send)

# 6. Run the script
while True:
    schedule.run_pending()
    time.sleep(60)
