from email.mime.text import MIMEText
import smtplib


def send_email(email, height, average_height, count):
    from_mail = "shanmugam091098@gmail.com"
    from_password = "njuzzknyrqxbpdng"
    to_mail = email

    subject = "Height Data"

    message = f"Hey there, your height is <strong>{height}</strong>. Average height of all is <strong>{average_height}</strong>. and that calculated out of <strong>{count}</strong> of people."

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_mail
    msg["From"] = from_mail

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_mail, from_password)
    gmail.send_message(msg)
