"""
-be able to schedule reminders to dates/times
-Repeat reminders in their initial setting only, maybe let you save settings you like so you don’t have to set them up again and again
-Have a function where once a reminder pops up you can either dismiss, mark as completed, 
    -bonus: enter a second option set that lets you set a second reminder for the same thing in a certain (or slightly randomized if you choose) set of time
-Have either an option when creating a reminder where you can pick either to use specific times or range randomized times
    -So you could say, when this shows up, give me the options of 5 min until next remind, 20 min, or 30 min
    Or you could say, in the range of 15-30/20-40/40-60, pick a random number and set a reminder for that time

-I think this'll need to be done with lists of sepcific structures, idk how I'm going to create individual lists per reminder tho

could do a basic dictionary that I dont alter and then create children from it that do?
"""
from breezypythongui import EasyFrame


#ideal world I'd love to add more seperation between things
#need to add variable checking whenever possible
    #message boxes can be used for errors, need to set those nightmares up


class SetReminder(EasyFrame):
    def __init__(self):
        """sets up general options"""
        EasyFrame.__init__(self, title = "Set Reminder")

        #sets reminder name
        self.addLabel(text = "Reminder Name", row = 0, column = 0)
        self.remName = self.addTextField(text = "", row = 0, column = 1)

        #sets reminder time
        self.addLabel(text = "Reminder Time (__.__)", row = 1, column = 0)
        self.remTime = self.addFloatField(value = 0, row = 1, column = 1)

        # repeat #s radio
        self.addLabel(text = "Repeat?", row = 2, column = 0)
        self.remindGroup = self.addRadiobuttonGroup(row = 2, column = 0, columnspan = 6)
        defaultRG = self.remindGroup.addRadiobutton(text = "None") 
        self.remindGroup.setSelectedButton(button = defaultRG)
        self.remindGroup.addRadiobutton(text = "1") 
        self.remindGroup.addRadiobutton(text = "2")
        self.remindGroup.addRadiobutton(text = "3")
        self.remindGroup.addRadiobutton(text = "4")
        self.remindGroup.addRadiobutton(text = "5")

        self.addButton(text = "Done?", row = 4, column = 0, command = self.checkForRepeat) #directs to where it's decided if it needs to set reminder or not


    def checkForRepeat(self):
        """checks if it needs to open the decision tree further"""
        remindNum = self.remindGroup.getSelectedButton()["text"]
        self.addLabel(text = "Select Repeat Method or Set Reminder", row = 5, column = 0)
        self.setReminderButton = self.addButton(text = "Set Reminder", row = 6, column = 0, command = "") # command will be whatever gets the reminder to actually set
        self.specificButton = self.addButton(text = "Specific Period", row = 6, column = 1, command = self.specificTree) # opens specifc's tree
        self.randomButton = self.addButton(text = "Random Periods", row = 6, column = 2, command = self.randomTree) # opens random's decision tree

        #this should be at the center of an if structure that only gets here after the text/num imputs have been validated
        if remindNum == "None":
            self.setReminderButton["state"] = "normal"
            self.specificButton["state"] = "disabled"
            self.randomButton["state"] = "disabled"
        else:
            self.setReminderButton["state"] = "disabled"
            self.specificButton["state"] = "normal"
            self.randomButton["state"] = "normal"


    def randomTree(self):
        self.addLabel(text = "What Range Do You Want The Reminder To Pick From?", row = 7, column = 0)
        self.addLabel(text = "Low:", row = 8, column = 0)
        self.lowRand = self.addIntegerField(value = 0, row = 8, column = 1)
        self.addLabel(text = "High:", row = 9, column = 0)
        self.highRand = self.addIntegerField(value = 0, row = 9, column = 1)
        self.randomDone = self.addButton(text = "Done?", row = 10, column = 0, command = "") #goes to where the random times are handled, which will get printed, then "set reminder"


    def specificTree(self):
        self.addLabel(text = "How Many Minutes Between Each Repeat?", row = 10, column = 0)
        self.specificPeriod = self.addIntegerField(value = 0 , row = 11, column = 0)
        self.specificDone = self.addButton(text = "Done?", row = 12, column = 0, command = "") #goes to where specific times are handled, If I could figure out the source it could probably be in same module as random


    def randomTimes(self, remindNum):
        low = self.lowRand.getNumber()
        high = self.highRand.getNumber()
        randCount = remindNum
        startTime = self.remTime.getNumber()

        for i in range(remindNum):
            #num the bers
            #should pick a rand three times and store
            #each of those should get put on a list of times building off the past one (will need to account for day overflow)
            #these then get passed to the set reminder module


        


    def setReminder(self):
        self.addIntegerField() #we're not touching this one at all yet, not ready for it



def main():
    SetReminder().mainloop()


if __name__ == "__main__":
    main()





"""
FINAL final criteria
- A working GUI tkinter application with at least two windows.  -  need to figure this out
- Implementing a modular approach in your application.  - yeah ok sure
- Consistent clear navigation throughout the GUI application.  -  okie dokie
- Use at least two images in your application(images should have alternate text).  - headers? Reminder Set/Reminder
- Include at least three labels. - done
- Include at least three buttons. - done
- Include at least three call-back functions with each button, including the exit button. - use more buttons to open/submit sections
- Implement secure coding best practices, including input validation to check if the user entered the correct data type,
  make sure the entry box is not empty, etc.  - certain buttons in certain order
"""