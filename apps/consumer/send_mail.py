from email.message import EmailMessage
import smtplib


class SendMail():
	template_name = 'account/password_reset/send_mail.html'
	context = []
	def __init__(self, template, context):
		self.template = template 
		self.context = context

	def send(self):
		remitente = "swodorheranndez@gmail.com"
		destinatario = " "
		mensaje = "¡Hola, mundo!"

		email = EmailMessage()
		email["From"] = remitente
		email["To"] = destinatario
		email["Subject"] = "Correo de prueba"
		email.set_content(mensaje)

		smtp = smtplib.SMTP_SSL("smtp.gmail.com")
		smtp.sendmail(remitente, destinatario, email.as_string())
		smtp.quit()