#! /bin/bash

sudo pip install -U pip
sudo pip install -U -r test_requirements.txt
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -f chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
