import smtplib, requests, json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from .templates import *

class Email:

    def Send_Documents(self,name_zip,invoice):
        remitente = 'facturas.theriosoft@gmail.com'
        destinatarios = ["notificacionesoftware@gmail.com",]
        asunto = 'Aceptación de factura N° '+str(invoice.number)
        html = SEND_DOCUMENT
        html = html.replace("$(client_name)",invoice.client.name)
        html = html.replace("$(invoice_number)",str(invoice.number))
        html = html.replace("$(pk_company)",str(invoice.company.pk))
        ruta_adjunto = 'C:/laragon/www/api/storage/app/public/'+str(invoice.company.nit)+'/'+name_zip
        nombre_adjunto = name_zip
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(html,'html'))
        archivo_adjunto = open(ruta_adjunto, 'rb')     
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        adjunto_MIME.set_payload((archivo_adjunto).read())
        encoders.encode_base64(adjunto_MIME)
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        mensaje.attach(adjunto_MIME)
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        sesion_smtp.starttls()
        texto = mensaje.as_string()
        usuario = 'facturacionelectronica2030@gmail.com'
        clave = 'webqbjzogcbqhtew'
        sesion_smtp.login(usuario,clave)
        sesion_smtp.sendmail(remitente, destinatarios, texto)
        sesion_smtp.quit()

    def Send_Thanks(self,name_zip,invoice):
        remitente = 'facturas.theriosoft@gmail.com'
        destinatarios = ["notificacionesoftware@gmail.com",]
        asunto = 'Aceptación de factura N° '+str(invoice.number)
        html = SEND_THANKS
        html = html.replace("$(client_name)",invoice.client.name)
        html = html.replace("$(cufe)",invoice.cufe)
        html = html.replace("$(invoice_number)",str(invoice.number))
        ruta_adjunto = 'C:/laragon/www/api/storage/app/public/'+str(invoice.company.nit)+'/'+name_zip
        nombre_adjunto = name_zip
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = ", ".join(destinatarios)
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(html,'html'))
        archivo_adjunto = open(ruta_adjunto, 'rb')     
        adjunto_MIME = MIMEBase('application', 'octet-stream')
        adjunto_MIME.set_payload((archivo_adjunto).read())
        encoders.encode_base64(adjunto_MIME)
        adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
        mensaje.attach(adjunto_MIME)
        sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        sesion_smtp.starttls()
        texto = mensaje.as_string()
        usuario = 'facturacionelectronica2030@gmail.com'
        clave = 'webqbjzogcbqhtew'
        sesion_smtp.login(usuario,clave)
        sesion_smtp.sendmail(remitente, destinatarios, texto)
        sesion_smtp.quit()

