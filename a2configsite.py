import os
import sys
import webbrowser
os.system('cd /etc/apache2/sites-available')
n = len(sys.argv)
if n < 2:
	print(f"[Usage]: python3 {sys.argv[0]} domain_name1 [,domain_name2[,domain_name3]]")
	os._exit(0)
for i in range(1, n):
	domain = sys.argv[i]
	root_dir = "/var/www/" + domain + "/html"
	config = """<VirtualHost *:80>
			ServerAdmin	webmaster@localhost
			ServerName	""" + domain  + """
			ServerAlias	www.""" + domain + """
			DocumentRoot	""" + root_dir + """
			ErrorLog	${APACHE_LOG_DIR}/error.log
			CustomLog	${APACHE_LOG_DIR}/access.log combined
			<IfModule mod_dir.c>
				DirectoryIndex index.php index.pl index.cgi index.html index.xhtml index.htm
			</IfModule>
		</VirtualHost>
	"""
	os.system("sudo mkdir -p " + root_dir) 
	f = open(f"/etc/apache2/sites-available/{domain}.conf", "w")
	f.write(config)
	f.close()
	dnsmasquarade_ip = "127.0.0.1\t" + domain + "\n127.0.0.1\t" + domain + "\n"
	
	f = open("/etc/hosts", "r")
	content = f.read()
	f.close()

	f = open("/etc/hosts", "w")
	f.write(f"127.0.0.1\t{domain}\n127.0.0.1\twww.{domain}\n{content}")
	f.close()
	
	f = open(f"/var/www/{domain}/html/index.php", "w+")
	f.write(f"Welcome to <a href='#'>{domain}</a>. Change the content as your need.")
	f.close()
	os.system(f"sudo a2ensite {domain}.conf")
	os.system("sudo systemctl reload apache2")
	# os.system("clear")