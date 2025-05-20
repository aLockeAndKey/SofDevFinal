"""
-be able to schedule reminders to dates/times
-Repeat reminders in their initial setting only, maybe let you save settings you like so you don’t have to set them up again and again
-Have a function where once a reminder pops up you can either dismiss or mark as completed
    -the massage boxes don't do this, only output text, will need to use tkinter
    -this is an ideal world, i don't understand tkintr
-Have either an option when creating a reminder where you can pick either to use specific times or range randomized times
    -So you could say, when this shows up, give me the options of 5 min until next remind, 20 min, or 30 min
        -probably ditching this for only one time, could go back for later but not at present
    -Or you could say, in the range of 15-30/20-40/40-60, pick a random number and set a reminder for that time


    try import time and then time.sleep(x)
"""
from breezypythongui import EasyFrame
import tkinter
import time
import datetime #if I say "from datetime import *" then it throws the error that time.sleep(1) has no attribute in datetime.time.
#but if I remove it then datetime has no attribute "now"
import random


class SetReminder(EasyFrame):
    def __init__(self):
        """sets up general options"""
        EasyFrame.__init__(self, title = "Set Reminder")

        #sets reminder name
        self.addLabel(text = "Reminder Name", row = 0, column = 0)
        self.remName = self.addTextField(text = "", row = 0, column = 1)

        #sets reminder time
        self.addLabel(text = "Reminder Hour (00-24)", row = 1, column = 0)
        self.remHour = self.addIntegerField(value = 0, row = 1, column = 1)

        self.addLabel(text = "Reminder Minute (00-60)", row = 1, column = 2)
        self.remMin = self.addIntegerField(value = 0, row = 1, column = 4)

        # repeat #s radio
        self.addLabel(text = "Repeat?", row = 3, column = 0)
        self.remindGroup = self.addRadiobuttonGroup(row = 4, column = 0, columnspan = 6)
        defaultRG = self.remindGroup.addRadiobutton(text = "None") 
        self.remindGroup.setSelectedButton(button = defaultRG)
        self.remindGroup.addRadiobutton(text = "1") 
        self.remindGroup.addRadiobutton(text = "2")
        self.remindGroup.addRadiobutton(text = "3")
        self.remindGroup.addRadiobutton(text = "4")
        self.remindGroup.addRadiobutton(text = "5")

        self.addButton(text = "Done?", row = 5, column = 0, command = self.checkForRepeat) #directs to where it's decided if it needs to set reminder or not


    def checkForRepeat(self):
        """checks if it needs to open the decision tree further"""
        remName = self.remName.getValue()
        remHour = int(self.remHour.getValue())
        remMin = int(self.remMin.getValue())

        if str(remName) == "" or str(remHour) == "" or str(remMin) == "": #not processing, running next two checks instead
            self.messageBox(title = "ERROR", message = "Make Sure No Field Is Blank And Press 'Done?' Again")
        elif remHour > 24 or remHour < 0: #TypeError: '>' not supported between instances of 'FloatField' and 'float'
            self.messageBox(title = "ERROR", message = "Please Enter A Valid Hour And Press 'Done?' Again")
        elif remMin < 0 or remMin > 60:
            self.messageBox(title = "ERROR", message = "Please Enter A Valid Minute And Press 'Done?' Again")
        else:
            remindNum = self.remindGroup.getSelectedButton()["text"]
            self.addLabel(text = "Select Repeat Method or Set Reminder", row = 6, column = 0)
            self.setReminderButton = self.addButton(text = "Set Reminder", row = 7, column = 0, command = self.setReminder) #adding the function call with the extra varis breaks the buttons
            self.specificButton = self.addButton(text = "Specific Period", row = 7, column = 1, command = self.specificTree) # opens specifc's tree
            self.randomButton = self.addButton(text = "Random Periods", row = 7, column = 2, command = self.randomTree) # opens random's decision tree


        if remindNum == "None":
            self.setReminderButton["state"] = "normal"
            self.specificButton["state"] = "disabled"
            self.randomButton["state"] = "disabled"
        else:
            self.setReminderButton["state"] = "disabled"
            self.specificButton["state"] = "normal"
            self.randomButton["state"] = "normal"


    def randomTree(self):
        """sets up the rand range for times"""
        self.addLabel(text = "What Range Do You Want The Reminder To Pick From?", row = 8, column = 0)
        self.addLabel(text = "Low:", row = 9, column = 0)
        self.lowRand = self.addIntegerField(value = 0, row = 9, column = 1)
        self.addLabel(text = "High:", row = 10, column = 0)
        self.highRand = self.addIntegerField(value = 0, row = 10, column = 1)
        self.randomDone = self.addButton(text = "Done?", row = 11, column = 0, command = self.randomTimes) #goes to where the random times are handled, which will get printed, then "set reminder"


    def specificTree(self):
        """sets up the spcified range for times"""
        self.addLabel(text = "How Many Minutes Between Each Repeat?", row = 11, column = 0)
        self.specificPeriod = self.addIntegerField(value = 0 , row = 12, column = 0)
        self.specificDone = self.addButton(text = "Done?", row = 13, column = 0, command = self.setTimes) #goes to where specific times are handled, If I could figure out the source it could probably be in same module as random


    def setReminder(self, spacingList = [], remindNum = 0):
        """eventually communicates with computer at large to set reminder"""
        """modified from the geeksforgeeks website on setting an alarm clock in tkinter"""
       def setReminder(self, spacingList = [], remindNum = 0):
        """eventually communicates with computer at large to set reminder"""
        """modified from the geeksforgeeks website on setting an alarm clock in tkinter"""
        remHour = int(self.remHour.getValue())
        remMin = int(self.remMin.getValue())
        remName = self.remName["text"]

        while True:
            set_alarm = f"{remHour}:{remMin}:{0}"

            time.sleep(1)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            if current_time == set_alarm:
                self.messageBox(title = "REMINDER", message = remName)


    
    def randomTimes(self, remindNum):
        """creates a list with random numbers to pass to setReminder"""
        low = self.lowRand["integer"]
        high = self.highRand["integer"]
        randCount = remindNum
        spacingList = []

        for i in range(int(randCount)):
            spacingList.append(random(low, high))
        
        self.setReminder(self, spacingList, randCount)

    def setTimes(self, remindNum):
        """creates a list with one number to pass to setReminder"""
        period = self.specificPeriod
        repCount = remindNum
        spacingList = []

        for i in range(int(repCount)):
            spacingList.append(period)

        self.setReminder(self, spacingList, repCount)




        



def main():
    SetReminder().mainloop()


if __name__ == "__main__":
    main()





