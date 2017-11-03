import sendgrid
from sendgrid.helpers import mail
from random import *

api = sendgrid.SendGridAPIClient(apikey='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')

m = raw_input('Enter email: ')
#sub = raw_input('Subject: ')
#test = raw_input('message: ')
recipient = mail.Email(m)
count = 0

#while True:
	#try:
		
		sender = mail.Email('TEST@noreply.com')
		subject = 'SMTP TEST'
		body = mail.Content('text/plain', 'Whats up')

		email = mail.Mail(sender, subject, recipient, body)
		response = api.client.mail.send.post(request_body=email.get())
		count+=1
		print('sent')
		print('total sent mail is',count)
	#except:
	#	KeyboardInterrupt()

#print(response.status_code)
#print(response.body)
#print(response.headers)

