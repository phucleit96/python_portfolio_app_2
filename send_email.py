import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "badboy27796@gmail.com"
password = "gdfe bwww mnqk beni"

receiver = "moonknight196@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
Hello brother?
You good?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, msg=message)
