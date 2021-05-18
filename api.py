import requests
from datetime import datetime,timedelta
from fake_useragent import UserAgent
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound


date = datetime.today() + timedelta(days=1)
date = date.strftime('%d-%m-%Y')
print(date)
pincode = ['451221','451224','451228']
temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

def check_vaccine():
    while True:
        for pin in pincode:
            base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+pin+"&date="+str(date)
            r = requests.get(base_url, headers = browser_header)
            if r.status_code == 200:
                json_data = json.loads(r.content)
                for center in json_data['sessions']:
                    if center['min_age_limit'] == 45:
                        print(pin)
                        return 0

check_vaccine()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://selfregistration.cowin.gov.in/")
playsound("./preview.mp3")
playsound("./preview.mp3")
playsound("./preview.mp3")