import os
import subprocess as sp
import time
import remote_start
import remote_main_menu

########################################## DOCKER STORAGE #############################################
def remote_docker_storage():
	os.system("clear")
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print('''
[1] CREATE VOLUME
[2] VOLUME INFO
[3] ATTACH VOLUME TO CONTAINER
[4] SHOW VOLUMES
[5] REMOVE VOLUMES
[6] REMOVE ALL VOLUMES

[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("VOLUME NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker volume create {inp}")
		elif i==2:
			inp=input("VOLUME NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker volume inspect {inp}")
		elif i==3:
			inp=input("CONTAINER NAME : ")
			inp1=input("VOLUME NAME : ")
			inp2=input("IMAGE NAME  : ")
			inp3=input("ATTACH VOLUME TO ANY FOLDER (y/n) : ")
			if inp3.lower()[0]=='y':
				inp4=input("PATH TO FOLDER : ")
				os.system(f"ssh {remote_main_menu.remoteIP} docker run -dit --name {inp} -v {inp1}:{inp4} {inp2}")
			else:
				os.system(f"ssh {remote_main_menu.remoteIP} docker run -dit --name {inp} -v {inp1} {inp2}")
		elif i==4:
			os.system(f"ssh {remote_main_menu.remoteIP} docker volume ls")
		elif i==5:
			inp=input("VOLUME NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker volume rm {inp}")
		elif i==6:
			os.system(f"ssh {remote_main_menu.remoteIP} docker volume prune")		
		elif i==0:
			remote_main_menu.items()
		elif i==99:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue.......")
		os.system("tput setaf 15 && clear")

