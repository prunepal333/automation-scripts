import os
import sys

n = len(sys.argv)

if n < 2:
    print(f"[Usage]: python3 {sys.argv[0]} domain_name1 [,domain_name2[,domain_name3[,...]]]")
    os._exit(1)
for i in range(1, n):
    domain = sys.argv[i]
    os.system(f"sudo rm -rf /var/www/{domain}")
    os.system(f"sudo a2dissite {domain}.conf")
    # os.system("clear")
    os.system(f"sudo rm -f /etc/apache2/sites-available/{domain}.conf")
    os.system("sudo systemctl reload apache2")
    # os.system(f"sudo sed -i '/^{domain}$/d' /etc/hosts")
    # os.system(f"sudo sed -i '/^www.{domain}$/d' /etc/hosts")
    
    f = open("/etc/hosts", "r")
    lines = f.readlines()
    f.close()

    f = open("/etc/hosts", "w")
    for line in lines:
        if domain not in line:
            # continue
            f.write(line)
 
    f.close()