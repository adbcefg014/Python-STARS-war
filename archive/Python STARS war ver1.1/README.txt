Last updated by JohnsonW 13-6-2022 for windows10

Program set-up notes:
0) Is Python is PATH? (to check: open command prompt & type where python, if yes will see python.exe location, if no see 0a & 0b
0a) windows menu -> type environment variables -> Click Environment Variables -> Path -> Edit
0b) Add Python folder to list

1a) Install Tesseract from https://github.com/UB-Mannheim/tesseract/wiki
1b) Update location of tesseract.exe in tesseract_file_path.txt

2a) Control Panel -> Clock and Region -> Date and Time -> Internet Time -> Change Settings
2b) Tick Synchronise with an Internet time server
2c) sg.pool.ntp.org
2d) Update now
2e) Click OK

3a) Go to time.is
3b) Take note of "Your clock is X.X seconds behind/ahead"
3c) Update clock_sync_delay.txt
3ci) 	If clock 0.2 seconds ahead, update .txt to 0.2
3cii)	If clock 0.2 seconds behind, update .txt to -0.2

4) Update strike_time.txt to desired button click date/time

5) Run program.py


Program Execution Walkthrough:
1)    Program starts & initializes with information from .txt files
2)    Wait until 3 seconds left to strike_time to take a screenshot
3)    Take a screenshot, then find & move mouse to first button
4)    Wait until strike_time
5)    Click the button
6)    Wait for 0.3 seconds
7)    Take a screenshot, then find second button and click it; 2 times in case it fails first time