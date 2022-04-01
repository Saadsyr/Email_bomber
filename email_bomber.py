import smtplib
import time
mail = smtplib.SMTP("smtp.gmail.com",587)

mail.starttls() # securly send

mail.login("","") # put sender email in first parameter, your password in second one

SUBJECT = 'subject' #subject of the email
TEXT = ' body of the email '
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

for i in range(0,10):  # send 10 emails to bomb target mail

    



    mail.sendmail("",'',message) # sender email, reciever email

mail.quit()
