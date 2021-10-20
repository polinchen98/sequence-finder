import threading
import wx
from threading import Thread

ID_RUN = 101
ID_RUN2 = 102


class ChildThread(Thread):
    def __init__(self, myframe):
        Thread.__init__(self)
        self.myframe = myframe

    def run(self):
        wx.CallAfter(self.myframe.AfterRun, 'Ok button pressed')


class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title)
        panel = wx.Panel(self, -1)
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer.Add(wx.Button(panel, ID_RUN, "OK"))
        mainSizer.Add(wx.Button(panel, ID_RUN2, "Cancel"))
        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
        wx.EVT_BUTTON(self, ID_RUN, self.onRun)
        wx.EVT_BUTTON(self, ID_RUN2, self.onRun2)

    def onRun(self, event):
        self.child = ChildThread(myframe=self)
        self.child.daemon = True
        self.child.start()

    def onRun2(self, event):
        self.child2 = threading.Thread(None, self.__run)
        self.child2.daemon = True
        self.child2.start()

    def __run(self):
        wx.CallAfter(self.AfterRun, "Cancel button pressed")

    def AfterRun(self, msg):
        dlg = wx.MessageDialog(self, msg, "Message", wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "My GUI")
        frame.Show(True)
        frame.Centre()
        return True

app = MyApp(0)
app.MainLoop()
