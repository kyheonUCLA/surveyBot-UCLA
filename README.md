# Getting Started (Linux/Mac)

Currently, this script will only work with with chrome browser version 96. You can
check the version of chrome by navigating to chrome://settings/help in the browser. Make sure that
the version number is 96.X.XXXX.XX. If the version number for you does not match, you can simply download 
the correct chromedriver from https://chromedriver.chromium.org/downloads and replace it with the chromedriver
under the 'driver' folder.

1) clone the repo to local directory
2) use console command to create venv: python3 -m venv venv
3) activate venv: source venv/bin/activate
4) install Selenium: pip3 install selenium
5) create a json file called keys.json in same directory as main.py
6) In the json file, write: { "username" : "Your-UCLA-Username", : "Your-UCLA-Password"}
5) run the surveyBot with the command: python3 main.py