from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()

driver.get("https://restro-admin.vercel.app/#/menu/add/Upk6JR3mX3TxswCB5beJ")
driver.find_element(By.CSS_SELECTOR,"#container > div.form-container.sign-in > form > select > option:nth-child(1)").click()#select domain
driver.find_element(By.CSS_SELECTOR,"#container > div.form-container.sign-in > form > input[type=email]").send_keys("abc@gmail.com")#enter email id
driver.find_element(By.CSS_SELECTOR,"#container > div.form-container.sign-in > form > div.input_fields > input[type=password]").send_keys("84908490")#enter password
driver.find_element(By.CSS_SELECTOR,"#container > div.form-container.sign-in > form > button").click() #sign in

  
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.SideNav > ul > a:nth-child(2) > li > div").click()
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.breadcrumbs > div > a > button").click()
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input[type=text]").send_keys("Taj Ahemdabad")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > input[type=text]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input[type=text]").send_keys("Zoya Shaikh")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input[type=text]").send_keys("Manager")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > input[type=text]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > input[type=text]").send_keys("8154934933")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > input[type=password]").send_keys("84908490")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > input[type=password]").send_keys("84908490")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(5) > div > textarea").send_keys("Sindhu bhavan road 350005")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(6) > div > select > option:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.head > div > div > button.btn_solid")


#SETTINGS MODULE
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/ul/a[4]/li/div').click()  #click settings
#file_input=driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label.img_input_label")  #find image upload element
#image_path=r"C:\\Users\\LENOVO\\Pictures\\Screenshots\\download.png" #image path
#file_input.send_keys(image_path)
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(5) > div:nth-child(2) > input[type=password]").send_keys("8490849")  #for add password
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.page_bottom > div > button.btn_solid").click()


#FOR TAXMETHOD
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[1]/ul/a[3]/li/div').click()  #click taxmethod
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[2]/div[1]/div/a/button').click()
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(1) > div.input_text > input[type=text]").send_keys("GST")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > select > option:nth-child(4)").click()
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input[type=text]").send_keys("IGST")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.forms_one_column > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > input[type=number]").send_keys("5")
driver.find_element(By.CSS_SELECTOR,"#root > div > div.bottomContainer > div.main_container > div.page_details > div.head > div > div > button.btn_solid").click()

#FOR LOGOUT
driver.find_element(By.CSS_SELECTOR,"#root > div > div.Header > div.Header_actions > div.menu > button").click()
driver.find_element(By.XPATH,'//*[@id="account-menu"]/div[3]/ul/li[3]/h6').click()
time.sleep(1x0)



