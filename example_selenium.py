import time
from selenium import webdriver

# Abrir el explorador (driver) agregando su ubicación en carpeta 
driver = webdriver.Chrome('chromedriver/chromedriver')  
driver.get('http://www.google.com/')
time.sleep(5) 

# Busca el término "ChromeDriver" en el buscador
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) 

# Cierra el explorador
driver.close()