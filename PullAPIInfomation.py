while True:

    # -*- coding: utf-8 -*-
    #This file pulls API data from The Blue Alliance API to local directory

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

    eventKey = "2018mrcmp"

    TeamStatusesR = requests.get(BaseURL + "/event/"+ eventKey +"/teams/statuses", auth)
    TeamStatuses = TeamStatusesR.json()
    # print TeamStatusesR.text

    MatchesR = requests.get(BaseURL + "/event/"+ eventKey +"/matches", auth)
    Matches = MatchesR.json()
    # print MatchesR.text

    TeamsSimpleR = requests.get(BaseURL + "/event/"+ eventKey +"/teams/simple", auth)
    TeamsSimple = TeamsSimpleR.json()

    matchSchedule = json.load(open(myPath + "/matchSchedule.json","r"))

    def safe_div(x,y):
        if y == 0:
            return 0
        return x / y

    with open(os.path.join(myPath + "/APIData/TeamStatuses.csv"), 'w') as csvfile:
        headers = ['teamNum', 'matchesPlayed', 'rank', 'win', 'lose', 'tie']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key in TeamStatuses:
            # print key
            if key != "frc6667":
                teamNum = key.replace("frc","")
                matchesPlayed = TeamStatuses[key]["qual"]["ranking"]["matches_played"]
                rank = TeamStatuses[key]["qual"]["ranking"]["rank"]
                win = TeamStatuses[key]["qual"]["ranking"]["record"]["wins"]
                lose = TeamStatuses[key]["qual"]["ranking"]["record"]["losses"]
                tie = TeamStatuses[key]["qual"]["ranking"]["record"]["ties"]
                writer.writerow({'teamNum':teamNum, 'matchesPlayed':matchesPlayed, 'rank':rank, 'win':win, 'lose':lose, 'tie':tie})

    with open(os.path.join(myPath + "/APIData/MatchTeams.csv"), 'w') as csvfile:
        headers = ['teamNum','color','matchNum', 'arrangement']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for i in range(0, len(Matches)):
            if Matches[i]["comp_level"] == "qm" and Matches[i]["winning_alliance"] != "":
                # print Matches[i]["actual_time"]
                matchNum = Matches[i]["match_number"]
                redTeams = Matches[i]["alliances"]["red"]["team_keys"]
                blueTeams = Matches[i]["alliances"]["blue"]["team_keys"]
                # r = 1
                # b = 1
                # for t in redTeams:
                #     exec("red"+str(r) + '=' + t.replace("frc",""))
                #     r += 1
                # for t in blueTeams:
                #     exec("blue"+str(b) + '=' + t.replace("frc",""))
                #     b += 1
                arrangement = Matches[i]["score_breakdown"]["blue"]["tba_gameData"]
                for t in redTeams:
                    teamNum = t.replace("frc","")
                    color = "Red"
                    writer.writerow({'teamNum':teamNum,'color':color,'matchNum':matchNum, 'arrangement':arrangement})
                for t in blueTeams:
                    teamNum = t.replace("frc","")
                    color = "Blue"
                    writer.writerow({'teamNum':teamNum,'color':color,'matchNum':matchNum, 'arrangement':arrangement})

    with open(os.path.join(myPath + "/APIData/TeamNames.csv"), 'w') as csvfile:
        headers = ["teamNum", "teamName"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for i in range(0,len(TeamsSimple)):
            teamNum = TeamsSimple[i]["key"].replace("frc","")
            teamName = TeamsSimple[i]["nickname"]
            writer.writerow({"teamNum":teamNum, "teamName":teamName})

    with open(os.path.join(myPath + "/APIData/Playoff.csv"), 'w') as csvfile:
        headers = ["teamNum", "matchNum","color"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for i in range(0, len(matchSchedule)):
            if matchSchedule[i]["comp_level"] == "f" and matchSchedule[i]["match_number"] == 1:
                redTeam = matchSchedule[i]["alliances"]["red"]["team_keys"]
                blueTeam = matchSchedule[i]["alliances"]["blue"]["team_keys"]
                matchNum = matchSchedule[i]["set_number"]
                for t in redTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"Final" + str(matchNum),"color":"Red"})
                for t in blueTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"Final" + str(matchNum),"color":"Blue"})
            if matchSchedule[i]["comp_level"] == "sf" and matchSchedule[i]["match_number"] == 1:
                redTeam = matchSchedule[i]["alliances"]["red"]["team_keys"]
                blueTeam = matchSchedule[i]["alliances"]["blue"]["team_keys"]
                matchNum = matchSchedule[i]["set_number"]
                for t in redTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"SemiFinal" + str(matchNum),"color":"Red"})
                for t in blueTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"SemiFinal" + str(matchNum),"color":"Blue"})
            if matchSchedule[i]["comp_level"] == "qf" and matchSchedule[i]["match_number"] == 1:
                redTeam = matchSchedule[i]["alliances"]["red"]["team_keys"]
                blueTeam = matchSchedule[i]["alliances"]["blue"]["team_keys"]
                matchNum = matchSchedule[i]["set_number"]
                for t in redTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"QuarterFinal" + str(matchNum),"color":"Red"})
                for t in blueTeam:
                    t = t.replace("frc", "")
                    writer.writerow({"teamNum":t, "matchNum":"QuarterFinal" + str(matchNum),"color":"Blue"})

    with open(os.path.join(myPath + "/APIData/color.csv"), 'w') as csvfile:
        headers = ["teamNum", "matchNum","color"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for i in range(0,len(matchSchedule)):
            if matchSchedule[i]["comp_level"] == "qm":
                matchNum = Matches[i]["match_number"]
                redTeams = Matches[i]["alliances"]["red"]["team_keys"]
                blueTeams = Matches[i]["alliances"]["blue"]["team_keys"]
                for t in redTeams:
                    t = t.replace("frc","")
                    writer.writerow({"teamNum":t, "matchNum":str(matchNum),"color":"Red"})
                for t in blueTeams:
                    t = t.replace("frc","")
                    writer.writerow({"teamNum":t, "matchNum":str(matchNum),"color":"Blue"})

    with open(os.path.join(myPath + "/APIData/Ownership.csv"), 'w') as csvfile:
        headers = ["teamNum","autonScaleSec","autonSwitchSec","teleScaleSec","teleSwitchSec"]
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        matchesPlayedDict = {}
        autonScaleDict = {}
        autonSwitchDict = {}
        teleScaleDict = {}
        teleSwitchDict = {}

        for i in range(0,len(TeamsSimple)):
            teamNum = TeamsSimple[i]["key"].replace("frc","")
            teamName = TeamsSimple[i]["nickname"]
            matchesPlayedDict[teamNum] = 0
            autonScaleDict[teamNum] = 0
            autonSwitchDict[teamNum] = 0
            teleScaleDict[teamNum] = 0
            teleSwitchDict[teamNum] = 0

        for i in range(0, len(Matches)):
            if Matches[i]["comp_level"] == "qm" and Matches[i]["winning_alliance"] != "":
                redTeams = Matches[i]["alliances"]["red"]["team_keys"]
                blueTeams = Matches[i]["alliances"]["blue"]["team_keys"]
                for t in redTeams:
                    teamNum = t.replace("frc","")
                    autonScale = Matches[i]["score_breakdown"]["red"]["autoScaleOwnershipSec"]
                    autonSwitch = Matches[i]["score_breakdown"]["red"]["autoSwitchOwnershipSec"]
                    teleScale = Matches[i]["score_breakdown"]["red"]["teleopScaleOwnershipSec"] - Matches[i]["score_breakdown"]["red"]["teleopScaleForceSec"]
                    teleSwitch = Matches[i]["score_breakdown"]["red"]["teleopSwitchOwnershipSec"] - Matches[i]["score_breakdown"]["red"]["teleopSwitchForceSec"]

                    autonScaleDict[teamNum] += autonScale
                    autonSwitchDict[teamNum] += autonSwitch
                    teleScaleDict[teamNum] += teleScale
                    teleSwitchDict[teamNum] += teleSwitch
                for t in blueTeams:
                    teamNum = t.replace("frc","")
                    autonScale = Matches[i]["score_breakdown"]["blue"]["autoScaleOwnershipSec"]
                    autonSwitch = Matches[i]["score_breakdown"]["blue"]["autoSwitchOwnershipSec"]
                    teleScale = Matches[i]["score_breakdown"]["blue"]["teleopScaleOwnershipSec"] - Matches[i]["score_breakdown"]["blue"]["teleopScaleForceSec"]
                    teleSwitch = Matches[i]["score_breakdown"]["blue"]["teleopSwitchOwnershipSec"] - Matches[i]["score_breakdown"]["blue"]["teleopSwitchForceSec"]

                    autonScaleDict[teamNum] += autonScale
                    autonSwitchDict[teamNum] += autonSwitch
                    teleScaleDict[teamNum] += teleScale
                    teleSwitchDict[teamNum] += teleSwitch

        for key in TeamStatuses:
            # print key
            if key != "frc6667":
                teamNum = key.replace("frc","")
                # print teamNum
                matchesPlayed = TeamStatuses[key]["qual"]["ranking"]["matches_played"]
                matchesPlayedDict[teamNum] = matchesPlayed

        for i in range(0,len(TeamsSimple)):
            teamNum = TeamsSimple[i]["key"].replace("frc","")
            writer.writerow({"teamNum":teamNum, "autonScaleSec":safe_div(float(autonScaleDict[teamNum]),float(matchesPlayedDict[teamNum])), "autonSwitchSec":safe_div(float(autonSwitchDict[teamNum]),float(matchesPlayedDict[teamNum])), "teleScaleSec":safe_div(float(teleScaleDict[teamNum]),float(matchesPlayedDict[teamNum])),"teleSwitchSec":safe_div(float(teleSwitchDict[teamNum]),float(matchesPlayedDict[teamNum]))})

        # print matchesPlayedDict

time.sleep(300)
