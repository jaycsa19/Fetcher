import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep

USERNAME = "email"
PASSWORD = "password"

LOGIN_URL = "login_url"
URL = "base_url"
FILEPATH = "File_Location"

with requests.Session() as s:

    r = s.get(LOGIN_URL)
    soup = BeautifulSoup(r.content, "lxml")

    hidden = soup.find_all("input", {'type':'hidden'})
    target = LOGIN_URL + soup.find("form")['action']
    payload = {x["name"]: x["value"] for x in hidden}

    #add login creds to the dict
    payload["user[email]"] = USERNAME
    payload["user[password]"] = PASSWORD
    print(payload)
    r = s.post(target, data=payload)
    print(r)

    for i in range(587, 608):
        sleep(randint(1,5))
        url1 = URL + str(i)
        result = s.get(url1, headers = dict(referer = url1))
        fn = FILEPATH + str(i) + ".html"
        data = result.text   
        soup = BeautifulSoup(data, "html.parser")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(str(soup))