#!/bin/bash

# Variables
APP_DIR="/home/youruser/flask-app"
SERVICE_NAME="flaskapp"
VENV_DIR="$APP_DIR/venv"

# Update system
sudo apt update && sudo apt install -y python3 python3-venv python3-pip gunicorn

# Set up virtual environment
if [ ! -d "$VENV_DIR" ]; then
    python3 -m venv $VENV_DIR
fi
source $VENV_DIR/bin/activate

# Install Flask & Gunicorn
pip install --upgrade pip
pip install flask gunicorn

# Create systemd service file
echo "[Unit]
Description=Flask App
After=network.target

[Service]
User=youruser
WorkingDirectory=$APP_DIR
ExecStart=$VENV_DIR/bin/gunicorn -w 4 -b 0.0.0.0:8080 app:app
Restart=always

[Install]
WantedBy=multi-user.target" | sudo tee /etc/systemd/system/$SERVICE_NAME.service

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

echo "Flask app is now running permanently!"
