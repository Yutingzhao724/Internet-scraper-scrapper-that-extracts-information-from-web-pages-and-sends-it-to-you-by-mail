# import time
# import csv
# Reptile related modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains

# Email module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl

# Open Browser
driver = Chrome()
# Open the Google search home page
driver.get("https://www.google.com")

input_tag = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_tag.send_keys("python")
input_tag.send_keys(Keys.ENTER)

WebDriverWait(driver, 10).until(title_contains("python"))

# while True:
h3_list = driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb')
for h3 in h3_list:
    print(h3.text)

# driver.find_element(By.XPATH, '//*[@id="pnnext"]/span[2]').click()
# time.sleep(3)

with open('Result.txt', 'w', encoding='utf-8') as f:
    f.write('The result of searching python: \n')
    for h3 in h3_list:
        info = str(h3.text)+'\n'
        f.write(info)

from_addr = 'yutingzhao724@gmail.com'
from_password = '16-digit authorization code'
to_addr = 'yutingzhao724@gmail.com'
smtp_mail = 'smtp.gmail.com'

msg = MIMEMultipart()
att = MIMEText(open('D:\pythonProject\Result.txt', encoding="utf-8").read())
att['Content-Disposition'] = 'attachment; filename= "python_test“'
msg.attach(att)

msg['From'] = Header('yutingzhao724@gmail.com')
msg['To'] = Header('yutingzhao724@gmail.com')
msg['Subject'] = Header('Python test')

# mail = smtplib.SMTP()
# mail.connect(smtp_mail, 587)

mail = smtplib.SMTP_SSL("smtp.gmail.com", 465)

mail.login(from_addr, from_password)
mail.sendmail(from_addr, to_addr, msg.as_string())

mail.quit()