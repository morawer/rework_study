import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

def sabanaList(sabanaArray, avgLines):
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
        <h1>Listado de equipos revisados:</h1>
        <ol>
        '''
    html_sabana = ''' '''
    
    html_body_end = f'''
        </ol>
        <h4>La media de lineas por equipo es de {avgLines:.1f} lineas.
        </body>
        </html>
        '''
    for sabana in (sabanaArray):
        html_sabana= html_sabana + '<li><a href=' + sabana.url + ' target= "_blank">' + sabana.order + '</a>' + ' >>> ' + sabana.model + ' LINEAS: ' + str(sabana.lines) + '</li>'
    htmlEmail = html_body + html_sabana + html_body_end
    return htmlEmail

def sendEmail(mail_subject, mail_body, avgLines):

    username = os.getenv('USER_GMAIL')
    password = os.getenv('PWD_GMAIL')
    mail_from = os.getenv('USER_GMAIL')
    mail_to = os.getenv('DESTINATION_EMAIL')

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = mail_to
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(sabanaList(mail_body, avgLines), 'html'))
    try:
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()
    except:
        print('Algo salió mal... El email no pudo ser enviado.')
