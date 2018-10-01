import smtplib
from os.path import basename 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.utils import COMMASPACE, formatdate 

def send_mail(send_from, send_to, subject, text, files=None):
    from_email=""
    from_password=""
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = ",".join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    email_text = """\
    From: %s
    To: %s
    Subject: %s
    %s
    """ % (send_from, ", ".join(send_to), subject, text)
    body=MIMEText(text,'html')
    msg.attach(body)
    with open(files, "rb") as fil:
        part = MIMEApplication(fil.read(),Name=basename(files))
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(files)
        msg.attach(part)

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.sendmail("asc",send_to,msg.as_string())
    gmail.close()
