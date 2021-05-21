# Soc-Board

## Socket Shared Clipboard

Using this program, you will be able to share clipboard between two devices in the same network (for devices that are on different networks, you can still make this work using ngrok or use cloud)

This program uses [pyperclip](https://pypi.org/project/pyperclip/) to monitor clipboard activity on a system and sends/receives the clipboard data to/from a remote computer which is also running the program. Since *pyperclip* is cross-platform friendly, this program should also work on Windows, Mac and Linux. 

## Installation
You need Python 3.x to run this script.

Download the code

    git clone https://github.com/imrahulkant/Soc-Board.git
    cd Soc-Board


Install the requirements

    pip install pyperclip
    pip install rich

## Usage
Run this on Server OS

    py serverclipboard.py

Run this on Client OS

    py clientclipboard.py


**Note: This script must run on both the computers that are sharing the clipboard.** 
