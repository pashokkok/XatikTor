from colorama import init 
from colorama import Fore, Back, Style

print( Fore.GREEN )
print('XatinkExample v1.0 BrootSoftWare')
print( Fore.BLUE )
print('                                Tor Claim wget...')
print('                                Tor Claim wget...')
print('                                Gen Syst-Key: \n \n            Copy and Past \n \n' + Fore.YELLOW + '2jsjejHEkdjutt54lkvxa83etrbKB4hUeJLiwlfu56rhcksnrix')
print( Fore.BLUE )
key = input ("Syst-Key: ")

if key == "2jsjejHEkdjutt54lkvxa83etrbKB4hUeJLiwlfu56rhcksnrix":
	print( Fore.GREEN )
	print('Active')
	print('Starting Tor.....')


import subprocess


files = ["install.sh"] 
for file in files:
    subprocess.Popen(args=["start", "bash", file], shell=True, stdout=subprocess.PIPE)
	
else:
	print( Fore.RED )
	print('ERROR: 101' + Fore.YELLOW + '$' + Fore.RED + 'Invalid Syst-Key')