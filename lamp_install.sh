#Installation of lamp stack on ubuntu machine -- PHP 8.2, Mariadb, Apache2, Curl, Composer
sudo apt update -y
sudo apt install apache2 -y
sudo apt install mariadb-server mariadb-client -y
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:ondrej/php -y
sudo apt update -y
sudo apt install php8.2 libapache2-mod-php8.2 php8.2-mysql -y
sudo apt install curl -y
curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
sudo php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
