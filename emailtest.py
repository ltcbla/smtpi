import smtplib
import email.utils
import string





try:
	d = raw_input('Send email or not? Y/N: ')
	
	if d == 'y':
		content = raw_input('Type your message: ')
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.login('internjtest@gmail.com','jabiljabil')
		mail.sendmail('internjtest@gmail.com','lim.agent@gmail.com',content)
		mail.close()
	elif d == 'n':
		print 'OKAY.'
		
	
		
except KeyboardInterrupt():
		reset()
	


