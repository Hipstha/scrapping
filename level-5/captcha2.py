#************************************
# Author: Hipstha
# Date: 9/1/2021
#************************************

from selenium import webdriver
from time import sleep
import requests
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
  "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver', chrome_options=opts)
driver.get('https://google.com/recaptcha/api2/demo')

try:
  # get the captcha unique ID
  captcha_key = driver.find_element_by_id('recaptcha-demo').get_attribute('data-sitekey')
  # 2captcha request path
  url = "https://2captcha.com/in.php?"
  url += "key=" + "9421ea81859bbfa0d28355adb33eb75a" # API KEY 2CAPTCHA
  url += "&method=userrecaptcha"
  url += "&googlekey=" + captcha_key
  url += "&pageurl=" + url
  url += "&json=0"

  print(url)
  # GET request to 2captcha
  respuesta_requerimiento = requests.get(url)
  captcha_service_key = respuesta_requerimiento.text
  print(captcha_service_key)
  # parsing captcha ID
  captcha_service_key = captcha_service_key.split('|')[-1]

  # 2captcha request path
  url_resp = "https://2captcha.com/res.php?"
  url_resp += "key=" + "9421ea81859bbfa0d28355adb33eb75a" 
  url_resp += "&action=get"
  url_resp += "&id=" + captcha_service_key
  url_resp += "&json=0"
  sleep(5)

  while True: # waiting for solving
    respuesta_solver = requests.get(url_resp)
    respuesta_solver = respuesta_solver.text
    print(respuesta_solver)
    if respuesta_solver == 'CAPCHA_NOT_READY':
      sleep(5)
    else:
      break

  # parsing the captcha ID
  respuesta_solver = respuesta_solver.split('|')[-1]
  insertar_solucion = 'document.getElementById("g-recaptcha-response").innerHTML="' + respuesta_solver + '";'

  driver.execute_script(insertar_solucion)
  # clicking submit button
  submit_button = driver.find_element_by_xpath('//input[@id="recaptcha-demo-submit"]')
  submit_button.click()
except Exception as e:
  print(e)

print()
print('*********************************************')
print('Soy un robot y el captcha me la pela')
print('*********************************************')
print()

# get information protected by a captcha
contenido = driver.find_element_by_class_name('recaptcha-success')
print(contenido.text)