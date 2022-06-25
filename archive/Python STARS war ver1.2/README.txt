Last updated by JohnsonW 15-6-2022 for windows10

Program set-up notes:
0) Is Python is PATH? 
to check: open command prompt & type where python, if yes will see python.exe location, else see 0a & 0b
0a) windows menu -> type environment variables -> Click Environment Variables -> Path -> Edit
0b) Add Python folder to list

1a) Install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
1b) Update location of tesseract.exe in tesseract_file_path.txt

2) Update location of chromedriver.exe (in the same folder) in chromedriver_file_path.txt

3a) Control Panel -> Clock and Region -> Date and Time -> Internet Time -> Change Settings
3b) Tick Synchronise with an Internet time server
3c) sg.pool.ntp.org
3d) Click Update now
3e) Click OK

4) Update strike_time.txt to desired button click date/time
5) Update username.txt to Studentlink login username
6) Update password.txt to Studentlink login password

7) Run program.py

>>> Ideally the screen should be set to potrait view (not landscape), to prevent the buttons being hidden from a "scroll down"
>>> If theres an error related to chromedriver, download the version corresponding to error message;
https://chromedriver.chromium.org/


Program Execution Walkthrough:
1)    Program starts & initializes with information from .txt files
2)    Wait until 50 seconds left
3)    Go to time.is to get clock-sync offset
4)    Wait until 15 seconds left
5)    Open STARS and login
6)    Wait until 3 seconds left to strike_time to take a screenshot
7)    Take a screenshot, then find & move mouse to first button
8)    Wait until strike_time
9)    Click the button
10)   Wait for 0.3 seconds
11)   Take a screenshot, then find second button and click it; 2 times in case it fails first time
12)   Pause program with an input request
13)   Program finishes