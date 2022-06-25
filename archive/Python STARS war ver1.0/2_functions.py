def button_search(buttonFile):
    method = cv2.TM_SQDIFF_NORMED

    pyautogui.screenshot('screenshot.png')

    small_image = cv2.imread(buttonFile)        #button to search for
    large_image = cv2.imread('screenshot.png')  #search area

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    mn,_,mnLoc,_ = cv2.minMaxLoc(result)

    # Draw the rectangle:
    # Extract the coordinates of our best match
    MPx,MPy = mnLoc

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = small_image.shape[:2]

    pyautogui.moveTo(MPx + (tcols/5) , MPy + (trows/5) )
    



def time2strike():
    now = datetime.now()
    print('now: ', now)

    global strike_time

    diff = strike_time - now
    print("difference =", diff)

    delay = diff.total_seconds()
    print("delay seconds =", delay)
    print()

    return delay



#import strike time
f = open('strike_time.txt', 'r')
content = f.read()
f.close()
import_dt = content
# Considering date is in dd/mm/yyyy format
strike_time = datetime.strptime(import_dt, "%d/%m/%Y %H:%M:%S")
print("strike_time: ", strike_time)

#import clock sync delay
f = open('clock_sync_delay.txt', 'r')
content = f.read()
f.close()
sync_delay = float( content.strip() )
print("sync_delay: + ", sync_delay)
