from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib


class Mail(object):
	def __init__(self):
		# 配置邮箱及密码
		self.from_mail = input("Login:")
		self.from_mail_password = input("Input password:")
		self.to_mail = input("Send to:")



		# 设置总的邮件体对象，对象类型为mixed
		self.msg = MIMEMultipart('mixed')

		# 邮件的发件人及收件人信息
		self.msg['From'] = self.from_mail
		self.msg['To'] = self.to_mail

		# 邮件的主题
		self.msg['Subject'] = input("Email title:")

	def text(self):
		# 构造文本内容
		self.text_info = open(r'./resource/email/text.txt', 'r').read()
		self.text_sub = MIMEText(self.text_info, 'plain', 'utf-8')
		self.msg.attach(self.text_sub)

	def href(self):
		# 构造附件
		self.f = input("File name:")
		self.txt_file = open(r'./resource/email/'+f, 'rb').read()
		self.txt = MIMEText(self.txt_file, 'base64', 'utf-8')
		self.txt["Content-Type"] = 'application/octet-stream'
		self.txt.add_header('Content-Disposition', 'attachment', filename=f)
		self.msg.attach(self.txt)

	def send(self):
		try:
			self.server = smtplib.SMTP(input("Server:"))
			self.server.docmd('ehol', self.from_mail)
			self.server.starttls()
			self.server.login(self.from_mail,self.from_mail_password)

			self.server.sendmail(self.from_mail,self.to_mail,self.msg.as_string())
			self.server.quit()
			print('sendemail successful!')
		except Exception as e:
			print('sendemail failed next is the reason')
			print(e)

