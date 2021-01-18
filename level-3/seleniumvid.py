# import random
# from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('./chromedriver')

driver.get('https://www.olx.com.ec')

# Primero las interacciones, luego la recoleccion

for i in range(3):
  try:
    # Busco el boton para cargar mas informacion
    boton = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
    )
    # boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    # le doy click
    boton.click()
    # espero que cargue la información dinámica
    WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemPrice"]'))
    )
    # sleep(random.uniform(8.0, 10.0))
    # boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
  except: 
    break

# Todos los anuncios en una lista
anuncios = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for anuncio in anuncios:
  precio = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
  print(precio)

  descripcion = anuncio.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
  print(descripcion)
