import smtplib
import ssl


def send_email(user_email,message):
    host = "smtp.gmail.com"
    port = 465
    username = "febrypythontest@gmail.com"
    password = "ofampvnzxxvyrgtl"
    receiver = f"{username}"
    context = ssl.create_default_context()

    msg = f"Subject : New email from {user_email}\n\nFrom: {user_email}\n{message}"
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg=msg)


# send_email()



