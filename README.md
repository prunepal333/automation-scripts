# automation-scripts
Collection of scripts that automates my workspace and environment.
# Warning to developers: It is meant to be used for development/learning purpose only.

(DISCLAIMER: Some file requires root prviliges to make changes to root-owned files and directories)


a2configsite.py => It is used to create vhosts in apache server.
[Usage]: sudo python3 a2configsite.py example.com bugs.example.com project.example.com

a2delsite.py => It is used to remove vhosts from apache server.
[Usage]: sudo python3 a2delsite.py example.com bugs.example.com project.example.com
