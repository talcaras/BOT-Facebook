from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

email = driver.find_element_by_xpath ('//*[@id="email"]')
email.send_keys('seuemail')

senha = driver.find_element_by_xpath ('//*[@id="pass"]')
senha.send_keys('senha')

login = driver.find_element_by_xpath ('//*[@id="u_0_d_7d"]')
login.click()
time.sleep(5)

grupo = driver.find_element_by_xpath ('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/label/input')
grupo.click()
grupo.send_keys('quando a demanda chega')
grupo.send_keys(Keys.ENTER)
time.sleep(5)

acessar = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/a/div[1]/div[1]/span/div')
acessar.click()
time.sleep(5)

driver.get("https://www.facebook.com/atazlandia/photos/a.103582278079969/113544003750463/")
time.sleep(5)

finalera = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div/div/div[1]/div[5]/div/div[2]/div/div/div/div/form/div/div/div[2]/div/div/div/div')
finalera.click()
finalera.send_keys('Boa tarde chefia, alguém manjando de bot pra facebook?')
finalera.send_keys(Keys.ENTER)

