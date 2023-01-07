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

# Open Browser & Google search home page
driver = Chrome()
driver.get("https://www.google.com")

# Navigate to the search bar, enter "python", and control the keyboard to press the Enter key
input_tag = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_tag.send_keys("python")
input_tag.send_keys(Keys.ENTER)
# Drive the browser to wait ten seconds until a title containing "python" appears
WebDriverWait(driver, 10).until(title_contains("python"))

# Traversing and inputting each information tagged with h3.LC20lb (that is, the title of the search result) into a text
h3_list = driver.find_elements(By.CSS_SELECTOR, 'h3.LC20lb')
for h3 in h3_list:
    print(h3.text)

with open('Result.txt', 'w', encoding='utf-8') as f:
    f.write('The result of searching python: \n')
    for h3 in h3_list:
        info = str(h3.text)+'\n'
        f.write(info)

# Send email
from_addr = 'Sender's email address'
from_password = '16-digit authorization code'
to_addr = 'Recipient's email address'
smtp_mail = 'smtp.gmail.com'

msg = MIMEMultipart()
att = MIMEText(open('D:\pythonProject\Result.txt', encoding="utf-8").read())
att['Content-Disposition'] = 'attachment; filename= "python_test“'
msg.attach(att)

msg['From'] = Header('Sender's email address')
msg['To'] = Header('Recipient's email address')
msg['Subject'] = Header('Python test')

mail = smtplib.SMTP_SSL("smtp.gmail.com", 465)

mail.login(from_addr, from_password)
mail.sendmail(from_addr, to_addr, msg.as_string())

mail.quit()
