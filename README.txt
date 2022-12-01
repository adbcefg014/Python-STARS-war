Last updated by JohnsonW 2-12-2022 for Windows 10, Chrome browser (Chrome only)

This was created in for use in the NTU STARS. 
For testing purposes, you can change the variable testing from False to True, near the top of the file

Program set-up notes:
0) Is Python in PATH? 
to check: open command prompt & type where python, if yes will see python.exe location, else see 0a onwards
0a) Windows Settings-> Apps -> Python 3.XX -> Modify -> Modify -> Next
0b) Tick Add Python to environment variables -> Install
0c) Restart computer

1a) Control Panel -> Clock and Region -> Date and Time -> Internet Time -> Change Settings
1b) Tick Synchronise with an Internet time server
1c) sg.pool.ntp.org
1d) Click Update now
1e) Click OK

(config folder)
2) Update strike_time.txt to desired button click date/time
3) Update username.txt to Studentlink login username
4) Update password.txt to Studentlink login password

(main folder)
5) Run program.py
6) Enter <ENTER> to end program


Program Execution Walkthrough:
1)    Program starts & initializes with information from .txt files
2)    Wait until 59 seconds left
3)    Go to time.is to get clock-sync offset
4)    Wait until 20 seconds left
5)    Open STARS and login
6)    Wait until 3 seconds left
7)    Find the first button
8)    Wait until strike_time
9)    Click the first button
10)   Wait 0.1 second for page to load, then find & click the second button
11)   Pause program with an input request
12)   Program finishes
