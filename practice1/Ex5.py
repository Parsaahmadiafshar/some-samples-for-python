import smtplib

USER = input('Enter your gmail ====>>')
PASS = input('Enter your password =====>> ')

FROM = USER
TO = input('who do you want to send a message to?(Enter his gmail) ====>>')

MS = input('now Enter a message =====>> ')

server = smtplib.SMTP()
server.connect("smtp.gmail.com", 587)
server.starttls()
server.login(USER, PASS)
server.sendmail(FROM, TO, MS)
server.quit()
