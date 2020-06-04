"""

This program will explain how to send emails using python
port might changes based on the email providers , for most of them it is 587 and for verizon and AT&T it is 465

NOTE : google application specific password to generate password for using these type of applications

"""

import smtplib

conn =smtplib.SMTP('smtp.gmail.com',587)
type(conn)

conn.ehlo()  # gives a tuple having response code and bytes object , if status is 200 or 250 it is fine

conn.starttls()
conn.login('email_id','password')
conn.sendmail('from_address','to_Address','body of the mail')  # Subject:   \n\n Body of the mail
# gives blank dictionary if all mails send successfully

conn.quit()   # closing the connection
