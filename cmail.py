import smtplib
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sumanthmendadhala@gmail.com','fdho rzjf stpz zzpg')
    msg=EmailMessage() #creating object to for emailmeassage class
    msg['FROM']='sumanthmendadhala@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject 
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
    #server.close()