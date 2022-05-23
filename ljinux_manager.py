#Import libraries

import os 
from time import sleep

print("Welcome to the ljinux manager scipt.\n")

#Functions

def connect():
	print("You must have screen command installed.")
	sleep(1)
	input("Press enter to connect...")
	os.system("cd src/ && git clone https://github.com/bill88t/ljinux.git")
	os.system("cd src/ljinux/source && make connection")

def flash():
	input("Please connect your pico with the boot select button pressed and press enter.")
	sleep(1)
	print("Formating...")
	sleep(1)
	os.system("cp src/format.uf2 /media/$USER/RPI-RP2/")
	sleep(20)
	print("Flashing circuit python...")
	sleep(1)
	os.system("cp src/circuit_python.uf2 /media/$USER/RPI-RP2/")
	sleep(20)
	print("Flashing ljinux...")
	sleep(1)
	os.system("cd src/ && git clone https://github.com/bill88t/ljinux.git")
	sleep(1)
	os.system("cd src/ljinux/source && make install")
	sleep(1)
	print("Installation done! Now rerun the script with the connect option.")
#Preparation

do = input("Please type flash for flash and connect for connect: ")

if do == "connect":
	connect()
elif do == "flash":
	flash()
else:
	print("Wrong instructions")


