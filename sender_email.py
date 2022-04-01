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
        <style>
        a href {
            color:white
        }
        header {
            text-align: center;
        }
        section {
            padding: 30px;
            text-align: left;
            background: #1a4c7f;
            color: white;
            font-family: 'Lato', sans-serif;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            padding: 10px;
        }
          
        th, td {
            text-align: center;
            padding: 8px;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #33689D;
        }

        a:link {
          color: white;
          background-color: transparent;
          text-decoration: none;
          font-weight: bold;
        }
        a:visited {
          color: white;
          background-color: transparent;
          text-decoration: none;
          text-decoration: underline;

        }
        a:hover {
          color: white;
          background-color: transparent;
          text-decoration: underline;
        }
        a:active {
          color: yellow;
          background-color: transparent;
          text-decoration: underline;
        }
        </style>
        </head>
        <body>
            <header>
            <img src="https://www.systemair.com/fileadmin/template_screen/img/systemair-b2b/logo.svg" alt="www.systemair.es" width="370" height="170">
            </header>
        <section>
        <h1>Listado de equipos revisados:</h1>
        <table>
            <tr>
                <th>Pedido</th>
                <th>MO</th>
                <th>Modelo</th>
                <th>Inspector</th>
                <th>Líneas de sábana</th>
            </tr>
        '''
    html_sabana = ''' '''
    
    html_body_end = f'''
        </table>
        <h4>La media de lineas por equipo es de {avgLines:.1f} lineas.
        </section>
        </body>
        </html>
        '''
    for sabana in (sabanaArray):
        html_sabana = html_sabana + '<tr><td><a href=' + sabana.url + ' target= "_blank">' + \
            sabana.order + '</td><td>' + str(sabana.mo) + \
                '</td><td>' + sabana.model + '</td><td>' + sabana.inspector + '</td><td>' + str(sabana.lines) + '</td>'
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
