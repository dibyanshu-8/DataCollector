from email.mime.text import MIMEText
def send_email(email,heigh):
    from_email="dibyanshukarr@gmail.com"
    from_password="job@12_45"
    to_email=email
    
    
    subject="Height data"
    message="Hey there,your height is <strong> %s</strong>."
    
    msg=MIMEText(message,'html')
    msg['subject']=subject
    msg['To']=to_email
    msg['From']=from_email
    
    
    
    