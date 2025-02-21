"""
trying to see the extent of my capabilitites with the mesage boxes
if not for the reminders than I can use them for errors (hoping to put pictures on the reminders)

Options are:
-import Tk (need to pip instal tkintr)
-message box
- just base tkintr
"""

from breezypythongui import EasyFrame
import 

class TrialStuff(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "messingAbout")

        self.messageBox(title = "ERROR", message = "Heyo, that wasn't supposed to happen")





def main():
    TrialStuff().mainloop()


if __name__ == "__main__":
    main()