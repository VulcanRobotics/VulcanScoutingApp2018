# -*- coding: utf-8 -*-
import wx
import csv


class Panel(wx.Panel):
    global autonSwitch
    autonSwitch = 0
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        #Identifiers
        self.nameTitle = wx.StaticText(self, label="Name", pos=(20, 30))
        self.matchNumTitle = wx.StaticText(self, label="Match #", pos=(20, 50))
        self.teamNumTitle = wx.StaticText(self, label="Team #", pos=(350, 50))
        self.nameInput = wx.TextCtrl(self, pos=(120, 30), size = (100, 20))
        self.matchNumInput = wx.TextCtrl(self, pos=(120, 50), size = (100, 20))
        self.teamNumInput = wx.ComboBox(self, pos=(450, 50), size = (100, 20))

        #Autons
        self.autonTitle = wx.StaticText(self, label="Auton", pos=(20, 100))

        self.baselineTitle = wx.StaticText(self, label="Baseline", pos=(20, 120))
        self.baselineInput = wx.CheckBox(self, pos=(100,120))

        self.autonSwitchTitle = wx.StaticText(self, label="# of cubes on the Switch", pos=(20, 140))
        self.autonSwitchInput = wx.TextCtrl(self, pos=(300, 140), size=(30,20))
        self.autonSwitchInput.AppendText("0")
        self.autonSwitchInputUp = wx.Button(self, label="+", pos=(350, 137.5), size=(25,25), name="autonSwitchInputUp")
        self.autonSwitchInputDown = wx.Button(self, label="-", pos=(380, 137.5), size=(25,25), name="autonSwitchInputDown")


        self.autonScaleTitle = wx.StaticText(self, label="# of cubes on the Scale", pos=(20, 160))
        self.autonScaleInput = wx.TextCtrl(self, pos=(300, 160), size=(30,20))
        self.autonScaleInput.AppendText("0")
        self.autonScaleInputUp = wx.Button(self, label="+", pos=(350, 157.5), size=(25,25), name="autonScaleInputUp")
        self.autonScaleInputDown = wx.Button(self, label="-", pos=(380, 157.5), size=(25,25), name="autonScaleInputDown")

        self.autonPlatformTitle = wx.StaticText(self, label="# of cubes got from the Plateform Zone", pos=(20, 180))
        self.autonPlatformInput = wx.TextCtrl(self, pos=(300, 180), size=(30,20))
        self.autonPlatformInput.AppendText("0")
        self.autonPlatformInputUp = wx.Button(self, label="+", pos=(350, 177.5), size=(25,25), name="autonPlatformInputUp")
        self.autonPlatformInputDown = wx.Button(self, label="-", pos=(380, 177.5), size=(25,25), name="autonPlatformInputDown")

        self.autonPowerCubeTitle = wx.StaticText(self, label="# of cubes got from the Power Cube Zone", pos=(20, 200))
        self.autonPowerCubeInput = wx.TextCtrl(self, pos=(300, 200), size=(30,20))
        self.autonPowerCubeInput.AppendText("0")
        self.autonPowerCubeInputUp = wx.Button(self, label="+", pos=(350, 197.5), size=(25,25), name="autonPowerCubeInputUp")
        self.autonPowerCubeInputDown = wx.Button(self, label="-", pos=(380, 197.5), size=(25,25), name="autonPowerCubeInputDown")

        self.autonExchangeTitle = wx.StaticText(self, label="# of cubes got from the Exchange", pos=(20, 220))
        self.autonExchangeInput = wx.TextCtrl(self, pos=(300, 220), size=(30,20))
        self.autonExchangeInput.AppendText("0")
        self.autonExchangeInputUp = wx.Button(self, label="+", pos=(350, 217.5), size=(25,25), name="autonExchangeInputUp")
        self.autonExchangeInputDown = wx.Button(self, label="-", pos=(380, 217.5), size=(25,25), name="autonExchangeInputDown")

        #TeleOp
        self.teleOpTitle = wx.StaticText(self, label="TeleOperation", pos=(20, 270))

        self.teleOpSwitchTitle = wx.StaticText(self, label="# of cubes on the Switch", pos=(20, 290))
        self.teleOpSwitchInput = wx.TextCtrl(self, pos=(220, 290), size=(30,20))
        self.teleOpSwitchInput.AppendText("0")
        self.teleOpSwitchInputUp = wx.Button(self, label="+", pos=(270, 287.5), size=(25,25), name="teleOpSwitchInputUp")
        self.teleOpSwitchInputDown = wx.Button(self, label="-", pos=(300, 287.5), size=(25,25), name="teleOpSwitchInputDown")

        self.teleOpScaleTitle = wx.StaticText(self, label="# of cubes on the Scale", pos=(20, 310))
        self.teleOpScaleInput = wx.TextCtrl(self, pos=(220, 310), size=(30,20))
        self.teleOpScaleInput.AppendText("0")
        self.teleOpScaleInputUp = wx.Button(self, label="+", pos=(270, 307.5), size=(25,25), name="teleOpScaleInputUp")
        self.teleOpScaleInputDown = wx.Button(self, label="-", pos=(300, 307.5), size=(25,25), name="teleOpScaleInputDown")

        self.teleOpExchangeTitle = wx.StaticText(self, label="# of cubes to the Exchange", pos=(20, 330))
        self.teleOpExchangeInput = wx.TextCtrl(self, pos=(220, 330), size=(30,20))
        self.teleOpExchangeInput.AppendText("0")
        self.teleOpExchangeInputUp = wx.Button(self, label="+", pos=(270, 327.5), size=(25,25), name="teleOpExchangeInputUp")
        self.teleOpExchangeInputDown = wx.Button(self, label="-", pos=(300, 327.5), size=(25,25), name="teleOpExchangeInputDown")

        self.teleOpOppoSwitchTitle = wx.StaticText(self, label="# of cubes on opponent's Switch", pos=(20, 350))
        # self.teleOpExchangeTitle.Wrap(200)
        self.teleOpOppoSwitchInput = wx.TextCtrl(self, pos=(220, 350), size=(30,20))
        self.teleOpOppoSwitchInput.AppendText("0")
        self.teleOpOppoSwitchInputUp = wx.Button(self, label="+", pos=(270, 347.5), size=(25,25), name="teleOpOppoSwitchInputUp")
        self.teleOpOppoSwitchInputDown = wx.Button(self, label="-", pos=(300, 347.5), size=(25,25), name="teleOpOppoSwitchInputDown")

        self.teleOpFromExchangeTitle = wx.StaticText(self, label="# of cubes acquired from the Exchange", pos=(350, 290))
        self.teleOpFromExchangeInput = wx.TextCtrl(self, pos=(640, 290), size=(30,20))
        self.teleOpFromExchangeInput.AppendText("0")
        self.teleOpFromExchangeInputUp = wx.Button(self, label="+", pos=(690, 287.5), size=(25,25), name="teleOpFromExchangeInputUp")
        self.teleOpFromExchangeInputDown = wx.Button(self, label="-", pos=(720, 287.5), size=(25,25), name="teleOpFromExchangeInputDown")

        self.teleOpFromPlatformTitle = wx.StaticText(self, label="# of cubes acquired from the Platform Zone", pos=(350, 310))
        self.teleOpFromPlatformInput = wx.TextCtrl(self, pos=(640, 310), size=(30,20))
        self.teleOpFromPlatformInput.AppendText("0")
        self.teleOpFromPlatformInputUp = wx.Button(self, label="+", pos=(690, 307.5), size=(25,25), name="teleOpFromPlatformInputUp")
        self.teleOpFromPlatformInputDown = wx.Button(self, label="-", pos=(720, 307.5), size=(25,25), name="teleOpFromPlatformInputDown")

        self.teleOpFromPowerCubeTitle = wx.StaticText(self, label="# of cubes acquired from the Power Cube Zone", pos=(350, 330))
        self.teleOpFromPowerCubeInput = wx.TextCtrl(self, pos=(640, 330), size=(30,20))
        self.teleOpFromPowerCubeInput.AppendText("0")
        self.teleOpFromPowerCubeInputUp = wx.Button(self, label="+", pos=(690, 327.5), size=(25,25), name="teleOpFromPowerCubeInputUp")
        self.teleOpFromPowerCubeInputDown = wx.Button(self, label="-", pos=(720, 327.5), size=(25,25), name="teleOpFromPowerCubeInputDown")

        self.teleOpParked = wx.RadioBox(self, label="Robot parked on the Platform\\?", pos=(20, 380), choices=["Yes", "Attempted", "No"])
        self.teleOpClimbed = wx.RadioBox(self, label="Robot successfully climbed\\?", pos=(320, 380), choices=["Yes", "Attempted", "No"])
        self.teleOpTeamwork =  wx.RadioBox(self, label="Robot has mechanisms to assist others with climbing\\?", pos=(20, 430), choices=["Yes", "Attempted", "No"])


        #Post-Match questions
        self.postMatchTitle = wx.StaticText(self, label="Post-Match Questions", pos=(20, 480))

        self.strategyTitle = wx.StaticText(self, label="Any specific strategies\\?", pos=(20, 500))
        self.strategyInput = wx.TextCtrl(self, pos=(300, 500), size = (300, 20))

        self.penaltyTitle = wx.StaticText(self, label="Any fouls or penalties\\?", pos=(20, 520))
        self.penaltyInput = wx.TextCtrl(self, pos=(300, 520), size = (300, 20))


        self.submitButton = wx.Button(self, 10, "Submit Match Data!", pos=(600,700))


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
        self.teleOpFromExchangeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpFromExchangeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpFromPlatformInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpFromPlatformInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpFromPowerCubeInputUp.Bind(wx.EVT_BUTTON, self.Number_Change)
        self.teleOpFromPowerCubeInputDown.Bind(wx.EVT_BUTTON, self.Number_Change)

        self.submitButton.Bind(wx.EVT_BUTTON, self.CSV_OUTPUT)

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
frame = wx.Frame(None, title = "1218 Vulcan Scouting 2018", size = (800, 800))
panel = Panel(frame)
frame.Show()
app.MainLoop()
