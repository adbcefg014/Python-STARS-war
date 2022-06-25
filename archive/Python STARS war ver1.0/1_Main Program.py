'''==============================initializing=============================='''
import sys, pytesseract, cv2, pyautogui, time
from datetime import datetime

try:
    #execute sub-file
    exec(open('2_functions.py').read())
except FileNotFoundError:   #end main program if any missing sub-files
    print('Error: Missing Files within the Program Directory.')
    print('Ending Program...')
    sys.exit()

#import & execute tesseract.exe
f = open('tesseract_file_path.txt', 'r')
content = f.read()
f.close()
tesseract_path = content.strip()
print("tesseract_file_path: ", tesseract_path)
pytesseract.pytesseract.tesseract_cmd = tesseract_path


#====================wait until 3sec before strike time==================
print('\nprogram start')
delay = time2strike()
time.sleep(delay - 3.0)

#search for button 2sec before strike time
button_search('button2.png')

#==============================first click==============================
print('\nfirst click')
#click dalay after strike time, account for clock cync offsets
delay = time2strike()
time.sleep(delay + sync_delay + 0.1)      #clock synce delay value
pyautogui.click()

#time1 = datetime.now()             #execution time taken      
#print(time1 - strike_time)         #checking takes ~0.3s

#=============================second click=============================
print('\nsecond click')
#wait for page to load, consecutive tries
time.sleep(0.5)                         
num = 2                                 
for x in range(num):
    button_search('button3.jpg')
    pyautogui.click()
    print(x)
print(datetime.now() - time1)


