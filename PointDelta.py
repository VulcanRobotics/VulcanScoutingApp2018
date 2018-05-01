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

red = 0
blue = 0

file = open(myPath + "/matchKeys.json","w")

EventsDict = {}
for i in range(0,len(Events)):
    eventKey = Events[i]["key"]
    eventName = Events[i]["name"]
    EventsDict[eventKey] = eventName

a = 1
for key in EventsDict:
    print "Pulling from " + str(EventsDict[key])+ "," + str(len(EventsDict) - a) + " events to go."
    a += 1
    MatchesR = requests.get(BaseURL + "/event/" + key + "/matches/timeseries", auth)
    print MatchesR.text
    if MatchesR.text != []:
        file = open(myPath + "/matchKeys.json","a")
        file.write(MatchesR.text)
        file.close()


#     Matches = MatchesR.json()
#     for i in range(0,len(Matches)):
#         if Matches[i]["comp_level"] == "f" or Matches[i]["comp_level"] == "sf" or Matches[i]["comp_level"] == "qf":
#             if Matches[i]["winning_alliance"] == "red":
#                 red += 1
#             if Matches[i]["winning_alliance"] == "blue":
#                 blue += 1
#
#
#
#
# def small(a,b):
#     if a > b:
#         return b
#     if b > a:
#         return a
#
# def GCD(a, b):
#     lim = small(a,b)
#     for i in range(lim, 0, -1):
#         if a%i == 0 and b%i == 0:
#             return i
#
# def reduce(a,b):
#     a = a
#     b = b
#     number = GCD(a,b)
#     # print number
#     if number == 1:
#         # print a, b
#         result = (a, b)
#         # return a, b
#     else:
#         a = a/number
#         b = b/number
#         reduce(a,b)
#     return a,b
#
#
# print "Red wins "+ str(red)+" matches, blue wins "+ str(blue)+" matches." "Red to blue ratio is " + str(reduce(red, blue)) + "."
# # print reduce(red, blue)
