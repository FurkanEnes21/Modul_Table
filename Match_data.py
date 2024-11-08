import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options





USERNAME = 'deharmantepe'
PASSWORD = 'Qwerty123!'
CHROMEDRIVER_PATH = 'C:\\Users\\Dell\\Desktop\\0-90\\chromedriver.exe'
DOWNLOAD_DIR = 'C:\\Users\\Dell\\Desktop\\0-90\\Data'





# Chrome options to set the download directory
chrome_options = Options()
prefs = {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://footystats.org/login')

time.sleep(5)

username_box = driver.find_element(By.NAME, 'username')
username_box.send_keys(USERNAME)

password_box = driver.find_element(By.NAME, 'password')
password_box.send_keys(PASSWORD)

password_box.send_keys(Keys.RETURN)

time.sleep(5)

cookies = driver.get_cookies()








# Links to visit and download
links = [
    {
        "visit_link": "https://footystats.org/argentina/primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11212"
    },
    {
        "visit_link": "https://footystats.org/austria/bundesliga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12472"
    },
    {
        "visit_link": "https://footystats.org/austria/2-liga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12478"
    },
    {
        "visit_link": "https://footystats.org/germany/bundesliga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12529"
    },
    {
        "visit_link": "https://footystats.org/germany/2-bundesliga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12528"
    },
    {
        "visit_link": "https://footystats.org/england/championship",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12451"
    },
    {
        "visit_link": "https://footystats.org/spain/la-liga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12316"
    },
    {
        "visit_link": "https://footystats.org/spain/segunda-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12467"
    },
    {
        "visit_link": "https://footystats.org/belgium/pro-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12137"
    },
    {
        "visit_link": "https://footystats.org/england/premier-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12325"
    },
    {
        "visit_link": "https://footystats.org/brazil/serie-a",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11321"
    },
    {
        "visit_link": "https://footystats.org/denmark/superliga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12132"
    },
    {
        "visit_link": "https://footystats.org/norway/eliteserien",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=10976"
    },
    {
        "visit_link": "https://footystats.org/portugal/liga-nos",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12931"
    },
    {
        "visit_link": "https://footystats.org/portugal/ligapro",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12585"
    },
    {
        "visit_link": "https://footystats.org/portugal/campeonato-de-portugal-group-b",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12864"    
    },
    {
        "visit_link": "https://footystats.org/netherlands/eredivisie",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12322"
    },
    {
        "visit_link": "https://footystats.org/scotland/premiership",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12455"
    },
    {
        "visit_link": "https://footystats.org/south-korea/k-league-1",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11102"
    },
    {
        "visit_link": "https://footystats.org/switzerland/super-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12326"
    },
    {
        "visit_link": "https://footystats.org/italy/serie-a",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12530"
    },
    {
        "visit_link": "https://footystats.org/italy/serie-b",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12621"
    },
    {
       "visit_link": "https://footystats.org/italy/serie-c",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=4978"
    },
    {
        "visit_link": "https://footystats.org/japan/j1-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=10994"
    },
    {
        "visit_link": "https://footystats.org/japan/j2-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=10995"
    },
    {
       "visit_link": "https://footystats.org/bulgaria/first-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12149"
    },
    {
       "visit_link": "https://footystats.org/chile/primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11103"
    },
    {
       "visit_link": "https://footystats.org/colombia/categoria-primera-a",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=10997"
    },
    {
       "visit_link": "https://footystats.org/costa-rica/primera-division-fpd",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12324"
    },
    {
       "visit_link": "https://footystats.org/croatia/prva-hnl",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12121"
    },
    {
       "visit_link": "https://footystats.org/czech-republic/first-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12336"
    },
    {
       "visit_link": "https://footystats.org/ecuador/primera-categoria-serie-a",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11157"
    },
    {
       "visit_link": "https://footystats.org/el-salvador/salvadoran-primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12819"
    },
    {
       "visit_link": "https://footystats.org/ethiopia/ethiopia-premier-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13358"
    },
    {
       "visit_link": "https://footystats.org/france/ligue-1",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12337"
    },
    {
       "visit_link": "https://footystats.org/france/ligue-2",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12338"
    },
    {
       "visit_link": "https://footystats.org/greece/super-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12734"
    },
    {
       "visit_link": "https://footystats.org/guatemala/liga-nacional-de-futbol-de-guatemala",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12118"
    },
    {
       "visit_link": "https://footystats.org/honduras/liga-nacional-de-futbol-profesional-de-honduras",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12650"
    },
    {
       "visit_link": "https://footystats.org/hungary/nb-ii",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12590"
    },
    {
       "visit_link": "https://footystats.org/india/indian-super-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13386"
    },
    {
       "visit_link": "https://footystats.org/indonesia/liga-1",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13046"
    },
    {
       "visit_link": "https://footystats.org/mexico/ascenso-mx",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12643"
    },
    {
       "visit_link": "https://footystats.org/morocco/botola-pro",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13286"
    },
    {
       "visit_link": "https://footystats.org/morocco/botola-2",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13642"
    },
    {
       "visit_link": "https://footystats.org/nicaragua/primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12498"
    },
    {
       "visit_link": "https://footystats.org/paraguay/division-profesional",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11141"
    },
    {
       "visit_link": "https://footystats.org/peru/primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11062"
    },
    {
       "visit_link": "https://footystats.org/poland/ekstraklasa",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12120"
    },
    {
       "visit_link": "https://footystats.org/poland/1-liga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12156"
    },
    {
       "visit_link": "https://footystats.org/poland/2-liga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12820"
    },
    {
       "visit_link": "https://footystats.org/poland/2-liga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12820"
    },
    {
       "visit_link": "https://footystats.org/romania/liga-i",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12495"
    },
    {
       "visit_link": "https://footystats.org/russia/fnl",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12540"
    },
    {
       "visit_link": "https://footystats.org/saudi-arabia/first-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12496"
    },
    {
       "visit_link": "https://footystats.org/senegal/senegal-premier-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=13648"
    },
    {
       "visit_link": "https://footystats.org/serbia/superliga",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12138"
    },
    {
       "visit_link": "https://footystats.org/slovenia/2-snl",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12481"
    },
    {
       "visit_link": "https://footystats.org/thailand/thai-league-t1",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12475"
    },
    {
       "visit_link": "https://footystats.org/ukraine/ukrainian-premier-league",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=12483"
    },
    {
       "visit_link": "https://footystats.org/uruguay/primera-division",
        "download_link": "https://footystats.org/c-dl.php?type=matches&comp=11209"
    }
]




for link in links:
    driver.get(link["visit_link"])

    for cookie in cookies:
        driver.add_cookie(cookie)
    
    time.sleep(5)

    driver.get(link["download_link"])
    
    time.sleep(10)

driver.quit()
