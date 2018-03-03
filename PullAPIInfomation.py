while True:
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

    eventKey = "2018week0"

    TeamStatusesR = requests.get(BaseURL + "/event/"+ eventKey +"/teams/statuses", auth)
    TeamStatuses = TeamStatusesR.json()

    MatchesR = requests.get(BaseURL + "/event/"+ eventKey +"/matches", auth)
    Matches = MatchesR.json()

    TeamsSimpleR = requests.get(BaseURL + "/event/"+ eventKey +"/teams/simple", auth)
    TeamsSimple = TeamsSimpleR.json()



    with open(os.path.join(myPath + "/APIData/TeamStatuses.csv"), 'w') as csvfile:
        headers = ['teamNum', 'matchesPlayed', 'rank', 'win', 'lose', 'tie']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for key in TeamStatuses:
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
            if Matches[i]["comp_level"] == "qm":
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



    # print TeamStatuses, Matches, TeamsSimple

    # file = open(myPath + "/data.json","w")
    # file.write(TeamStatuses)
    # file.write(Matches)
    # file.write(TeamsSimple)
    # file.close()
time.sleep(300)
