# Author: Jeff Vang
# https://exrx.net/Lists/Directory
from classes import Workout, Session, Routine
import MainWindow;
import wx;
import os;
import json;

def main():
    # Create a GUI?
    # Initialize Application With Settings
    if not os.path.exists('settings.json'):
        defaultSettings = {};
        defaultSettings['Settings'] = {};
        defaultSettings['Settings']['Default_User'] = "Default_User";
        with open('settings.json', 'w') as outfile:
            json.dump(defaultSettings, outfile);

    # Load Settings
    try:
        with open('settings.json') as settingsjson:
            settings = json.load(settingsjson);
            active_user = settings["Settings"]['Default_User']
    except FileNotFoundError:
        wx.MessageBox('No Settings were found.', 'Info', wx.OK | wx.ICON_INFORMATION);

    # Load Routines if any exist
    try:
        with open('./profiles/{}.json'.format(active_user), 'r') as userjson:
            userData = json.load(userjson)
            if(len(userData["Routines"]) > 0):
                routines = userData["Routines"]
            else:
                routines = []
    except FileNotFoundError:
        wx.MessageBox('No Routines were found.', 'Info', wx.OK | wx.ICON_INFORMATION);

    app = wx.App();
    frame = MainWindow.MainWindow(None, "MyTrainer", active_user, routines);
    app.MainLoop();


main();