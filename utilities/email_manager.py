from pydantic import EmailStr
import smtplib
from email.message import EmailMessage
from config import settings
from string import Template
from pathlib import Path


def send_email_with_subject(email_from: str, email_to: str, email_subject: str, email_content: str):
    email = EmailMessage()
    email['from'] = email_from
    email['to'] = email_to
    email['subject'] = email_subject
    email.set_content(email_content)
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(settings.email_address, settings.email_password)
        smtp.send_message(email)
        # print('sent')


def send_mail(reciever: EmailStr, content: str):
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
        email_address = settings.email_address
        email_password = settings.email_password
        connection.login(email_address, email_password)
        connection.sendmail(from_addr=email_address, to_addrs=reciever,
                            msg=content)


#TODO: fix the parameters, maybe use the name and link as parameters or something else.
def send_html_email_with_subject(email_from: str, email_to: str, email_subject: str, email_content: str):
    html = Template(Path('utilities/templates/reset.html').read_text())
    content = html.substitute(
    {'name': 'name', 'link': 'link'})
    email = EmailMessage()
    email['from'] = email_from
    email['to'] = email_to
    email['subject'] = email_subject
    email.set_content(email_content, 'html')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(settings.email_address, settings.email_password)
        smtp.send_message(email)
