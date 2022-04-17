import os
import smtplib
from collections import Counter
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USER_GMAIL')
password = os.getenv('PWD_GMAIL')
mail_from = os.getenv('USER_GMAIL')
email_gmail_dm = os.getenv('DESTINATION_EMAIL')
email_sys_dm = os.getenv('EMAIL_SYS_DM')
email_sys_al = os.getenv('EMAIL_SYS_AL')

def tagsStadistics(tagsArray):
    tagsList = Counter(tagsArray)
    listRank = tagsList.most_common(5)
    return listRank
    
def sabanaList(sabanaArray, avgLines, tagsArray):
    sabanaLenght = len(sabanaArray)
    listRank = tagsStadistics(tagsArray)
    html_body = '''
        <!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>HTML</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">        
        </head>
        <body>
            <header>
            <div style = "text-align:center;">
            <img src="https://mussun.com/wp-content/uploads/2019/08/Systemair_logo-768x237.jpg" alt="www.systemair.es">
            </div>
            </header>
            <div style= "background-color: #1a4c7f; text-align: left; color: white; font-family: 'Lato', sans-serif; padding: 10px">
        '''

    htmlBodyTitle = f'''
                <h1>Se han revisado {sabanaLenght} UTA's</h1>'''

    htmlBodyTable = f'''
                <table style= "width: 100%; background-color: #1a4c7f; font-size: 14px; border-collapse: collapse;">
                    <tr>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Pedido</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">MO</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Modelo</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Inspector</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Líneas de sábana</th>
                    </tr>
        '''
    html_sabana = ''' '''

    html_body_end = f'''
                </table>
                <h3 style = "color: white">Los equipos tienen una media de {avgLines:.1f} líneas.</h3>
                 <table style= "width: 50%; background-color: #1a4c7f; font-size: 14px; border-collapse: collapse; text-align: center; margin-left: auto; margin-right: auto;">
                    <tr>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 22px;">TAG's</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 22px;">Veces</th>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[0][0]}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[0][1]}</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[1][0]}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[1][1]}</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[2][0]}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[2][1]}</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[3][0]}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[3][1]}</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[4][0]}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{listRank[4][1]}</td>
                    </tr>
                </table>
                <hr style = padding: 8px; color: white;>
                <p style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 12px">Este correo electrónico ha sido generado automáticamente. Si no desea recibir mas correos como este escriba un correo a {email_sys_dm}.</p>
            </div>
        </body>
        </html>
        '''
    a = 0
    for sabana in sabanaArray:
        if a % 2 == 0:
            html_sabana = html_sabana + '<tr style = "background-color: #33689D;"><td style = "text-align: center; padding: 8px; color: white;"><a href=' + sabana.url + ' style = "color: white; background-color: transparent; text-decoration: none; font-weight: bold;" target= "_blank">' + sabana.order + '</td><td style= "text-align: center; padding: 8px; color: white;">' + str(sabana.mo) + '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.model + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.inspector + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.lines) + '</td></tr>'
        else:
            html_sabana = html_sabana + '<tr style = "background-color: #1a4c7f;"><td style = "text-align: center; padding: 8px; color: white;"><a href=' + sabana.url + ' style = "color: white; background-color: transparent; text-decoration: none; font-weight: bold;" target= "_blank">' + sabana.order + '</td><td style= "text-align: center; padding: 8px; color: white;">' + str(sabana.mo) + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.model + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.inspector + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.lines) + '</td></tr>'
        a = a + 1
    htmlEmail = html_body + htmlBodyTitle + \
        htmlBodyTable + html_sabana + html_body_end
    return htmlEmail


def sendEmail(mail_subject, mail_body, avgLines, tagsArray):
    
    dateGraph = datetime.now()
    dateGraphWeekNumber = dateGraph.strftime('%U')
    dateGraphWeek = int(dateGraphWeekNumber) - 1
    
    path_attach = f'avg_week_{dateGraphWeek}_graph.png'
    name_attach = f'avg_week_{dateGraphWeek}_graph.png'

    listEmails = [email_gmail_dm, email_sys_dm, email_sys_al]

    mimemsg = MIMEMultipart()
    mimemsg['From'] = mail_from
    mimemsg['To'] = ', '.join(listEmails)
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(MIMEText(sabanaList(mail_body, avgLines, tagsArray), 'html'))
    archivo_adjunto = open(path_attach, 'rb')
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    adjunto_MIME.set_payload((archivo_adjunto).read())
    encoders.encode_base64(adjunto_MIME)
    adjunto_MIME.add_header('Content-Disposition',
                            "attachment; filename= %s" % name_attach)
    mimemsg.attach(adjunto_MIME)
    try:
        connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
        connection.starttls()
        connection.login(username, password)
        connection.send_message(mimemsg)
        connection.quit()
        print('>> EMAIL SENDED <<')
    except:
        print('Algo salió mal... El email no pudo ser enviado.')
