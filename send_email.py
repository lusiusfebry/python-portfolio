import smtplib
import ssl

host = "smtp.gmail.com"
port = 465
username="febrypythontest@gmail.com"
password = "ofampvnzxxvyrgtl"

receiver = "lusiusf@yahoo.com"
context = ssl.create_default_context()

message = """\
Subject: test
Just testing
"""
with smtplib.SMTP_SSL(host,port,context=context) as server :
    server.login(username,password)
    server.sendmail(username,receiver,message)



