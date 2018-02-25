# -*- coding: utf-8 -*-
#This file generates the drive team input
import wx
import csv


class Panel(wx.Panel):
    global autonSwitch
    autonSwitch = 0
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #Identifiers
        self.nameTitle = wx.StaticText(self, label="Drive Team Input", pos=(20, 30))
        self.matchNumTitle = wx.StaticText(self, label="Match #", pos=(20, 80))
        self.teamNumTitle = wx.StaticText(self, label="Team #", pos=(350, 80))
        self.matchNumInput = wx.TextCtrl(self, pos=(120, 80), size = (100, 20))
        self.teamNumInput = wx.ComboBox(self, pos=(450, 80), size = (100, 20))

        # self.robotRatingTitle = wx.StaticText(self, label="On a scale 1 to 10, how is this robot?", pos=(20, 120))
        self.robotRating = wx.RadioBox(self, label="On a scale 1 to 10, how did this robot perform?", pos=(20, 120), choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.driveTeamRating = wx.RadioBox(self, label="On a scale 1 to 10, how was the drive team?", pos=(20, 200), choices=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])



        #Post-Match questions
        self.postMatchTitle = wx.StaticText(self, label="Post-Match Questions", pos=(20, 280))

        self.strategyTitle = wx.StaticText(self, label="Any specific strategies\\?", pos=(20, 300))
        self.strategyInput = wx.TextCtrl(self, pos=(300, 300), size = (300, 20))

        self.penaltyTitle = wx.StaticText(self, label="Any fouls or penalties\\?", pos=(20, 320))
        self.penaltyInput = wx.TextCtrl(self, pos=(300, 320), size = (300, 20))


        self.submitButton = wx.Button(self, 10, "Submit Match Data!", pos=(600,700))


        # #Setups
        # self.autonSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonScaleInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonScaleInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonPlatformInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonPlatformInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonPowerCubeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonPowerCubeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.autonExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpScaleInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpScaleInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpOppoSwitchInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpOppoSwitchInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPlatformInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPlatformInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPowerCubeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        # self.teleOpFromPowerCubeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        #
        # self.submitButton.Bind(wx.EVT_BUTTON, self.CSV_OUTPUT)

    def Number_Change(self, event):
        btn = event.GetEventObject().GetName()
        if btn.endswith("InputUp"):
            textName = btn.replace("InputUp", "")
            num = int(eval("self."+textName+"Input").GetValue())
            eval("self."+textName+"Input").Clear()
            eval("self."+textName+"Input").AppendText(str(num + 1))
        elif btn.endswith("InputDown"):
            textName = btn.replace("InputDown", "")
            num = int(eval("self."+textName+"Input").GetValue())
            eval("self."+textName+"Input").Clear()
            eval("self."+textName+"Input").AppendText(str(num - 1))

    def CSV_OUTPUT(self, event):
        with open('entry.csv', 'w') as csvfile:
            fieldnames = ['name','matchNumber','teamNumber','baseline','autonSwitch','autonScale','autonPZ','autonPCZ','autonExchange','teleopSwitch','teleopScale','teleopExchange','teleopOppoSwitch','teleopFromExchange','teleopFromPZ','teleopFromPCZ','robotOnPlatform','robotClimb','buddyBar','strategies','penalties']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'name':self.nameInput.GetValue(), 'matchNumber':self.matchNumInput.GetValue(), 'teamNumber':self.teamNumInput.GetValue(), 'baseline':self.baselineInput.GetValue(), 'autonSwitch':self.autonSwitchInput.GetValue(), 'autonScale':self.autonScaleInput.GetValue(), 'autonPZ':self.autonPlatformInput.GetValue(), 'autonPCZ':self.autonPowerCubeInput.GetValue(), 'autonExchange':self.autonExchangeInput.GetValue(), 'teleopSwitch':self.teleOpSwitchInput.GetValue(), 'teleopScale':self.teleOpScaleInput.GetValue(), 'teleopExchange':self.teleOpExchangeInput.GetValue(), 'teleopOppoSwitch':self.teleOpOppoSwitchInput.GetValue(), 'teleopFromExchange':self.teleOpFromExchangeInput.GetValue(), 'teleopFromPZ':self.teleOpFromPlatformInput.GetValue(), 'teleopFromPCZ':self.teleOpFromPowerCubeInput.GetValue(), 'robotOnPlatform':self.teleOpParked.GetSelection(), 'robotClimb':self.teleOpClimbed.GetSelection(), 'buddyBar':self.teleOpTeamwork.GetSelection(), 'strategies':self.strategyInput.GetValue(), 'penalties':self.penaltyInput.GetValue()})


app = wx.App(False)
frame = wx.Frame(None, title = "1218 Vulcan Scouting Drive Team Input", size = (800, 800))
panel = Panel(frame)
frame.Show()
app.MainLoop()
