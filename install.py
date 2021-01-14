import os 
import subprocess
import platform

print(os.name) 
print(os.uname())
print(os.system)

def linux_distro(): #Check which distro is being used
	uname = platform.uname()

	uname = str(uname)
	
	if uname.find("Ubuntu") > -1 or uname.find("ubuntu") > -1:
		return "ubuntu"
	if uname.find("Debian") > -1 or uname.find("ubuntu") > -1:
		return "debian"
	if uname.find("Mint") > -1 or uname.find("mint") > -1:
		return "mint"
	if uname.find("Knoppix") > -1 or uname.find("knoppix") > -1:
		return "mint"
	if uname.find("Deepin") > -1 or uname.find("deepin") > -1:
		return "deepin"
	if uname.find("Bodhi") > -1 or uname.find("bohdi") > -1:
		return "bohdi"
	if uname.find("Kali") > -1 or uname.find("kali") > -1:
		return "kali"
	if uname.find("Arch") > -1 or uname.find("arch") > -1:
		return "arch"
	if uname.find("Gentoo") > -1 or uname.find("gentoo") > -1:
		return "gentoo"
	if uname.find("Red hat") > -1 or uname.find("red hat") > -1:
		return "red hat"

def package_manager(distro): #Takes the name of the distro and returns the name of a package manager it uses
	if distro == "ubuntu":
		return "apt"
	if distro == "debian":
		return "apt"
	if distro == "mint":
		return "apt"
	if distro == "knoppix":
		return "apt"
	if distro == "deepin":
		return "apt"
	if distro == "bodhi":
		return "apt"
	if distro == "arch":
		return "apt"
	if distro == "kali":
		return "pacman"
	if distro == "gentoo":
		return "equo"
	if distro == "red hat":
		return "dnf"

def apps_to_install(): # check which apps are installed and which need to be installed
	ls = []
	ls.append("nodejs") if os.system("which node") else print("nodejs is already installed") 
	ls.append("curl") if os.system("which curl") else print("curl is already installed") 
	ls.append("wget") if os.system("which wget") else print("wget is already installed") 
	ls.append("doctuor") if os.system("which doctuor") else print("doctour is already installed") 

	if len(ls) == 0:
		return False
	return ls

if platform.system() == "Linux": # Installs apps on a linux OS\
	distro = linux_distro()
	pm = package_manager(distro)

	if apps_to_install() == False:
		print("all apps already intalled... exiting")
		exit()
	print("installing")
	if pm == "apt":
		os.system("apt update -y")
		os.system("apt upgrade -y")
		os.system("apt install wget curl nodejs -y")
	if pm == "pacman":
		os.system("pacman -Sc")
		os.system("pacman -Qdtq | pacman - Rs")
		os.system("pacman -Syu")
		os.system("pacman -Sy nodejs npm wget curl")
	if pm == "equo":
		os.system("emerge --ask --verbose --update --deep --unchanged-use @world")
		os.system("emerge -pv nodejs npm wget curl")
	if pm == "red hat":
		os.system("dnf update")
		os.system("dnf upgrade")
		os.system("dnf install nodejs npm wget curl")

elif platform.system() == "Mac": # Installs apps on a Mac OS

	if apps_to_install() == False:
		print("all apps already installed... exiting")
		exit()
	print("installing")
	os.system("curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh")
	os.system("brew update")
	os.system("brew upgrade")
	os.system("brew install wget curt nodejs")
	
print("Finished")