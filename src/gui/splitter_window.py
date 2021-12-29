import wx
from src.logic import Splitter


class SplitterWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, 'Splitter', size=(600, 300))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(panel, label='sequence')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(panel, label='choose file', size=(90, 30))
        hbox1.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_file)

        self.sequence = wx.TextCtrl(panel)
        hbox1.Add(self.sequence, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st2 = wx.StaticText(panel, label='length')
        self.length = wx.TextCtrl(panel)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        hbox2.Add(self.length, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st3 = wx.StaticText(panel, label='interval')
        self.interval = wx.TextCtrl(panel)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        hbox3.Add(self.interval, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st4 = wx.StaticText(panel, label='output')
        self.output = wx.TextCtrl(panel)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        hbox4.Add(self.output, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add(wx.Size(50, 50))

        btnRun = wx.Button(panel, label='RUN', size=(70, 30))
        hrun = wx.BoxSizer(wx.HORIZONTAL)
        hrun.Add(btnRun, flag=wx.LEFT, border=10)
        vbox.Add(hrun, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        panel.SetSizer(vbox)
        btnRun.Bind(wx.EVT_BUTTON, self.split_sequence)

    def choose_file(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.sequence.SetValue(str(paths))
        dlg.Destroy()

    def split_sequence(self, event):
        output = self.output.GetValue()
        interval = self.interval.GetValue()
        length = self.length.GetValue()
        sequence = self.sequence.GetValue()
        if output != '' and interval != '' and length != '' and sequence != '':
            Splitter(output, sequence, int(length), int(interval))
        else:
            wx.MessageDialog(None, 'Not enough data', '!', wx.OK).ShowModal()
