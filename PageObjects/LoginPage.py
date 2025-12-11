from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def enter_email(self, email):
        userEmail=self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        userEmail.clear()
        userEmail.send_keys(email)

    def enter_password(self, password):
        UserPassword=self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        UserPassword.clear()
        UserPassword.send_keys(password)

    def click_login(self):
        logInBtn=self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/section/div/div[2]/div[1]/div/form/div[3]/button')))
        logInBtn.click()


