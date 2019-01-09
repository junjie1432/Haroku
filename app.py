import smtplib


def send_email(user, pwd, recipient, subject, body):
    FROM = user
    TO = recipient
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print( 'successfully sent the mail')
    except:
        print ("failed to send mail")

send_email("applechickencider123@gmail.com","ooppproject","chickenCC2019@gmail.com","Hellosadsadsadsadsadsadsadsadsadsadsadsad Worlo","bye12312312312312312312312312312bye")