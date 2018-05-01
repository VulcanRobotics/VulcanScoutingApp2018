# -*- coding: utf-8 -*-
#This file pulls the match schedule data from The Blue Alliance API to local directory

#!!EVENT KEYS:
#Hatboro-Horsham: 2018pahat
#Springside Chestnut Hill: 2018paphi
#Seneca: njtab
#FIRST Mid-Atlantic District Championship: mrcmp


import requests
import json
import module_locator
import csv
import os

myPath = module_locator.module_path()

BaseURL = "http://www.thebluealliance.com/api/v3"
auth={"X-TBA-Auth-Key":"dJhYGUW5l6EWDj6ev6h1CcF20VzyFQl6J8dBuVcwnFh8JtJhoP0BeqMnvHcyqM3d"}

EventsR = requests.get(BaseURL + "/events/2018/simple", auth)
Events = EventsR.json()
# print EventsR.text

TeamDistrict = {}
reader = csv.reader(open(os.path.join(myPath + "/APIData/TeamDistrict.csv"), 'r'))
for row in reader:
    k, v = row
    TeamDistrict[k] = v

# print TeamDistrict

EventsDict = {}
for i in range(0,len(Events)):
    eventKey = Events[i]["key"]
    eventName = Events[i]["name"]
    EventsDict[eventKey] = eventName

with open(os.path.join(myPath + "/APIData/Event.csv"), 'w') as csvfile:
    headers = ["teamNum","event","district"]
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for key in EventsDict:
        EventTeamR = requests.get(BaseURL + "/event/"+ key +"/teams/keys", auth)
        # print EventTeamR.text
        EventTeam = EventTeamR.json()
        for t in EventTeam:
            teamNum = t.replace("frc","")
            event = EventsDict[key]
            district = TeamDistrict[teamNum]
            writer.writerow({"teamNum":teamNum,"event":event,"district":district})
            print teamNum, event, district
