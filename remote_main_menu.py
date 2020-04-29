import os
import subprocess as sp
import time
import remote_start
import main
import remote_docker_storage
import remote_docker_network
import remote_docker_container
import remote_docker_compose
import remote_docker_image
import remote_general
########################################## REMOTE MAIN MENU ############################################
def remote_main_menu():
	remote_start.remote_start()
	global remoteIP
	remoteIP = input("\n\tENTER YOUR IP ADDRESS : ")
	fileoutput='power_ranger.txt'
	output=sp.getoutput(f"nmap -sT {remoteIP} | grep ^H | cut -c 1-4")
	if "Host" in output and os.path.isfile(fileoutput)==True and remoteIP in open('power_ranger.txt').read():
		items()
	elif "Host" in output:	
		os.system("ssh-keygen")
		os.system(f"ssh-copy-id {remoteIP}")
		if os.path.isfile(fileoutput)==True:
			os.system(f"echo -e {remoteIP} >> power_ranger.txt")
		else:
			os.system(f"echo -e {remoteIP} > power_ranger.txt")
		items()	
	else:
		os.system("tput setaf 9 && echo -e 'HOST IS NOT UP !!!' && tput setaf 15")
		time.sleep(3)
		remote_main_menu()
	
########################################## REMOTE MENU ITEMS ###########################################
def items():
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print('''
[1] INSTALL DOCKER								[100] CHANGE LOCATION
[2] GENERAL 
[3] DOCKER CONTAINER
[4] DOCKER IMAGE
[5] DOCKER COMPOSE
[6] DOCKER NETWORK
[7] DOCKER STORAGE
[0] EXIT 
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			repo = sp.getoutput(f"ssh {remoteIP} rpm -q docker-ce | cut -c 1-9")
			if repo == "docker-ce":
				os.system(f"tput setaf 4 && echo -e 'DOCKER IS ALREADY INSTALLED' && tput setaf 15")
			else:
				os.system(f"ssh {remoteIP} echo -e '[docker]\nbaseurl=https://download.docker.com/linux/centos/7/x86_64/stable/\ngpgcheck=0' > /etc/yum.repos.d/docker.repo && ssh {remoteIP} dnf install docker-ce -y")
		elif i==2:
			remote_general.remote_general()
		elif i==3:
			remote_docker_container.remote_docker_container()
		elif i==4:
			remote_docker_image.remote_docker_image()
		elif i==5:
			remote_docker_compose.remote_docker_compose()
		elif i==6:
			remote_docker_network.remote_docker_network()
		elif i==7:
			remote_docker_storage.remote_docker_storage()
		elif i==100:
			docker.main()
		elif i==0:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue.......")
		os.system("tput setaf 15 && clear")

