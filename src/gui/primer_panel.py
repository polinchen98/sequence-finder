import wx


class PrimerPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        hbox9 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(self, label='input')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose file', size=(90, 30))
        hbox1.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_file)

        self.input = wx.TextCtrl(self)
        hbox1.Add(self.input, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st2 = wx.StaticText(self, label='output')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose folder', size=(100, 30))
        hbox2.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_folder_output)

        self.output = wx.TextCtrl(self)
        hbox2.Add(self.output, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st3 = wx.StaticText(self, label='length')
        self.length = wx.TextCtrl(self)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        hbox3.Add(self.length, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st4 = wx.StaticText(self, label='optimum length')
        self.opt = wx.TextCtrl(self)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        hbox4.Add(self.opt, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st5 = wx.StaticText(self, label='minimum length')
        self.min = wx.TextCtrl(self)
        hbox5.Add(st5, flag=wx.RIGHT, border=8)
        hbox5.Add(self.min, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st6 = wx.StaticText(self, label='maximum length')
        self.max = wx.TextCtrl(self)
        hbox6.Add(st6, flag=wx.RIGHT, border=8)
        hbox6.Add(self.max, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st7 = wx.StaticText(self, label='optimum temperature (C)')
        self.tm_opt = wx.TextCtrl(self, value='60.0')
        hbox7.Add(st7, flag=wx.RIGHT, border=8)
        hbox7.Add(self.tm_opt, proportion=1)
        vbox.Add(hbox7, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st8 = wx.StaticText(self, label='minimum temperature (C)')
        self.tm_min = wx.TextCtrl(self, value='57.0')
        hbox8.Add(st8, flag=wx.RIGHT, border=8)
        hbox8.Add(self.tm_min, proportion=1)
        vbox.Add(hbox8, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st9 = wx.StaticText(self, label='maximum temperature (C)')
        self.tm_max = wx.TextCtrl(self, value='63.0')
        hbox9.Add(st9, flag=wx.RIGHT, border=8)
        hbox9.Add(self.tm_max, proportion=1)
        vbox.Add(hbox9, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        self.btnRun = wx.Button(self, label='Make primers!', size=(100, 30))
        h_run = wx.BoxSizer(wx.HORIZONTAL)
        h_run.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(h_run, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)

        self.btnReturn = wx.Button(self, label='Return to step mapping')
        h_return = wx.BoxSizer(wx.HORIZONTAL)
        h_return.Add(self.btnReturn, flag=wx.EXPAND, border=10)
        vbox.Add(h_return, flag=wx.ALIGN_LEFT | wx.BOTTOM | wx.LEFT, border=10)

    def choose_file(self, event):
        dlg = wx.DirDialog(
            self, message="Choose a file")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.input.SetValue(str(paths))
        dlg.Destroy()

    def choose_folder_output(self, event):
        dlg = wx.DirDialog(
            self, message="Choose a folder")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.output.SetValue(str(paths))
        dlg.Destroy()
