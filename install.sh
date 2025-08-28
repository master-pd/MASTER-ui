#!/data/data/com.termux/files/usr/bin/bash
# Installer for UA TOOL

PREFIX=/data/data/com.termux/files/usr

echo "📦 Installin MASTER Tool..."
pkg install -y python
pip install requests prettytable

cp ua_tool.py $PREFIX/bin/ua-tool
chmod +x $PREFIX/bin/ua-tool
echo "✅ Installation complete! Run with: MASTER-tool "