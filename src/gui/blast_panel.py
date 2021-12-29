import wx
from src.logic import Blast


class BlastPanel(wx.Panel):
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

        st1 = wx.StaticText(self, label='input')
        hbox1.Add(st1, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose file', size=(90, 30))
        hbox1.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_file)

        self.input = wx.TextCtrl(self)
        hbox1.Add(self.input, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st2 = wx.StaticText(self, label='database')
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        btn_file = wx.Button(self, label='choose folder', size=(100, 30))
        hbox2.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_folder_database)

        self.database = wx.TextCtrl(self)
        hbox2.Add(self.database, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st3 = wx.StaticText(self, label='output')
        hbox3.Add(st3, flag=wx.RIGHT, border=8)

        btn_file = wx.Button(self, label='choose folder', size=(100, 30))
        hbox3.Add(btn_file, flag=wx.RIGHT, border=8)
        btn_file.Bind(wx.EVT_BUTTON, self.choose_folder_output)

        self.output = wx.TextCtrl(self)
        hbox3.Add(self.output, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st4 = wx.StaticText(self, label='e-value')
        self.evalue = wx.TextCtrl(self, value='10')
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        hbox4.Add(self.evalue, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st5 = wx.StaticText(self, label='num_threads')
        self.num_threads = wx.TextCtrl(self)
        hbox5.Add(st5, flag=wx.RIGHT, border=8)
        hbox5.Add(self.num_threads, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        tasks_list = ['blastn', 'dc-megablast', 'megablast', 'blastn-short']

        self.rbox = wx.RadioBox(self, label='Task', choices=tasks_list,
                                majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        hbox6.Add(self.rbox)
        vbox.Add(hbox6)

        vbox.Add(wx.Size(50, 50))

        self.btnRun = wx.Button(self, label='RUN', size=(70, 30))
        self.btnReturn = wx.Button(self, label='Return to prepare')
        h_btn = wx.BoxSizer(wx.HORIZONTAL)
        h_btn.Add(self.btnReturn, flag=wx.LEFT, border=10)
        h_btn.Add(wx.Size(450, 10))
        h_btn.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(h_btn, flag=wx.ALIGN_LEFT | wx.BOTTOM | wx.LEFT, border=10)

    def choose_file(self, event):
        dlg = wx.FileDialog(
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

    def choose_folder_database(self, event):
        dlg = wx.DirDialog(
            self, message="Choose a folder")
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPath()
            self.database.SetValue(str(paths))
        dlg.Destroy()
