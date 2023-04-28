#!/bin/env bash
source ~/.bashrc
sudo rm -rf /var/www/blog/html/
sudo mkdir -p /var/www/blog/html
rm -rf ~/ne
mkdir ~/ne
jekyll build -s ~/baojunwang/ -d ~/ne
sudo cp -r ~/ne/* /var/www/blog/html/
#sudo cp -r ~/ne/* /usr/share/nginx/html/
rm -rf ~/ne
