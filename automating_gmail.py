import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('fromAdress@gmail.com','password$') # (fromAdress, password)
conn.sendmail('fromAdress@gmail.com','toAdress@gmail.com',"Subject: Test \n\n message body \n\n -signature") # (fromAdress, toAdress, message)