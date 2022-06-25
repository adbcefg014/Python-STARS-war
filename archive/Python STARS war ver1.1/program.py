import sys, pytesseract, cv2, pyautogui, time
from datetime import datetime

# Program Execution Walkthrough:
# 1)    Program starts & initializes with information from .txt files
# 2)    Wait until 3 seconds left to TIME to take a screenshot
# 3)    Find & move mouse to first button
# 4)    Wait until target time reached
# 5)    Click the button
# 6)    Wait for 0.3 seconds
# 7)    Screenshot and find second button and click it; 2 times in case it fails first time

# Main Program
def Main():
    # Step 1
    program_setup()

    # Step 2
    seconds2time = seconds_left()
    time.sleep(seconds2time - 3.0)

    # Step 3
    button_file = 'button1st.png'
    button_search(button_file)

    # Step 4
    seconds2time = seconds_left()
    time.sleep(seconds2time + sync_delay + 0.1)

    # Step 5
    pyautogui.click()

    # Step 6
    time.sleep(0.3) 

    # Step 7
    num = 2                                 
    for x in range(num):
        button_search('button2nd.jpg')
        pyautogui.click()



def program_setup():
    # https://pypi.org/project/pytesseract/
    # Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will 
    #   recognize and “read” the text embedded in images.
    # If you don't have tesseract executable in your PATH (computer environment variables), include the following:
    f = open('tesseract_file_path.txt', 'r')
    content = f.read()
    f.close()
    tesseract_path = content.strip()
    print("tesseract_file_path: ", tesseract_path)
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Birth of the Button Click Target Time
    global strike_time
    f = open('strike_time.txt', 'r')
    content = f.read()
    f.close()
    import_dt = content
    # Considering date is in dd/mm/yyyy format
    strike_time = datetime.strptime(import_dt, "%d/%m/%Y %H:%M:%S")
    print("strike_time: ", strike_time)

    # Accounting for the synchronization between computer time & time.is website
    f = open('clock_sync_delay.txt', 'r')
    content = f.read()
    f.close()
    global sync_delay
    sync_delay = float( content.strip() )
    print("sync_delay: + ", sync_delay)


# Screenshot, then search for either 'button1st.png' or 'button2nd.png'
def button_search(button_file):
    method = cv2.TM_SQDIFF_NORMED

    pyautogui.screenshot('screenshot.png')

    small_image = cv2.imread(button_file)
    large_image = cv2.imread('screenshot.png')

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    pyautogui.moveTo(MPx + (tcols/5) , MPy + (trows/5) )


def seconds_left():
    now = datetime.now()
    print('now: ', now)

    global strike_time

    diff = strike_time - now
    print("difference =", diff)

    delay = diff.total_seconds()
    print("delay seconds =", delay)
    print()

    return delay


Main()