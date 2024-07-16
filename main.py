import time

from selenium import webdriver
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

FACEBOOK_EMAIL = os.environ.get("FACEBOOK_EMAIL")
FACEBOOK_PASSWORD = os.environ.get("FACEBOOK_PASSWORD")

# Keep  Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")

time.sleep(5)
login_button = driver.find_element(By.CSS_SELECTOR, value='a.c1p6lbu0 .c9iqosj')
login_button.click()

time.sleep(5)
cookie_button = driver.find_element(By.XPATH, value='//*[@id="t-1686761967"]/div/div[2]/div/div/div[1]/div[1]/button')
cookie_button.click()

time.sleep(5)
login_with_facebook_button = driver.find_element(By.XPATH, value='//*[@id="t-1686761967"]/div/div[1]/div/div[1]/div/'
                                                                 'div/div[2]/div[2]/span/div[2]/button')
login_with_facebook_button.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(5)
facebook_email_field = driver.find_element(by=By.ID, value='email')
facebook_email_field.send_keys(FACEBOOK_EMAIL)
time.sleep(5)
facebook_password_field = driver.find_element(By.XPATH, value='//*[@id="pass"]')
facebook_password_field.click()
time.sleep(2)
facebook_password_field.send_keys(FACEBOOK_PASSWORD)
facebook_password_field.send_keys(Keys.ENTER)
time.sleep(2)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_button = driver.find_element(By.CSS_SELECTOR, value="[data-testid='allow']")
allow_button.click()

time.sleep(2)
dismiss_notification_button = driver.find_element(By.CSS_SELECTOR, value="[data-testid='decline']")
dismiss_notification_button.click()

time.sleep(10)
for n in range(20):
    time.sleep(3)
    try:
        reject_button = driver.find_element(By.XPATH, value='//*[@id="t41619109"]/div/div[1]/div/main/div[2]'
                                                            '/div/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button')
        reject_button.click()
        # time.sleep(3)
        # like_button = driver.find_element(By.XPATH, value=
        #     '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        # like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

# for i in range(10):
#     reject_button.click()


input("Hit enter to close the window")
driver.quit()
