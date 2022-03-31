import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()



def sabanaList(sabanaArray):
    html_sabana = ''' '''
    for sabana in sabanaArray:
        html_sabana= html_sabana + '<li>' + sabana.order + ' >>> ' + sabana.model + '<li>'
    return str(html_sabana)



def sendEmail(mail_subject, mail_body):

    html_body = '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>HTML</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="estilo.css">
        </head>

        <body>
        '''
    html_body_end = '''
        </body>
        </html>
        '''

    username = os.getenv('USER_GMAIL')
    password = os.getenv('PWD_GMAIL')
    mail_from = os.getenv('USER_GMAIL')
    mail_to = os.getenv('DESTINATION_EMAIL')

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(html_body + sabanaList(mail_body) + html_body_end, 'html'))
    try:
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()
    except:
        print('Algo salió mal... El email no pudo ser enviado.')