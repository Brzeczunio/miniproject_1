# PRZYGOTOWANIE SYSTEMU CentOS

Automatyczne przygotowanie czystego systemu (CentOS)
---
- Instalacja wszystkiech rzeczy za pomocą skryptu

```
  chmod 775 prepare_os
  ./prepare_os.sh
```

Manualne przygotowanie czystego systemu (CentOS)
---
- Instalacja GUI w systemie (CentOS)

```
  su -
  yum groupinstall "GNOME Desktop" -y
  systemctl isolate graphical.target #odpala GUI
  systemctl set-default graphical.target #ustawia odpalanie GUI przy uruchomieniu systemu
  systemctl get-default #powinno zwrócić: graphical.target
  logout
```

- Aktualizacja systemu:

```
  su -
  yum update -y
  logout
```

- Instalacja edytora tesktu atom:

```
  wget https://atom-installer.github.com/v1.25.0/atom.x86_64.rpm
  sudo yum install atom.x86_64.rpm -y
  rm -f atom.x86_64.rpm
```

- Instalacja przeglądarki chrome:

```
  sudo yum remove google-chrome google-chrome-unstable
  su -
  cat << EOF > /etc/yum.repos.d/google-chrome.repo
  [google-chrome]
  name=google-chrome
  baseurl=http://dl.google.com/linux/chrome/rpm/stable/x86_64
  enabled=1
  gpgcheck=1
  gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub
  EOF
  logout
  sudo yum install google-chrome-stable -y
```

- Pobranie chromedriver:

```
  wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
  unzip chromedriver_linux64.zip
  rm -f chromedriver_linux64.zip
  sudo mv chromedriver /usr/local/bin/
```

- Instalacja python-pip:

```
  sudo yum install epel-release
  sudo yum update -y
  sudo yum install python-pip -y
```
