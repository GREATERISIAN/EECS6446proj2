import logging
from http.client import HTTPConnection

import time
from locust import HttpUser, task, between
from bs4 import BeautifulSoup
import json
import random
import string
import os
HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
name=["a"]
firsttoken=[]
tasks=[1,1,1,1]
g=open('C:\\Users\\natan\\counting\\pseudolocust\\tasks.csv',"w")

    



g.write(str(tasks))
g.close()


class QuickstartUser(HttpUser):
    wait_time = between(1, 12)
    @task(tasks[0])
    def statsserv(self):
        self.client.get("/statistics/current", headers={"Authorization":"Bearer "+self.token}  )
    @task(tasks[1])
    def notesserv(self):
        self.client.get("/notifications/recipients/current", headers={"Authorization":"Bearer "+self.token}  )
    @task(tasks[2])
    def get(self):
        self.client.get("/accounts/current", headers={"Authorization":"Bearer "+self.token}  )
    @task(tasks[3])
    def put(self):
        self.client.put("/accounts/current",  headers={"Authorization":"Bearer "+self.token}, json={"note":"Oh no I was killed by a kangaroo","incomes":[{"income_id":1,"title":"Salary","icon":"doll","currency":"RUB","period":"DAY","amount":"14","converted":"426.833"},{"income_id":2,"title":"Borg","icon":"wallet","currency":"RUB","period":"YEAR","amount":"12","converted":"1.000"}],"expenses":[{"expense_id":1,"title":"Rent","icon":"cart","currency":"USD","period":"MONTH","amount":"12","converted":"0.000"},{"expense_id":2,"title":"Cats","icon":"cart","currency":"RUB","period":"YEAR","amount":"12","converted":"1.000"}],"saving":{"amount":0,"capitalization":False,"deposit":False,"currency":"RUB","interest":0}})
    #@task(3)
    #def rent(self):
    #    self.client.put("/accounts/current", json={"note":None,"incomes":[],"expenses":[{"expense_id":1,"title":"Rent","icon":"cart","currency":"USD","period":"MONTH","amount":"12"}],"saving":{"amount":0,"capitalization":False,"deposit":False,"currency":"USD","interest":0}})
    #    self.client.put("/accounts/current", json={"note":None,"incomes":[{"income_id":1,"title":"Salary","icon":"doll","currency":"RUB","period":"DAY","amount":"14"}],"expenses":[{"expense_id":1,"title":"Rent","icon":"cart","currency":"USD","period":"MONTH","amount":"12","converted":"NaN"}],"saving":{"amount":0,"capitalization":False,"deposit":False,"currency":"USD","interest":0}})    

    #@task(3)
    #def view_items(self):
    #    for item_id in range(10):
    #        self.client.get("/accounts/current")
    #        time.sleep(1)
    #        self.client.put("/accounts/current")

    def on_start(self):
        host="http://192.168.2.11:80"
        length = 8
        username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if(len(name)==1):
            print(len(name))
            username=name[0]+username
        self.username=username
            

        self.client.post("/accounts/", json={"username":username, "password":"brfererre"})
        #headers={"Authorization": "Basic YnJvd3Nlcjo=\r\n"}
        response=self.client.post("/uaa/oauth/token",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Authorization": "Basic YnJvd3Nlcjo="},data="scope=ui&username="+username+"&password=brfererre&grant_type=password")


        soup = BeautifulSoup(response.content, 'html.parser')

        soup.children
        
        step1 = soup.contents
        
        step2=json.loads(step1[0])
        self.token=step2["access_token"]
        if(len(name)==1):
            name.append(username)
            firsttoken.append(self.token)

        self.client.get("/accounts/current", headers={"Authorization":"Bearer "+self.token})
        time.sleep(6)
        #self.client.put("/notifications/recipients/current", json={"email":"maxwell@gmail.com","scheduledNotifications":{"REMIND":{"active":True,"frequency":"MONTHLY"}}})
