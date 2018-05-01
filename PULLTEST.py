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

divisionsDict = {"Archimedes Division":"2018arc","Carson Division":"2018cars","Curie Division":"2018cur","Daly Division":"2018dal","Darwin Division":"2018dar","Tesla Division":"2018tes"}

for key in divisionsDict:
    eventKey = divisionsDict[key]

    matchScheduleRequest = requests.get(BaseURL + "/event/"+ eventKey +"/alliances", auth)
    matchSchedule = matchScheduleRequest.text
    print matchSchedule

    file = open(myPath + "/Alliances/"+ eventKey +".json","w")
    file.write(matchSchedule)
    file.close()
