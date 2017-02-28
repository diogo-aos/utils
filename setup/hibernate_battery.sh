#!/bin/bash
# script to create upstart service
# run script as root
# after install, you can now user service hibernate_battery status/start/stop

ROOT_PATH=$(dirname `readlink -f "$0"`)
cd $ROOT_PATH
cd ..

echo "start on filesystem" > /etc/init/hibernate_battery.conf
echo "exec /bin/bash $(pwd)/bin/hibenate_battery.sh" >> /etc/init/hibernate_battery.conf

ln -s /etc/init/hibernate_battery.conf /etc/init.d/hibernate_battery.conf
chmod +x /etc/init.d/hibernate_battery.conf
