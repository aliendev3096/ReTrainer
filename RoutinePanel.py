import wx;
from ObjectListView import ObjectListView, ColumnDefn, GroupListView

class RoutinePanel(wx.Panel):
    def __init__(self, parent):
        super(RoutinePanel, self).__init__(parent, wx.ID_ANY)

        self.active_routine = self.GetParent().GetParent().active_routine

        if self.active_routine is not None:
            self.sessions = self.active_routine["sessions"]
        else:
            self.sessions = []

        self.routineView = GroupListView(self, wx.ID_ANY, style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.routineView.SetColumns([
            ColumnDefn("Date", "left", 200, "date"),
            ColumnDefn("Workout Name", "left", 280, "workoutName"),
            ColumnDefn("Target", "left", 200, "muscleGroup"),
            ColumnDefn("Weight", "left", 150, "weight"),
            ColumnDefn("Sets", "right", 50, "sets"),
            ColumnDefn("Reps", "left", 50, "reps")
        ])

        self.routineView.cellEditMode = ObjectListView.CELLEDIT_DOUBLECLICK
        self.routineViewSizer = wx.BoxSizer(wx.VERTICAL)
        self.routineViewSizer.Add(self.routineView, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(self.routineViewSizer)


    # Routine Event Handler
    def onPageChangeListener(self, event=None):
        # Clear the routines
        self.sessions = []
        self.active_routine = self.GetParent().GetParent().active_routine

        # if active routine is set, generate list
        if self.active_routine is not None:
            sessions = self.active_routine["sessions"]

            # For each session, append the workouts
            for session in sessions:
                for workout in session["workouts"]:
                    # Append the date to each workout for ObjectListView grouping
                    workout["date"] = session["date"]

                self.sessions.extend(session["workouts"])

            self.routineView.SetObjects(self.sessions)


