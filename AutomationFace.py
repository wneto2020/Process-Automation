from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class AutomationFace:

    def __init__(self):
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.get('https://web.facebook.com/?_rdc=1&_rdr')

        except WebDriverException as error:
            self.driver.close()
            self.driver.quit()
            print({'msg': error})

    def user_email(self, email: str):
        path_email = self.driver.find_element_by_xpath('//*[@id="email"]')
        path_email.click()
        path_email.send_keys(email)

    try:
        def user_password(self, pwd: str):
            path_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')
            path_pass.click()
            path_pass.send_keys(pwd)
            path_pass.send_keys(Keys.ENTER)

    except WebDriverException as error:
        print({'msg': error})


if __name__ == '__main__':
    Automation = AutomationFace()
    Automation.user_email('Seu e-mail/Your e-mail')
    Automation.user_password('Sua senha/Your password')



