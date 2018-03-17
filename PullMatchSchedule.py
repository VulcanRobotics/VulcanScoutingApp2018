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

myPath = module_locator.module_path()

BaseURL = "http://www.thebluealliance.com/api/v3"
auth={"X-TBA-Auth-Key":"dJhYGUW5l6EWDj6ev6h1CcF20VzyFQl6J8dBuVcwnFh8JtJhoP0BeqMnvHcyqM3d"}

eventKey = "2018paphi"

matchScheduleRequest = requests.get(BaseURL + "/event/"+ eventKey +"/matches/simple", auth)
matchSchedule = matchScheduleRequest.text

file = open(myPath + "/matchSchedule.json","w")
file.write(matchSchedule)
file.close()
