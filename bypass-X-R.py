import os, platform
try:os.system('git pull')
except:pass
try:os.mkdir('OK')
except:pass
try:os.mkdir('CP')
except:pass
try:os.system('touch .prox.txt')
except:pass
 
import requests
bit = platform.architecture()[0]
if bit == '64bit':
import GREEN
GREEN.login()

elif bit == '32bit':
import GREEN32
GREEN32.login()
