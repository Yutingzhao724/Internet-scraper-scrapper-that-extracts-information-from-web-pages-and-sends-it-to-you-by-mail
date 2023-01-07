# Internet scrapper that extracts information from web pages and sends it by mail
  In the era of big data, to conduct data analysis, we must first have a data source, and learning crawlers allows us to obtain more data sources, and these data sources can be collected according to our purpose, removing a lot of irrelevant data.When doing big data analysis or data mining, data sources can be obtained from some websites that provide data statistics, or from some literature or internal information, but these ways of obtaining data are sometimes difficult to meet our expectations The demand for data, and manually looking for these data from the Internet, consumes too much energy. At this time, we can use crawler technology to automatically obtain the data content we are interested in from the Internet, and crawl these data content back as our data source, so as to conduct deeper data analysis and obtain more valuable data. Information.

## Setting Task
Use Python to write a program:

Drive the browser to open automatically

Enter "python" to search

Crawl the titles of the search results separately

Store the collected information in a text

Send it by email.


## some preparations
Install the browser driver (take Google as an example)  
https://chromedriver.chromium.org/

Introduce **selenium**, **stmplib** library

```bash
pip install selenium
```

```python
# Reptile related modules
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_contains
```

```python
# Email module
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import ssl
```

_**About selenium**_
_This Python networking library is an open-source browser automation tool (webdriver) that allows you to automate processes such as logging into social media platforms. Selenium is widely used to test cases or test scripts on applications. Its advantage in web scraping stems from its ability to render web pages like any browser by running JavaScript -- a programming language that standard web crawlers cannot run. Currently Selenium is widely used by developers.  
By running JavaScript, Selenium can process any content displayed dynamically, and then use built-in methods or even Beautiful Soup to parse the content of the web page. In addition, it can mimic the user's behavior.  
The only downside to using Selenium in web scraping is that it slows down the process as it has to execute JavaScript code for each page before it can be parsed. Therefore, it is not suitable for large-scale data extraction. However, if you want to extract data on a small scale or don't care about data extraction speed, then Selenium is a good choice._

Obtain the third-party permission information authorization code of the mailbox
https://support.google.com/accounts/answer/1066447?hl=en&co=GENIE.Platform%3DAndroid

## Result
Got a text that collected the search result information and received a mail with the information
