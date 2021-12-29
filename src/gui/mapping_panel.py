import wx


class MappingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='input')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose file', size=(90, 30))
        hbox1.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_file)

        self.input = wx.TextCtrl(self)
        hbox1.Add(self.input, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(self, label='output')
        hbox2.Add(st3, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose folder', size=(100, 30))
        hbox2.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_folder_output)

        self.output = wx.TextCtrl(self)
        hbox2.Add(self.output, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        h_run = wx.BoxSizer(wx.HORIZONTAL)
        self.btnRun = wx.Button(self, label='Mapping', size=(70, 30))
        h_run.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(h_run, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(wx.Size(30, 200))
        self.btnPrimers = wx.Button(self, label='To making primers', size=(150, 30))
        self.btnReturn = wx.Button(self, label='Return to blast')

        h_button = wx.BoxSizer(wx.HORIZONTAL)

        h_button.Add(self.btnReturn, flag=wx.LEFT | wx.BOTTOM, border=10)

        h_button.Add(wx.Size(400, 10))
        h_button.Add(self.btnPrimers, flag=wx.LEFT | wx.BOTTOM, border=10)
        vbox.Add(h_button, flag=wx.ALIGN_LEFT | wx.BOTTOM, border=10)

    def choose_file(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file...")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.input.SetValue(str(paths))
        dlg.Destroy()

    def choose_folder_output(self, event):
        dlg = wx.DirDialog(
            self, message="Choose a folder...")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.output.SetValue(str(paths))
        dlg.Destroy()
