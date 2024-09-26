import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import manager as mg

INSTA_EMAIL = mg.INSTA_EMAIL
INSTA_PASSWORD = mg.INSTA_PASSWORD
USER_NAME = mg.USER_NAME
SIMILAR_ACCOUNT = "chefsteps"

class InstaFollwer:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        self.driver.get(" https://www.instagram.com/accounts/login/")
        time.sleep(5)
        user_name = self.driver.find_element(By.NAME, value='username')
        user_name.send_keys(USER_NAME)
        time.sleep(4)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(INSTA_PASSWORD, Keys.ENTER)

        time.sleep(10)
        # Click "Not now" and ignore Save-login info prompt
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)
        # Click "not now" on notifications prompt
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        # Show followers of the selected account.
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        time.sleep(3)
        # for i in range(10):
        #     # In this case we're executing some Javascript, that's what the execute_script() method does.
        #     # The method can accept the script as well as an HTML element.
        #     # The modal in this case, becomes the arguments[0] in the script.
        #     # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        #     time.sleep(2)

    def follow(self):
        tap_follow = self.driver.find_elements(By.XPATH, value="// button[contains(text(), 'Follow')]")
        for touch in tap_follow:
            touch.click()
            time.sleep(2)


follow = InstaFollwer()
follow.login()
follow.find_followers()
follow.follow()