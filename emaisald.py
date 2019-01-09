# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("applechickencider123@gmail.com", "ooppproject")

# message to be sent
message = "hello world"

# sending the mail
s.sendmail("applechickencider123@gmail.com", "chickenCC2019@gmail.com", message)

# terminating the session
s.quit()