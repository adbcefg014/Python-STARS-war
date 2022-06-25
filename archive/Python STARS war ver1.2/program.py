import pytesseract, cv2, pyautogui, time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Main Program, refer to README.txt for execution flow
def main():
    # Step 1
    program_setup()

    # Step 2
    seconds2time = seconds_left()
    time.sleep(seconds2time - 50.0)

    # Step 3
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)
    driver.get("https://time.is")
    time.sleep(5)

    sync_diff = driver.find_element(By.ID, "syncH").text
    if 'exact' in sync_diff:
        sync_delay = 0
    else:
        sync_delay = float(sync_diff[14:17])
        if 'behind' in sync_diff:
            sync_delay = -abs(sync_delay)
    print("Sync delay: ", sync_delay)

    # Step 4
    seconds2time = seconds_left()
    time.sleep(seconds2time - 15.0)

    # Step 5
    form_url = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"
    driver.get(form_url)
    driver.maximize_window()

    username_bar = driver.find_element(By.ID, "UID")
    username_bar.send_keys(login_user)
    username_bar.send_keys(Keys.ENTER)
    password_bar = driver.find_element(By.ID, "PW")
    password_bar.send_keys(login_pass)
    password_bar.send_keys(Keys.ENTER)

    # Step 6
    seconds2time = seconds_left()
    time.sleep(seconds2time - 5.0)

    # Step 7
    button_file = 'button1st.png'
    button_search(button_file)

    # Step 8
    seconds2time = seconds_left()
    time.sleep(seconds2time + sync_delay + 0.1)

    # Step 9
    pyautogui.click()

    # Step 10
    time.sleep(0.3) 

    # Step 11
    num = 2                                 
    for x in range(num):
        button_search('button2nd.jpg')
        pyautogui.click()

    # Step 12
    pause()



def program_setup():
    # https://pypi.org/project/pytesseract/
    # Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will 
    #   recognize and “read” the text embedded in images.
    # If you don't have tesseract executable in your PATH (computer environment variables), include the following:
    with open('tesseract_file_path.txt') as f:
        content = f.read()
    tesseract_path = content.strip()
    print("tesseract_file_path: ", tesseract_path)
    pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # chromedriver file directory
    global chromedriver_path
    with open('chromedriver_file_path.txt') as f:
        content = f.read()
    chromedriver_path = content.strip()
    print("chromedriver_file_path: ", chromedriver_path)

    # Birth of the Button Click Target Time
    with open('strike_time.txt') as f:
        content = f.read()
    global strike_time
    import_dt = content
    # Considering date is in dd/mm/yyyy format
    strike_time = datetime.strptime(import_dt, "%d/%m/%Y %H:%M:%S")
    print("strike_time: ", strike_time)

    # Login username and password
    global login_user, login_pass
    with open('username.txt') as f:
        login_user = f.read().strip()
    print(f"Username: {login_user}")
    with open('password.txt') as f:
        login_pass = f.read().strip()
    print(f"Password: {login_pass}")
    

def button_search(button_file):
    # Screenshot, then search for either 'button1st.png' or 'button2nd.png'
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
    delay = diff.total_seconds()
    print("seconds left =", delay)
    print()

    return delay


def pause():
    input("Press the <ENTER> key to continue...")
    return

if __name__ == "__main__":
    main()
