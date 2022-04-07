import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
load_dotenv()

def sabanaList(sabanaArray, avgLines):
    sabanaLenght = len(sabanaArray)
    html_body = '''
        <!DOCTYPE html>
<<<<<<< HEAD
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>HTML</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="estilo.css">
        
        </head>
        <body>
            <header>
            <div style = "text-align:center;">
            <img src="https://mussun.com/wp-content/uploads/2019/08/Systemair_logo-768x237.jpg" alt="www.systemair.es" width="390" height="170">
            </div>
            </header>
        <section style= "padding: 30px; text-align: left; background: #1a4c7f; color: white; font-family: 'Lato', sans-serif;">
        '''
        
    htmlBodyTitle = f'''
                <h1>Se han revisado {sabanaLenght} UTA's</h1>'''
        
    htmlBodyTable = f'''
                <table style= "border-collapse: collapse; width: 100%; padding: 10px; background-color: #1a4c7f; font-size: 14px;">
                    <tr>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Pedido</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">MO</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Modelo</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Inspector</th>
                        <th style= "text-align: center; padding: 8px; color: white; font-size: 18px;">Líneas de sábana</th>
                    </tr>
=======
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
			<img src="https://www.systemair.com/fileadmin/template_screen/img/systemair-b2b/logo.svg" alt="http://www.systemair.es" width="370" height="170">
		</header>
		<section>
        '''
        
    htmlBodyTitle = f'			<h1>Listado: {sabanaLenght} equipos revisados.</h1>'
        
    htmlBodyTable = f'''
			<table>
				<tr>
					<th>Pedido</th>
					<th>MO</th>
					<th>Modelo</th>
					<th>Inspector</th>
					<th>Líneas de sábana</th>
				</tr>
>>>>>>> 575eed7a1aeb489c88c3bd4e644ee72d6f9b1d89
        '''
    html_sabana = ''' '''
    
    html_body_end = f'''
<<<<<<< HEAD
                </table>
                <h3>Los equipos tienen una media de {avgLines:.1f} líneas.</h3>
        </section>
        </body>
        </html>
        '''
    a = 0
    for sabana in sabanaArray:
        if a % 2 == 0:
            html_sabana = html_sabana + '<tr style = "background-color: #33689D;"><td style = "text-align: center; padding: 8px; color: white;"><a href=' + sabana.url + ' style = "color: white; background-color: transparent; text-decoration: none; font-weight: bold;" target= "_blank">' + sabana.order + '</td><td style= "text-align: center; padding: 8px; color: white;">' + str(sabana.mo) +'</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.model + \
            '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.inspector + \
            '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
            str(sabana.lines) + '</td>'
        else:
            html_sabana = html_sabana + '<tr style = "background-color: #1a4c7f;"><td style = "text-align: center; padding: 8px;color: white;"><a href=' + sabana.url + ' style = "color: white; background-color: transparent; text-decoration: none; font-weight: bold;" target= "_blank">' + sabana.order + '</td><td style= "text-align: center; padding: 8px; color: white;">' + str(sabana.mo) + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.model + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + sabana.inspector + \
                '</td><td style= "text-align: center; padding: 8px; color: white;">' + \
                str(sabana.lines) + '</td>'
        a = a + 1       
=======
			</table>
			<h3>Los equipos tienen una media de {avgLines:.1f} líneas.</h3>
		</section>
	</body>
</html>
        '''
    for sabana in (sabanaArray):
        html_sabana = html_sabana + '               <tr><td><a href=' + sabana.url + ' target= "_blank">' + \
            sabana.order + '</td><td>' + str(sabana.mo) + \
                '</td><td>' + sabana.model + '</td><td>' + sabana.inspector + '</td><td>' + str(sabana.lines) + '</td>'
>>>>>>> 575eed7a1aeb489c88c3bd4e644ee72d6f9b1d89
    htmlEmail = html_body + htmlBodyTitle + htmlBodyTable + html_sabana + html_body_end
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
