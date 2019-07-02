#!/bin/bash

NC='\033[0m'
BG='\033[1;32m'
FR='\033[1;31m'
WH='\033[1;37m'

if command -v python3 &>/dev/null; then
  echo -e "${BG}[*]${NC} Installing python-dependencies."
  pip install -r requirements.txt --user -U
else
  echo -e "${FR}[x] Python3 is not installed...${NC}"
  exit 0
fi

if [[ "$OSTYPE" == *"darwin"* ]]; then
  command -v brew >/dev/null 2>&1 || {
    echo -e "${WH}[+] Installing brew...${NC}"
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  }
  brew update
  echo -e "${BG}[+]${NC} Installing geckodriver..."
  brew install jq
  brew install geckodriver
  echo -e "${BG}[+]${NC} Installing PhantomJS..."
  brew tap caskroom/cask
  brew cask install phantomjs
  echo -e "${BG}[+] The installation completed successfully!${NC}"
  exit 0
elif [[ "$OSTYPE" == *"linux-gnu"* ]]; then
  sudo apt-get update
  echo -e "${BG}[+]${NC} Installing PhantomJS..."
  sudo apt-get install build-essential chrpath libssl-dev libxft-dev
  sudo apt-get install libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev
  wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
  tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
  sudo ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
  echo -e "${BG}[+]${NC} Installing geckodriver..."
  sudo apt-get install jq
  # taken from here: https://gist.github.com/cgoldberg/4097efbfeb40adf698a7d05e75e0ff51
  json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
  url=$(echo "$json" | jq -r '.assets[].browser_download_url | select(contains("linux64"))')
  curl -s -L "$url" | tar -xz
  chmod +x geckodriver
  sudo mv geckodriver /usr/local/bin
  echo -e "${BG}[+] The installation completed successfully!${NC}"
  exit 0
else
  echo -e "${FR}[x] Unknown operating system!${NC}"
  exit 1
fi