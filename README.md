# UA TOOL (Random User-Agent Requester)

A Termux tool that sends HTTP requests with random User-Agent headers.  
Includes a demo web page (`web/`) for local testing.

## Installation
```bash
apt update && apt upgrade -y
pkg install git -y
pkg install python -y

git clone https://github.com/master-pd/MASTER-ui.git
cd MASTER-ui
bash install.sh

ua-tool
