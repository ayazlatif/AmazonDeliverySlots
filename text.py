import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CARRIERS = ['@txt.att.net','@pm.sprint.com','@tmomail.net','@vtext.com','@myboostmobile.com',
        '@sms.mycricket.com','@mymetropcs.com','@mmst5.tracfone.com','@email.uscc.net','@vmobl.com']


def clean_up_phone(phone):
    return phone.replace("(", "").replace(")", "").replace(" ", "").replace("-","")

def send_text(phone_info, message):
    email, password, phone, carrier = phone_info
    phone = clean_up_phone(phone)
    sms_address = phone + CARRIERS[carrier]

    # start up server
    smtp = "smtp.gmail.com" 
    port = 587
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(email, password)

    # format message
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = sms_address
    body = "%s\n" % message
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email, sms_address, sms)
    server.quit()