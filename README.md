- 👋 Hi, I’m @inTracKas




Setup Python based WWW server script.


1) Download, install and run Python script WWW server:
cd /home/
wget https://github.com/inTracKas/inTracKas/blob/main/python-server.py


2) Create a new systemd service file:
sudo nano /etc/systemd/system/python-server.service

3) Paste or edit by your Python script location:

[Unit]
Description=Python web server with AWS IPS
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/python-server.py
[Install]
WantedBy=multi-user.target

Save the file.

4) Reload the daemon
sudo systemctl daemon-reload

5) Enable our service so that it doesn’t get disabled if the server restarts.
sudo systemctl enable test.service

6) Start our service
sudo systemctl start test.service


