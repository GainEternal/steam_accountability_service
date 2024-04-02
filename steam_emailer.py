import smtplib
from email.message import EmailMessage

def send_game_email(content:str, sender:str, password:str, receiver:str|list[str], subject:str='', logger=''):
    msg = EmailMessage()
    msg.set_content(content)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver if isinstance(receiver, str) else ', '.join(receiver)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(msg)
            if logger:
                logger.log(f'Email sent to {receiver}')
