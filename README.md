- 👋 Hi, I’m @inTracKas




Setup Python based WWW server script.


1) Download, install and run Python script WWW server: <br>
cd /home/  <br>
wget https://github.com/inTracKas/inTracKas/blob/main/python-server.py   <br>
<br>

2) Create a new systemd service file: <br>
sudo nano /etc/systemd/system/python-server.service  <br>

3) Paste or edit by your Python script location: <br>

[Unit] <br>
Description=Python web server with AWS IPS <br>
After=multi-user.target <br>
[Service] <br>
Type=simple <br>
Restart=always <br>
ExecStart=/usr/bin/python3 /home/python-server.py <br>
[Install] <br>
WantedBy=multi-user.target <br>
<br>
<br>
Save the file.

4) Reload the daemon:


sudo systemctl daemon-reload

5) Enable our service so that it doesn’t get disabled if the server restarts.


sudo systemctl enable test.service

6) Start our service


sudo systemctl start test.service


