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
recipients = os.getenv('RECIPIENT')
email_sys_dm = os.getenv('EMAIL_SYS_DM')


def tagsStadistics(tagsArray):
    tagsList = Counter(tagsArray)
    listRank = tagsList.most_common(5)
    return listRank


def sabanaList(sabanaArray, avgLines, tagsArray, avgWorkers):
    sabanaLenght = len(sabanaArray)
    listRank = tagsStadistics(tagsArray)
    try:
        percentTags1 = (listRank[0][1] / sabanaLenght) * 100
    except:
        percentTags1 = 0

    try:
        percentTags2 = (listRank[1][1] / sabanaLenght) * 100
    except:
        percentTags2 = 0

    try:
        percentTags3 = (listRank[2][1] / sabanaLenght) * 100
    except:
        percentTags3 = 0

    try:
        percentTags4 = (listRank[3][1] / sabanaLenght) * 100
    except:
        percentTags4 = 0

    try:
        percentTags5 = (listRank[4][1] / sabanaLenght) * 100
    except:
        percentTags5 = 0

    try:
        tag_1 = listRank[0][0]
    except:
        tag_1 = "N/A"

    try:
        tag_2 = listRank[1][0]
    except:
        tag_2 = "N/A"

    try:
        tag_3 = listRank[2][0]
    except:
        tag_3 = "N/A"

    try:
        tag_4 = listRank[3][0]
    except:
        tag_4 = "N/A"

    try:
        tag_5 = listRank[4][0]
    except:
        tag_5 = "N/A"

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
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Nº operarios</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Nº Tags</th>

                    </tr>
        '''
    html_sabana = ''' '''

    html_body_end = f'''
                </table>
                <h3 style = "color: white">Los equipos tienen una media de {avgLines:.1f} líneas.</h3>
                <h3 style = "color: white">La media es de {avgWorkers:.1f} operarios por equipo.</h3>

                 <table style= "width: 50%; background-color: #1a4c7f; font-size: 14px; border-collapse: collapse; text-align: center; margin-left: auto; margin-right: auto;">
                    <tr>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 22px;">TAG's</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 22px;">Porcentaje</th>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{tag_1}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{percentTags1:.1f} %</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{tag_2}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{percentTags2:.1f} %</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{tag_3}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{percentTags3:.1f} %</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{tag_4}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{percentTags4:.1f} %</td>
                    </tr>
                    <tr style = "background-color: #33689D;">
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{tag_5}</td>
                        <td style = "text-align: center; padding: 8px; color: white; font-weight: bold; font-size: 18px">{percentTags5:.1f} %</td>
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
                str(sabana.lines) + '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.numberWorkers) + '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.numberTags) + '</td></tr>'
        else:
            html_sabana = html_sabana + '<tr style = "background-color: #1a4c7f;"><td style = "text-align: center; padding: 8px; color: white;"><a href=' + sabana.url + ' style = "color: white; background-color: transparent; text-decoration: none; font-weight: bold;" target= "_blank">' + sabana.order + '</td><td style= "text-align: center; padding: 8px; color: white;">' + str(sabana.mo) + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.model + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.inspector + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.lines) + '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.numberWorkers) + '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.numberTags) + '</td></tr>'
        a = a + 1
    htmlEmail = html_body + htmlBodyTitle + \
        htmlBodyTable + html_sabana + html_body_end
    return htmlEmail


def sendEmail(mail_subject, mail_body, avgLines, tagsArray, avgWorkers):

    dateGraph = datetime.now()
    dateGraphWeekNumber = int(dateGraph.strftime('%W')) - 1
    dateGraphWeek = int(dateGraphWeekNumber)

    path_attach = f'/home/dani/projects/rework_study/avg_week_{dateGraphWeek}_graph.png'
    name_attach = f'/home/dani/projects/rework_study/avg_week_{dateGraphWeek}_graph.png'

    mimemsg = MIMEMultipart()
    mimemsg['From'] = username
    mimemsg['To'] = 'morala84@gmail.com, alberto.solar@systemair.es, antonio.mencias@systemair.es, said.hajjaje@systemair.es, fernando.vaquero@systemair.es'
    mimemsg['Subject'] = mail_subject
    mimemsg.attach(
        MIMEText(sabanaList(mail_body, avgLines, tagsArray, avgWorkers), 'html'))
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
    except Exception as e:
        print('Algo salió mal... El email no pudo ser enviado.')
        print(f'EXCEPTION: {e}')
