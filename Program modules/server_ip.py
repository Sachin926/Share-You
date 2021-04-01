#processing out the server IP from cmd terminal using python subprocess module

import subprocess
a = subprocess.Popen("arp -a", shell = True,  stdout = subprocess.PIPE)	#running the adress resolution protocol
s = a.stdout.read().decode()	#getting the output from the cmd terminal in form of string into s
#text processing of the received string
s = s[s.index('Internet') : ]
l = s.split()
print (l[5])