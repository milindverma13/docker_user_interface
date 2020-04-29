import os
import subprocess as sp
import time
import remote_start
import remote_main_menu
########################################## REMOTE GENERAL FUNCTION #####################################
def remote_general():
	os.system("clear")
	while True:
		remote_start.remote_start()
		os.system("tput setaf 10")
		print('''
[1] RUN NEW COMMAND
[2] HELP
[3] RUN CONTAINER
[4] DOCKER INFO
[5] RAM CONSUMPTION
[6] ALL STOPPED / RUNNING CONTAINERS
[7] REMOVE ALL (stopped + running) DOCKER  CONTAINER
[8] CREATE IMAGE
[9] CONTAINER DETAIL 
[10] CPU SHARE 
[11] PORTS RUNNING
[12] CONTAINER LOGS
[13] YUM WHATPROVIDES
[14] KERNAL VERSION
[15] ID OF ALL CONTAINERS
[16] PROCESS TREE
[17] IPTABLES
 
[0] BACK
[99] EXIT 
''')
		os.system("tput setaf 15")
		i=int(input("ENTER CHOICE : "))
		if i==1:
			inp=input("COMMAND : ")
			os.system(f"ssh {remote_main_menu.remoteIP} {inp}")
		elif i==2:
			inp=input("COMMAND INFO : ")
			os.system(f"ssh {remote_main_menu.remoteIP} man {inp}")
		elif i==15:
			os.system(f"ssh {remote_main_menu.remoteIP} docker container ls -a -q")
		elif i==3:
			inp=input("ENTER THE IMAGE_NAME:VERSION : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker run -dit {inp}")
		elif i==4:
			os.system(f"ssh {remote_main_menu.remoteIP} docker info")
		elif i==5:
			os.system(f"ssh {remote_main_menu.remoteIP} free -m")
		elif i==6:
			os.system(f"ssh {remote_main_menu.remoteIP} docker ps -a")
		elif i==7:
			os.system(f"ssh {remote_main_menu.remoteIP} docker container rm -f $(ssh {remote_main_menu.remoteIP} docker container ls -q -a)")
		elif i==8:
			inp=input("ENTER THE CONTAINER NAME : ")
			inp1=input("ENTER THE IMAGENAME WITH VERSION : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker commit {inp} {inp1}")
		elif i==9:
			inp=input ("ENTER THE CONTAINER NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker container inspect {inp}")
		elif i==10:
			os.system(f"ssh {remote_main_menu.remoteIP} lscpu")
		elif i==11:
			os.system(f"ssh {remote_main_menu.remoteIP} netstat -tnlp")
		elif i==12:
			inp=input("ENTER THE CONTAINER NAME  : ")
			os.system(f"ssh {remote_main_menu.remoteIP} docker logs  -f {inp}") # -f -> to show logs in real time
		elif i==13:
			inp=input("ENTER THE SOFTWARE NAME : ")
			os.system(f"ssh {remote_main_menu.remoteIP} yum whatprovides {inp}")
		elif i==14:
			os.system(f"ssh {remote_main_menu.remoteIP} uname -r")
		elif i==16:
			os.system(f"ssh {remote_main_menu.remoteIP} pstree")
		elif i==17:
			os.system(f"ssh {remote_main_menu.remoteIP} iptables -F && ssh {remote_main_menu.remoteIP} iptables -nvL")
		elif i==0:
			remote_main_menu.items()
		elif i==99:
			os.system("reset")
			exit()
		else:
			os.system("tput setaf 9 && echo -e 'OPTION NOT SUPPORTED !!!' && tput setaf 15")
			time.sleep(1)
		os.system("tput setaf 4")
		inp=input("enter to continue..........")
		os.system("tput setaf 15 && clear")

