import time, os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Main Program, refer to README.txt for execution flow
# for testing comment out "time.sleep" in steps 2, 4, 6, 8
def main():
    # Step 1
    program_setup()
    s = Service(chromedriver_path)
    driver = webdriver.Chrome(service=s)

    # Step 2
    seconds2time = seconds_left()
    time.sleep(seconds2time - 59.0)

    # Step 3
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
    time.sleep(seconds2time - 20.0)

    # Step 5
    form_url = "https://wish.wis.ntu.edu.sg/pls/webexe/ldap_login.login?w_url=https://wish.wis.ntu.edu.sg/pls/webexe/aus_stars_planner.main"
    driver.get(form_url)
    driver.maximize_window()

    time.sleep(2)
    username_bar = driver.find_element(By.ID, "UID")
    username_bar.send_keys(login_user)
    username_bar.send_keys(Keys.ENTER)
    time.sleep(1)
    password_bar = driver.find_element(By.ID, "PW")
    password_bar.send_keys(login_pass)
    password_bar.send_keys(Keys.ENTER)

    # Step 6
    seconds2time = seconds_left()
    time.sleep(seconds2time - 3.0)

    # Step 7
    submit_button1 = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Add (Register) Selected Course(s)']")

    # Step 8
    seconds2time = seconds_left()
    time.sleep(seconds2time + sync_delay + 0.1)

    # Step 9
    submit_button1.click()

    # Step 10
    time.sleep(0.1)
    submit_button2 = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Confirm to add course(s)']")
    submit_button2.click()

    # Step 11
    pause()


def program_setup():
    # chromedriver file directory
    global chromedriver_path
    path = os.getcwd()
    chromedriver_path = path  + "\\config\\chromedriver.exe"

    # Birth of the Button Click Target Time
    with open('config/strike_time.txt') as f:
        content = f.read()
    global strike_time
    import_dt = content
    # Considering date is in dd/mm/yyyy format
    strike_time = datetime.strptime(import_dt, "%d/%m/%Y %H:%M:%S")
    print("strike_time: ", strike_time)

    # Login username and password
    global login_user, login_pass
    with open('config/username.txt') as f:
        login_user = f.read().strip()
    print(f"Username: {login_user}")
    with open('config/password.txt') as f:
        login_pass = f.read().strip()
    print(f"Password: {login_pass}")

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
