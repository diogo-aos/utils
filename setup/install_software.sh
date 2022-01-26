sudo snap install slack --classic # professional chat platform
sudo snap install bitwarden # password manager
sudo snap install teams # ms teams
sudo snap install signal-desktop # personal chat platform
sudo snap install mailspring # email client

sudo snap install pycharm-professional --classic  # python IDE

sudo apt install -y flameshot # screenshots
sudo apt install -y i3 # window manager

# install Brave browser
# snap install doesn't allow to make default browser
# sudo snap install brave # browser

sudo apt install -y apt-transport-https curl
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
sudo apt update
sudo apt install -y brave-browser
# ------------------- Brave --------------

# install nordvpn from PPA
# sh <(wget -qO - https://downloads.nordcdn.com/apps/linux/install.sh)
# sudo usermod -aG nordvpn $USER

# install autenticacao.gov

sudo apt install -y gparted # partition management

sudo apt install -y thunar # lightweight file manager

sudo apt install -y audacious # music player
sudo apt install -y audacity # music editor

sudo apt install -y gimp # image editor

sudo apt install -y tmux # terminal manager
