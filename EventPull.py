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

# TeamList = ""
TeamList = []
TeamDistrictDict = {}

with open(os.path.join(myPath + "/APIData/TeamDistrict.csv"), 'w') as csvfile:
    headers = ["teamNum","District"]
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    for i in range(0,15):
        TeamListR = requests.get(BaseURL + "/teams/2018/"+ str(i) +"/keys", auth)
        Teams = TeamListR.json()
        for t in Teams:
            TeamList.append(t)

    for t in TeamList:
        TeamDistrictR = requests.get(BaseURL + "/team/"+ t +"/districts", auth)
        TeamDistrict = TeamDistrictR.json()
        if str(TeamDistrictR.text) != "[]":
            TD = TeamDistrictR.json()[0]["display_name"]
        else:
            TD = "Others"
        tt = t.replace("frc","")
        writer.writerow({"teamNum":tt, "District":TD})
        # print t,TD




# print TeamDistrictDict

# EventsSimpleR = requests.get(BaseURL + "/events/2018/simple", auth)
# EventsSimple = EventsSimpleR.json()
