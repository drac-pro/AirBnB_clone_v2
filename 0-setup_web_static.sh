#!/usr/bin/env bash
# sets up a web servers for the deployment of web_static
# Create the folder /data/web_static/releases/test/ and all subsequent folders if it doesn’t already exist
# Create a fake HTML file /data/web_static/releases/test/index.html

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:group /data/

echo "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	add_header X-Served-By $HOSTNAME;

	server_name _;

	location / {
		try_files \$uri \$uri/ =404;
	}

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		rewrite ^ https://github.com/drac-pro permanent;
	}

	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
}" | sudo tee /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
	sudo service nginx restart
else
	sudo nginx -s reload
fi
