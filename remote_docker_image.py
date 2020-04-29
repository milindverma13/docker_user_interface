import os
import subprocess as sp
import time
import remote_start
import remote_main_menu
########################################## DOCKER_IMAGE ###############################################
def remote_docker_image():				
	os.system("clear")
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print(''' 
[1] RUN NEW COMMAND 
[2] COMMIT CONTAINER 
[3] SHOW ALL IMAGES
[4] REMOVE IMAGE
[5] PULL IMAGES 
[6] PUSH IMAGES TO REGISTRY
[7] LOAD IMAGE

[0] BACK
[99] EXIT
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("COMMAND : ")
			os.system(f"ssh {remote_main_menu.remoteIP} {inp}")
		elif i==2:
			inp=input("CONTAINER NAME : ")
			inp1=input("IMAGE NAME WITH VERSION : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker commit {inp} {inp1}")
		elif i==3:
			os.system(f"ssh {remote_main_menu.remoteIP} docker image ls")
		elif i==4:
			inp=input("IMAGE NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker image rmi {inp}")
		elif i==5:
			inp=input("IMAGE NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker pull {inp}") 
		elif i==6:
			inp=input("IMAGE NAME WITH VERSION : ")
			inp1=input("DOCKER ID : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker login")
			os.system(f"ssh {remote_main_menu.remoteIP} docker tag {inp} {inp1}/{inp} && ssh {remote_main_menu.remoteIP} docker push {inp1}/{inp}")
		elif i==7:
			inp1=input("SHAREABLE NAME (with externsion .tar) : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker load -i {inp1}") 
			os.system("tput setaf 4 && echo -e 'ACTION COMPLETED' && tput setaf 15")		 	
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

