import wx
from .splitter_window import SplitterWindow
from .prepare_window import PrepareWindow


class PreparePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.Size(50, 50))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        statictext1 = wx.StaticText(self, wx.ID_ANY, label="Do you need to download genomes and create a database?")
        statictext2 = wx.StaticText(self, wx.ID_ANY, label="Do you need to split the genome?")

        hbox1.Add(statictext1, flag=wx.ALIGN_CENTER)
        hbox2.Add(statictext2, flag=wx.ALIGN_CENTER)

        vbox.Add(hbox1, flag=wx.ALIGN_CENTER)
        vbox.Add(hbox2, flag=wx.ALIGN_CENTER)

        btn_yes1 = wx.Button(self, wx.ID_ANY, label="Yes", size=(50, 30))
        btn_yes2 = wx.Button(self, wx.ID_ANY, label="Yes", size=(50, 30))

        hbox1.Add(btn_yes1, flag=wx.ALL, border=10)
        hbox2.Add(btn_yes2, flag=wx.ALL, border=10)

        vbox.Add(wx.Size(100, 100))

        btn_yes1.Bind(wx.EVT_BUTTON, self.OpenPrepareWindow)
        btn_yes2.Bind(wx.EVT_BUTTON, self.OpenSplitterWindow)

        # кнопка RUN
        self.btnRun = wx.Button(self, label='To Blast Step')
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(hbox3, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        self.SetSizer(vbox)

    def OpenPrepareWindow(self, event):
        secondWindow = PrepareWindow(parent=wx.Panel(self))
        secondWindow.Show()

    def OpenSplitterWindow(self, event):
        thirdWindow = SplitterWindow(parent=wx.Panel(self))
        thirdWindow.Show()
