import  webbrowser
from email.mime.multipart  import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from string import Template 
from pathlib import Path

template = Template(Path("template.html").read_text())
body = template.substitute({"name": "core "})
message  = MIMEMultipart()
message["from"] = "Core cena "
message["to"] = "coreweb387@gmail.com"
message["subject "] = " This is a python test of email module"
message.attach(MIMEText(body , "html"))
message.attach(Path("sinan.jpg").read_bytes())

with smtplib.SMTP( host ="smtp.gmail.com", port=587) as  smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("wanzusinani@gmail.com","KaboomISIS@1")
    smtp.send_message(message)
    print("sent ...")

#webbrowser.open("https://www.google.com")