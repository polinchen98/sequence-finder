import wx
from gui import PreparePanel
from gui import BlastPanel


# Основное окно, из которого открываются окна для закачки геномов и разрезания генома на куски.
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(700, 400))

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        self.panel_one = PreparePanel(self)
        vbox.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btnRun.Bind(wx.EVT_BUTTON, self.NewPanel)

        self.panel_two = BlastPanel(self)
        vbox.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.Hide()
        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?', 'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

    def NewPanel(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.Layout()


app = wx.App()
wnd = MyFrame(None, "S3Finder")
wnd.Show()
app.MainLoop()
