import smtplib
import getpass
import time

mail_from = input("Gmail From :")
password = getpass.getpass("Password (not shown) :")
mail_to = input("Mail To :")
subject = ('Subject: ' + input("Subject :"))
body = input("Body :")
rpt =  int(input("Repeat (N° of emails) :"))
timer = int(input("time between emails (seconds)"))
ctn = 0



while (ctn < rpt) :
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    conn.starttls()
    conn.login(mail_from,password) # (fromAdress, password)
    conn.sendmail(mail_from, mail_to, subject, body) # (fromAdress, toAdress, message)
    ctn += 1
    time.sleep(timer)
