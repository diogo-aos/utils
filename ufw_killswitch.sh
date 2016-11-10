ufw default deny outgoing
ufw default deny incoming
ufw allow out on tun0 from any to any
ufw allow in on tun0 from any to any

# ufw allow out from 172.21.1.252/16
# ufw allow in from 172.21.1.252/16

ufw enable