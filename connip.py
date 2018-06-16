import time
import commands
print"finding connected Ips"
time.sleep(2)
print commands.getoutput("arp -a|cut -d'(' -f2|cut -d')' -f1")

