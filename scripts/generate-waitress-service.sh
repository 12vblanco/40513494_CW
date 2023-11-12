#!/usr/bin/bash

cat > webtech.service << END
# /etc/systemd/system/helloapp.service
[Unit]
Description=Advanced Webtech App
After=network.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=/home/$USER/40514394_CW
ExecStart=/home/$USER/40514394_CW/env/bin/waitress-serve --listen=127.0.0.1:8080 app:app
Restart=always

[Install]
WantedBy=multi-user.target
END
