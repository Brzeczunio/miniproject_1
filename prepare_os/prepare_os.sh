#! /bin/bash

# CZYSZCZENIE KONSOLI
clear

# INSTALACJA GUI
sudo yum groupinstall "GNOME Desktop" -y # instalacja GUI
systemctl isolate graphical.target # odpala GUI
systemctl set-default graphical.target # ustawia odpalanie GUI przy uruchomieniu systemu

# AKTUALIZACJA SYSTEMU
sudo yum update -y

# INSTALACJA EDYTORA TEKSTU ATOM
wget https://atom-installer.github.com/v1.25.0/atom.x86_64.rpm
sudo yum install atom.x86_64.rpm -y
rm -f atom.x86_64.rpm

# INSTALACJA PRZEGLĄDARKI CHROME
sudo yum remove google-chrome google-chrome-unstable
sudo cat << EOF > /etc/yum.repos.d/google-chrome.repo
[google-chrome]
name=google-chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
enabled=1
gpgcheck=1
gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
EOF
sudo yum install google-chrome-stable -y

# INSTALACJA CHROMEDRIVER
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -f chromedriver_linux64.zip

# INSTALACJA PYTHON-PIP
sudo yum install epel-release
sudo yum update -y
sudo yum install python-pip -y

# INSTALACJA github
sudo yum install git -y
