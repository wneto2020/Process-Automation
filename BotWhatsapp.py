from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException


class BotWhatsapp:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        try:
            self.driver.get('https://web.whatsapp.com/')

        except WebDriverException as error:
            self.driver.close()
            self.driver.quit()
            print({'msg': error})

    def select_contact(self, contact: str):
        try:
            sleep(15)
            path_contact = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
            path_contact.click()
            path_contact.send_keys(contact)
            sleep(2)
            path_contact.send_keys(Keys.ENTER)
            print({'msg': 'contact selected'})

        except WebDriverException as error:
            print({'msg': error})

    def send_message(self, message: str):
        try:
            path_message = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            path_message.click()
            path_message.send_keys(message)
            sleep(2)
            path_message.send_keys(Keys.ENTER)
            print({'msg': 'message send sucessfuly'})

        except WebDriverException as error:
            print({'msg': error})


if __name__ == '__main__':
    bot = BotWhatsapp()
    contato = 'Vítor Lemos'
    mensagem = f'TESTE BOT: Mensagem de teste do BOT'
    bot.select_contact(contato)
    bot.send_message(mensagem)
