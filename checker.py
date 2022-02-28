# import module
import os
import psutil
import time
#Verificacion para saber si el cs esta abierto (True = 1) (False= 0)
processChecker = "csgo.exe" in (i.name() for i in psutil.process_iter())
#Verificacion para saber si myScripts esta abierto (True = 1) (False= 0)
qst = "open-chrome.exe" in (i.name() for i in psutil.process_iter())
#Verificacion para saber si python.exe esta abierto (True = 1) (False= 0)
qsyPy = "python.exe" in (i.name() for i in psutil.process_iter())
#esta funcion mata los medios (cmd and python)
qsyPyw = "pythonw.exe" in (i.name() for i in psutil.process_iter())
def terminateAll():
	if processChecker == True:
		os.system('TASKKILL /F /IM cmd.exe')
		if qsyPy == True:
			os.system('TASKKILL /F /IM python.exe')
	elif processChecker == False and qst == False:
		os.system('TASKKILL /F /IM cmd.exe')
		if qsyPy == True:
			os.system('TASKKILL /F /IM python.exe')
		elif qsyPyw ==  True:
			os.system('TASKKILL /F /IM pythonw.exe')

while qst == True:
	# Chekea si el csgo esta abierto
	if "csgo.exe" in (i.name() for i in psutil.process_iter()):
		#Mata el proceso de myScripts
		os.system('TASKKILL /F /IM open-chrome.exe')
	#Aca se da un tiempo entre pruebas de 5segs y eso reduce la carga del cpu
	time.sleep(5)
else:
	terminateAll()
terminateAll()