import wx


class LoadingBlastPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(self, label='Blast loading')
        hbox1.Add(st1, flag=wx.ALIGN_CENTER, border=8)
        vbox.Add(hbox1, flag=wx.ALIGN_CENTER, border=10)

        vbox.Add(wx.Size(50, 50))

        self.btnStop = wx.Button(self, label='Stop', size=(70, 30))
        h_stop = wx.BoxSizer(wx.HORIZONTAL)
        h_stop.Add(self.btnStop, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        vbox.Add(h_stop, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizer(vbox)

        self.btnRun = wx.Button(self, label='To mapping', size=(100, 30))
        self.btnReturn = wx.Button(self, label='Return')

        h_button = wx.BoxSizer(wx.HORIZONTAL)

        h_button.Add(self.btnReturn, flag=wx.LEFT, border=10)

        h_button.Add(wx.Size(470, 10))
        h_button.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(h_button, flag=wx.ALIGN_LEFT | wx.BOTTOM | wx.LEFT, border=10)
