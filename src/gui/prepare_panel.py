import wx
from .splitter_window import SplitterWindow
from .prepare_window import PrepareWindow


class PreparePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        staticbox1 = wx.StaticBox(self, wx.ID_ANY, label="Нужно ли скачивать геномы и создавать базу данных?")
        staticbox2 = wx.StaticBox(self, wx.ID_ANY, label="Нужно ли разрезать геном?")

        sizer_1 = wx.StaticBoxSizer(staticbox1, wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(staticbox2, wx.HORIZONTAL)

        vbox.Add(sizer_1)
        vbox.Add(sizer_2)

        btn_yes1 = wx.Button(self, wx.ID_ANY, label="Да", size=(50, 30), pos=(210, 30))
        btn_yes2 = wx.Button(self, wx.ID_ANY, label="Да", size=(50, 30), pos=(210, 95))

        sizer_1.Add(btn_yes1, flag=wx.ALL, border=8)
        sizer_2.Add(btn_yes2, flag=wx.ALL, border=8)

        vbox.Add(wx.Size(100, 100))

        btn_yes1.Bind(wx.EVT_BUTTON, self.OpenPrepareWindow)
        btn_yes2.Bind(wx.EVT_BUTTON, self.OpenSplitterWindow)

        # кнопка RUN
        self.btnRun = wx.Button(self, label='RUN', size=(70, 30))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        self.SetSizer(vbox)

    def OpenPrepareWindow(self, event):
        secondWindow = PrepareWindow(parent=wx.Panel(self))
        secondWindow.Show()

    def OpenSplitterWindow(self, event):
        thirdWindow = SplitterWindow(parent=wx.Panel(self))
        thirdWindow.Show()

