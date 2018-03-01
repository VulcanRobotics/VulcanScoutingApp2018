# -*- coding: utf-8 -*-
#This is the UI page for scout input
import wx
import csv
import os
import module_locator
import json
import requests
from datetime import datetime
from pathlib2 import Path


#locate the Package
myPath = module_locator.module_path()

#import match schedule from json generated by PullMatchSchedule.py
matchSchedule = json.load(open(myPath + "/matchSchedule.json","r"))
# print matchSchedule[0]["alliances"]["red"]["team_keys"]

leftColor = "Red"
rightColor = "Blue"

class Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.boldFont = wx.Font(18, wx.DEFAULT, wx.BOLD, wx.NORMAL)
        #Identifiers
        self.nameTitle = wx.StaticText(self, label="Name", pos=(20, 30))
        self.matchNumTitle = wx.StaticText(self, label="Match #", pos=(20, 50))
        self.teamNumTitle = wx.StaticText(self, label="Team #", pos=(230, 50))
        self.nameInput = wx.TextCtrl(self, pos=(120, 30), size = (100, 20))
        self.matchNumInput = wx.TextCtrl(self, pos=(120, 50), size = (100, 20))
        self.teamNumInput = wx.ComboBox(self, pos=(290, 50), size = (100, 25), style=wx.CB_READONLY)
        self.label = wx.StaticText(self, label="Dead robot / no show?", pos=(230,30))
        self.deadRobot = wx.CheckBox(self, pos=(380, 30))

        #Autons
        self.autonTitle = wx.StaticText(self, label="Auton", pos=(20, 100))
        self.autonTitle.SetFont(self.boldFont)

        self.baselineTitle = wx.StaticText(self, label="Baseline", pos=(20, 120))
        self.baselineInput = wx.CheckBox(self, pos=(100,120))

        self.autonSwitchTitle = wx.StaticText(self, label="SWITCH Cubes", pos=(20, 140))
        self.autonSwitchInput = wx.TextCtrl(self, pos=(220, 140), size=(30,20))
        self.autonSwitchInput.AppendText("0")
        self.autonSwitchInputUp = wx.Button(self, label="+", pos=(270, 137.5), size=(25,25), name="autonSwitchInputUp")
        self.autonSwitchInputDown = wx.Button(self, label="-", pos=(300, 137.5), size=(25,25), name="autonSwitchInputDown")
        self.autonSwitchColor = wx.RadioBox(self, pos=(680, 130), choices=["Yes", "No", "9"])
        self.label = wx.StaticText(self, label="CORRECT COLORED SIDE of the SWITCH?", pos=(410,140))
        self.autonSwitchColor.ShowItem(2, False)
        self.autonSwitchColor.SetSelection(2)
        self.autonSwitchColor.Enable(False)


        self.autonScaleTitle = wx.StaticText(self, label="SCALE Cubes", pos=(20, 160))
        self.autonScaleInput = wx.TextCtrl(self, pos=(220, 160), size=(30,20))
        self.autonScaleInput.AppendText("0")
        self.autonScaleInputUp = wx.Button(self, label="+", pos=(270, 157.5), size=(25,25), name="autonScaleInputUp")
        self.autonScaleInputDown = wx.Button(self, label="-", pos=(300, 157.5), size=(25,25), name="autonScaleInputDown")
        self.label = wx.StaticText(self, label="CORRECT COLORED SIDE of the SCALE?", pos=(410,160))
        self.autonScaleColor = wx.RadioBox(self, pos=(680, 155), choices=["Yes", "No", "9"])
        self.autonScaleColor.ShowItem(2, False)
        self.autonScaleColor.SetSelection(2)
        self.autonScaleColor.Enable(False)



        self.autonPlatformTitle = wx.StaticText(self, label="PLATFORM Zone Cubes", pos=(20, 180))
        self.autonPlatformInput = wx.TextCtrl(self, pos=(220, 180), size=(30,20))
        self.autonPlatformInput.AppendText("0")
        self.autonPlatformInputUp = wx.Button(self, label="+", pos=(270, 177.5), size=(25,25), name="autonPlatformInputUp")
        self.autonPlatformInputDown = wx.Button(self, label="-", pos=(300, 177.5), size=(25,25), name="autonPlatformInputDown")

        self.autonPowerCubeTitle = wx.StaticText(self, label="POWER CUBE Zone Cubes", pos=(20, 200))
        self.autonPowerCubeInput = wx.TextCtrl(self, pos=(220, 200), size=(30,20))
        self.autonPowerCubeInput.AppendText("0")
        self.autonPowerCubeInputUp = wx.Button(self, label="+", pos=(270, 197.5), size=(25,25), name="autonPowerCubeInputUp")
        self.autonPowerCubeInputDown = wx.Button(self, label="-", pos=(300, 197.5), size=(25,25), name="autonPowerCubeInputDown")

        self.autonExchangeTitle = wx.StaticText(self, label="PORTAL Cubes", pos=(20, 220))
        self.autonExchangeInput = wx.TextCtrl(self, pos=(220, 220), size=(30,20))
        self.autonExchangeInput.AppendText("0")
        self.autonExchangeInputUp = wx.Button(self, label="+", pos=(270, 217.5), size=(25,25), name="autonExchangeInputUp")
        self.autonExchangeInputDown = wx.Button(self, label="-", pos=(300, 217.5), size=(25,25), name="autonExchangeInputDown")

        self.title = wx.StaticText(self, label="Where is the robot's STARTING POSITION?", pos=(430,35))
        self.robotPosition = wx.RadioBox(self, pos=(420,30), majorDimension = 2, choices=["9","9","Red1                         ","Blue1","Red2","Blue2","Red3","Blue3"], style = wx.RA_SPECIFY_COLS)
        self.robotPosition.ShowItem(0, False)
        self.robotPosition.ShowItem(1, False)
        self.robotPosition.SetSelection(0)
        self.switchlabel = wx.StaticText(self, label="Switch Alliance sides", pos=(650, 60))
        self.switchlabel.Wrap(80)
        self.redRight = wx.CheckBox(self, pos=(690, 95))

        #TeleOp
        self.teleOpTitle = wx.StaticText(self, label="TeleOperation", pos=(20, 270))
        self.teleOpTitle.SetFont(self.boldFont)

        self.teleOpSwitchTitle = wx.StaticText(self, label="SWITCH Cubes", pos=(20, 290))
        self.teleOpSwitchInput = wx.TextCtrl(self, pos=(220, 290), size=(30,20))
        self.teleOpSwitchInput.AppendText("0")
        self.teleOpSwitchInputUp = wx.Button(self, label="+", pos=(270, 287.5), size=(25,25), name="teleOpSwitchInputUp")
        self.teleOpSwitchInputDown = wx.Button(self, label="-", pos=(300, 287.5), size=(25,25), name="teleOpSwitchInputDown")

        self.teleOpScaleTitle = wx.StaticText(self, label="SCALE Cubes", pos=(20, 310))
        self.teleOpScaleInput = wx.TextCtrl(self, pos=(220, 310), size=(30,20))
        self.teleOpScaleInput.AppendText("0")
        self.teleOpScaleInputUp = wx.Button(self, label="+", pos=(270, 307.5), size=(25,25), name="teleOpScaleInputUp")
        self.teleOpScaleInputDown = wx.Button(self, label="-", pos=(300, 307.5), size=(25,25), name="teleOpScaleInputDown")

        self.teleOpExchangeTitle = wx.StaticText(self, label="PORTAL Cubes", pos=(20, 330))
        self.teleOpExchangeInput = wx.TextCtrl(self, pos=(220, 330), size=(30,20))
        self.teleOpExchangeInput.AppendText("0")
        self.teleOpExchangeInputUp = wx.Button(self, label="+", pos=(270, 327.5), size=(25,25), name="teleOpExchangeInputUp")
        self.teleOpExchangeInputDown = wx.Button(self, label="-", pos=(300, 327.5), size=(25,25), name="teleOpExchangeInputDown")

        self.teleOpOppoSwitchTitle = wx.StaticText(self, label="Cubes on OPPONENT's Switch", pos=(20, 350))
        # self.teleOpExchangeTitle.Wrap(200)
        self.teleOpOppoSwitchInput = wx.TextCtrl(self, pos=(220, 350), size=(30,20))
        self.teleOpOppoSwitchInput.AppendText("0")
        self.teleOpOppoSwitchInputUp = wx.Button(self, label="+", pos=(270, 347.5), size=(25,25), name="teleOpOppoSwitchInputUp")
        self.teleOpOppoSwitchInputDown = wx.Button(self, label="-", pos=(300, 347.5), size=(25,25), name="teleOpOppoSwitchInputDown")

        # self.teleOpFromExchangeTitle = wx.StaticText(self, label="Cubes acquired from the Exchange", pos=(350, 290))
        # self.teleOpFromExchangeInput = wx.TextCtrl(self, pos=(640, 290), size=(30,20))
        # self.teleOpFromExchangeInput.AppendText("0")
        # self.teleOpFromExchangeInputUp = wx.Button(self, label="+", pos=(690, 287.5), size=(25,25), name="teleOpFromExchangeInputUp")
        # self.teleOpFromExchangeInputDown = wx.Button(self, label="-", pos=(720, 287.5), size=(25,25), name="teleOpFromExchangeInputDown")
        #
        # self.teleOpFromPlatformTitle = wx.StaticText(self, label="Cubes acquired from the Platform Zone", pos=(350, 310))
        # self.teleOpFromPlatformInput = wx.TextCtrl(self, pos=(640, 310), size=(30,20))
        # self.teleOpFromPlatformInput.AppendText("0")
        # self.teleOpFromPlatformInputUp = wx.Button(self, label="+", pos=(690, 307.5), size=(25,25), name="teleOpFromPlatformInputUp")
        # self.teleOpFromPlatformInputDown = wx.Button(self, label="-", pos=(720, 307.5), size=(25,25), name="teleOpFromPlatformInputDown")
        #
        # self.teleOpFromPowerCubeTitle = wx.StaticText(self, label="Cubes acquired from the Power Cube Zone", pos=(350, 330))
        # self.teleOpFromPowerCubeInput = wx.TextCtrl(self, pos=(640, 330), size=(30,20))
        # self.teleOpFromPowerCubeInput.AppendText("0")
        # self.teleOpFromPowerCubeInputUp = wx.Button(self, label="+", pos=(690, 327.5), size=(25,25), name="teleOpFromPowerCubeInputUp")
        # self.teleOpFromPowerCubeInputDown = wx.Button(self, label="-", pos=(720, 327.5), size=(25,25), name="teleOpFromPowerCubeInputDown")

        # self.teleOpCubesAcquiredTitle = wx.StaticText(self, label="Cubes acquired in total", pos=(20, 380))

        self.teleOpParked = wx.RadioBox(self, label="Robot parked on the Platform?", pos=(20, 380), choices=["Yes", "Attempted", "No"])
        self.teleOpClimbed = wx.RadioBox(self, label="Robot successfully climbed?", pos=(320, 380), choices=["Yes", "Attempted", "No"])
        self.teleOpTeamwork =  wx.RadioBox(self, label="Robot helped others to climb?", pos=(20, 430), choices=["1", "2", "None"])

        self.teleOpParked.SetSelection(2)
        self.teleOpClimbed.SetSelection(2)
        self.teleOpTeamwork.SetSelection(2)


        #Post-Match questions
        self.postMatchTitle = wx.StaticText(self, label="Post-Match Questions", pos=(20, 480))

        self.strategyTitle = wx.StaticText(self, label="Any specific defensive strategies?", pos=(20, 500))
        self.strategyInput = wx.TextCtrl(self, pos=(300, 500), size = (300, 20))

        self.penaltyTitle = wx.StaticText(self, label="Any fouls or penalties?", pos=(20, 520))
        self.penaltyInput = wx.TextCtrl(self, pos=(300, 520), size = (300, 20))

        self.robotCommentsTitle = wx.StaticText(self, label="What did the robot spend the most time on during this match?", pos=(20, 540))
        self.isRobotScale = wx.CheckBox(self, label="Scale", pos=(20, 560))
        self.isRobotSwitch = wx.CheckBox(self, label="Switch", pos=(100, 560))
        self.isRobotClimb = wx.CheckBox(self, label="Climb", pos=(180, 560))
        self.isRobotExchange = wx.CheckBox(self, label="Exchange", pos=(260, 560))
        self.isRobotDefense = wx.CheckBox(self, label="Defense", pos=(340, 560))
        self.isRobotHelpingOthers = wx.CheckBox(self, label="Helping others climb", pos=(420, 560))
        self.isRobotOthers = wx.CheckBox(self, label="Others", pos=(580, 560))
        self.isRobotOthersInput = wx.TextCtrl(self, pos=(650, 560), size=(100, 20))
        self.isRobotOthersInput.Enable(False)

        self.commentsTitle = wx.StaticText(self, label="Any comments for the robot?", pos=(20, 580))
        self.commentsInput = wx.TextCtrl(self, pos=(20,600), size=(400, 20))
        self.submitButton = wx.Button(self, 10, "Submit Match Data!", pos=(600,700))
        self.submitButton.Enable(False)



        self.matchNumInput.Bind(wx.EVT_TEXT, self.Team_Match)
        self.autonSwitchInput.Bind(wx.EVT_TEXT, self.Switch_Enable)
        self.autonScaleInput.Bind(wx.EVT_TEXT, self.Scale_Enable)
        self.isRobotOthers.Bind(wx.EVT_CHECKBOX, self.Others_Enable)
        self.redRight.Bind(wx.EVT_CHECKBOX, self.Red_Right)


        #Setups
        self.autonSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonScaleInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonScaleInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonPlatformInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonPlatformInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonPowerCubeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonPowerCubeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.autonExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpScaleInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpScaleInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpOppoSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpOppoSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPlatformInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPlatformInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPowerCubeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPowerCubeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)

        self.submitButton.Bind(wx.EVT_BUTTON, self.CSV_OUTPUT)

        self.nameInput.Bind(wx.EVT_TEXT, self.Enable_Submit)
        self.matchNumInput.Bind(wx.EVT_TEXT, self.Enable_Submit)
        self.teamNumInput.Bind(wx.EVT_TEXT, self.Enable_Submit)
        # self.teamNumInput.Bind(wx.EVT_COMBOBOX, self.Enable_Submit)
        self.robotPosition.Bind(wx.EVT_RADIOBOX, self.Enable_Submit)
        self.deadRobot.Bind(wx.EVT_CHECKBOX, self.Enable_Submit)
        self.tick = 0

    def Enable_Submit(self, event):
        if self.nameInput.GetValue() != "" and self.matchNumInput.GetValue() != ""  and self.teamNumInput.GetValue() != "" and self.robotPosition.GetSelection() != 0:
            self.submitButton.Enable()
        elif self.nameInput.GetValue() != "" and self.matchNumInput.GetValue() != "" and self.teamNumInput.GetValue() != "" and self.deadRobot.GetValue():
            self.submitButton.Enable()
        else:
            self.submitButton.Enable(False)
        event.Skip()

    def Red_Right(self, event):
        if self.redRight.GetValue():
            self.robotPosition.SetItemLabel(2, "Blue1                         ")
            self.robotPosition.SetItemLabel(3, "Red1")
            self.robotPosition.SetItemLabel(4, "Blue2")
            self.robotPosition.SetItemLabel(5, "Red2")
            self.robotPosition.SetItemLabel(6, "Blue3")
            self.robotPosition.SetItemLabel(7, "Red3")
            self.robotPosition.SetItemLabel(0, "9")
            self.robotPosition.SetItemLabel(1, "9")
        else:
            self.robotPosition.SetItemLabel(2, "Red1                         ")
            self.robotPosition.SetItemLabel(3, "Blue1")
            self.robotPosition.SetItemLabel(4, "Red2")
            self.robotPosition.SetItemLabel(5, "Blue2")
            self.robotPosition.SetItemLabel(6, "Red3")
            self.robotPosition.SetItemLabel(7, "Blue3")
            self.robotPosition.SetItemLabel(0, "9")
            self.robotPosition.SetItemLabel(1, "9")
        event.Skip()

    def Others_Enable(self, event):
        if self.isRobotOthers.GetValue():
            self.isRobotOthersInput.Enable()
        else:
            self.isRobotOthersInput.Enable(False)
        event.Skip()


    def Switch_Enable(self, event):
        if int(self.autonSwitchInput.GetValue()) > 0:
            self.autonSwitchColor.Enable()
        else:
            self.autonSwitchColor.Enable(False)
        event.Skip()

    def Scale_Enable(self, event):
        if int(self.autonScaleInput.GetValue()) > 0:
            self.autonScaleColor.Enable()
        else:
            self.autonScaleColor.Enable(False)

        event.Skip()


    def Team_Match(self, event):
        self.teamNumInput.Clear()
        matchNum = int(self.matchNumInput.GetValue())
        for i in range(0, len(matchSchedule)):
            if matchSchedule[i]["comp_level"] == "qm" and matchSchedule[i]["match_number"] == matchNum:
                redTeam = matchSchedule[i]["alliances"]["red"]["team_keys"]
                blueTeam = matchSchedule[i]["alliances"]["blue"]["team_keys"]
        red = 1
        blue = 1
        for t in redTeam:
            t = t.replace("frc", "Red  ")
            self.teamNumInput.Append(t)
            red += 1
        for t in blueTeam:
            t = t.replace("frc", "Blue  ")
            self.teamNumInput.Append(t)
            blue += 1
        # self.teamNumInput.GetChildren()[1].SetBackgroundColour(red)
        event.Skip()

    def Number_Change(self, event):
        btn = event.GetEventObject().GetName()
        if btn.endswith("InputUp"):
            textName = btn.replace("InputUp", "")
            num = int(eval("self."+textName+"Input").GetValue())
            eval("self."+textName+"Input").Clear()
            eval("self."+textName+"Input").AppendText(str(num + 1))
            if int(eval("self."+textName+"Input").GetValue()) < 0:
                eval("self."+textName+"Input").Clear()
                eval("self."+textName+"Input").AppendText("0")
        elif btn.endswith("InputDown"):
            textName = btn.replace("InputDown", "")
            num = int(eval("self."+textName+"Input").GetValue())
            eval("self."+textName+"Input").Clear()
            eval("self."+textName+"Input").AppendText(str(num - 1))
            if int(eval("self."+textName+"Input").GetValue()) < 0:
                eval("self."+textName+"Input").Clear()
                eval("self."+textName+"Input").AppendText("0")
        event.Skip()

    def CSV_OUTPUT(self, event):
        teamNum = ""
        print self.teamNumInput.GetValue()
        if self.teamNumInput.GetValue().startswith("R"):
            teamNum = self.teamNumInput.GetValue().replace(self.teamNumInput.GetValue()[0:5], "")
        elif self.teamNumInput.GetValue().startswith("B"):
            teamNum = self.teamNumInput.GetValue().replace(self.teamNumInput.GetValue()[0:6], "")

        filename = self.nameInput.GetValue()

        robot = ""
        if self.isRobotScale.GetValue():
            robot += "Scale, "
        if self.isRobotSwitch.GetValue():
            robot += "Switch, "
        if self.isRobotClimb.GetValue():
            robot += "Climb, "
        if self.isRobotExchange.GetValue():
            robot += "Exchange, "
        if self.isRobotDefense.GetValue():
            robot += "Defense, "
        if self.isRobotHelpingOthers.GetValue():
            robot += "Helping Others Climb, "
        if self.isRobotOthers.GetValue():
            robot += self.isRobotOthersInput.GetValue() + ", "

        robot = robot[:-2]

        # print self.robotPosition.GetSelection()
        # robotPosition = ""
        # if self.robotPosition.GetSelection() == 0:
        #     robotPosition = leftColor+"1"
        # elif self.robotPosition.GetSelection() == 1:
        #     robotPosition = leftColor+"2"
        # elif self.robotPosition.GetSelection() == 2:
        #     robotPosition = leftColor+"3"
        # elif self.robotPosition.GetSelection() == 3:
        #     robotPosition = rightColor+"1"
        # elif self.robotPosition.GetSelection() == 4:
        #     robotPosition = rightColor+"2"
        # elif self.robotPosition.GetSelection() == 5:
        #     robotPosition = rightColor+"3"
        if not Path(myPath + "/ScoutingData", filename + '.csv').exists():
            with open(os.path.join(myPath + "/ScoutingData", filename + '.csv'), 'ab+') as csvfile:
                fieldnames = ['name','matchNumber','teamNumber', 'deadRobot', 'autonPosition','baseline','autonSwitch','autonScale','autonSwitchColor', 'autonScaleColor','autonPZ','autonPCZ','autonExchange','teleopSwitch','teleopScale','teleopExchange','teleopOppoSwitch','robotOnPlatform','robotClimb','buddyBar','strategies','penalties','robotDescription','comments','timeStamp']

                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                writer.writerow({'name':self.nameInput.GetValue(), 'matchNumber':self.matchNumInput.GetValue(), 'teamNumber':teamNum, 'deadRobot':self.deadRobot.GetValue(), 'autonPosition':self.robotPosition.GetItemLabel(self.robotPosition.GetSelection()), 'baseline':self.baselineInput.GetValue(), 'autonSwitch':self.autonSwitchInput.GetValue(), 'autonScale':self.autonScaleInput.GetValue(), 'autonSwitchColor':self.autonSwitchColor.GetSelection(), 'autonScaleColor':self.autonScaleColor.GetSelection(), 'autonPZ':self.autonPlatformInput.GetValue(), 'autonPCZ':self.autonPowerCubeInput.GetValue(), 'autonExchange':self.autonExchangeInput.GetValue(), 'teleopSwitch':self.teleOpSwitchInput.GetValue(), 'teleopScale':self.teleOpScaleInput.GetValue(), 'teleopExchange':self.teleOpExchangeInput.GetValue(), 'teleopOppoSwitch':self.teleOpOppoSwitchInput.GetValue(), 'robotOnPlatform':self.teleOpParked.GetSelection(), 'robotClimb':self.teleOpClimbed.GetSelection(), 'buddyBar':self.teleOpTeamwork.GetSelection(), 'strategies':self.strategyInput.GetValue(), 'penalties':self.penaltyInput.GetValue(), 'robotDescription':robot, 'comments':self.commentsInput.GetValue(),'timeStamp':datetime.now().time()})
        else:
            with open(os.path.join(myPath + "/ScoutingData", filename + '.csv'), 'a') as csvfile:
                fieldnames = ['name','matchNumber','teamNumber', 'deadRobot', 'autonPosition','baseline','autonSwitch','autonScale','autonSwitchColor', 'autonScaleColor','autonPZ','autonPCZ','autonExchange','teleopSwitch','teleopScale','teleopExchange','teleopOppoSwitch','robotOnPlatform','robotClimb','buddyBar','strategies','penalties','robotDescription','comments','timeStamp']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writerow({'name':self.nameInput.GetValue(), 'matchNumber':self.matchNumInput.GetValue(), 'teamNumber':teamNum, 'deadRobot':self.deadRobot.GetValue(), 'autonPosition':self.robotPosition.GetItemLabel(self.robotPosition.GetSelection()), 'baseline':self.baselineInput.GetValue(), 'autonSwitch':self.autonSwitchInput.GetValue(), 'autonScale':self.autonScaleInput.GetValue(), 'autonSwitchColor':self.autonSwitchColor.GetSelection(), 'autonScaleColor':self.autonScaleColor.GetSelection(), 'autonPZ':self.autonPlatformInput.GetValue(), 'autonPCZ':self.autonPowerCubeInput.GetValue(), 'autonExchange':self.autonExchangeInput.GetValue(), 'teleopSwitch':self.teleOpSwitchInput.GetValue(), 'teleopScale':self.teleOpScaleInput.GetValue(), 'teleopExchange':self.teleOpExchangeInput.GetValue(), 'teleopOppoSwitch':self.teleOpOppoSwitchInput.GetValue(), 'robotOnPlatform':self.teleOpParked.GetSelection(), 'robotClimb':self.teleOpClimbed.GetSelection(), 'buddyBar':self.teleOpTeamwork.GetSelection(), 'strategies':self.strategyInput.GetValue(), 'penalties':self.penaltyInput.GetValue(), 'robotDescription':robot, 'comments':self.commentsInput.GetValue(),'timeStamp':datetime.now().time()})
        self.tick += 1

        #Resets
        # self.nameInput.Clear()
        self.matchNumInput.Clear()
        self.teamNumInput.Clear()
        self.baselineInput.SetValue(False)
        self.autonSwitchInput.SetValue("0")
        self.autonScaleInput.SetValue("0")
        self.autonPlatformInput.SetValue("0")
        self.autonPowerCubeInput.SetValue("0")
        self.autonExchangeInput.SetValue("0")
        self.teleOpSwitchInput.SetValue("0")
        self.teleOpScaleInput.SetValue("0")
        self.teleOpExchangeInput.SetValue("0")
        self.teleOpOppoSwitchInput.SetValue("0")
        self.teleOpParked.SetSelection(2)
        self.teleOpClimbed.SetSelection(2)
        self.teleOpTeamwork.SetSelection(2)
        self.strategyInput.Clear()
        self.penaltyInput.Clear()
        self.isRobotScale.SetValue(0)
        self.isRobotSwitch.SetValue(0)
        self.isRobotClimb.SetValue(0)
        self.isRobotExchange.SetValue(0)
        self.isRobotDefense.SetValue(0)
        self.isRobotHelpingOthers.SetValue(0)
        self.isRobotOthers.SetValue(0)
        self.isRobotOthersInput.Clear()
        self.commentsInput.Clear()
        self.robotPosition.SetSelection(0)
        self.autonScaleColor.SetSelection(2)
        self.autonSwitchColor.SetSelection(2)
        self.autonSwitchColor.Enable(False)
        self.autonScaleColor.Enable(False)
        self.isRobotOthersInput.Enable(False)
        self.deadRobot.SetValue(0)


        # print filename
        # print myPath + "/ScoutingData" + filename
        os.system("open -a /Applications/Utilities/Bluetooth\ File\ Exchange.app " + myPath + "/ScoutingData/" + filename + ".csv")
        event.Skip()

app = wx.App(False)
frame = wx.Frame(None, title = "1218 Vulcan Scouting 2018 - Scouts Input", size = (800, 800))
panel = Panel(frame)
frame.Show()
app.MainLoop()
