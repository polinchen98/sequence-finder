from enum import Enum
from multiprocessing import Process

import wx

from src.logic import GenomeDownloader


class State(Enum):
    NOT_STARTED = 1
    PROCESSING = 2
    ERROR = 3


# Окно с программой для закачки геномов
class PrepareWindow(wx.Frame):
    download_thread = None
    state = State.NOT_STARTED

    def __init__(self, parent):
        super().__init__(parent, title='Downloading and making database', size=(600, 450))

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        self.panel_one = DownloadPanel(self)
        vbox.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btnRun.Bind(wx.EVT_BUTTON, self.on_run)

        self.loading_panel = LoadingPanel(self)
        vbox.Add(self.loading_panel, 1, wx.EXPAND)
        self.loading_panel.btnStop.Bind(wx.EVT_BUTTON, self.on_stop)
        self.loading_panel.Hide()
        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.on_close_window)

    def on_close_window(self, event):
        if self.state == State.PROCESSING:
            dial = wx.MessageDialog(None, 'Are you sure you want to abort the process and exit?', '?',
                                    wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

            ret = dial.ShowModal()

            if ret == wx.ID_YES:
                self.Destroy()
            else:
                event.Veto()

        if self.state == State.NOT_STARTED:
            self.Destroy()

    def on_run(self, event):
        output = self.panel_one.output.GetValue()
        genus = self.panel_one.genus.GetValue()
        species = self.panel_one.species.GetValue()
        id = self.panel_one.id.GetValue()
        if output != '' and genus != '' and species != '' and id != '':
            self.state = State.PROCESSING

            self.loading_panel.Show()
            self.panel_one.Hide()
            self.Layout()

            self.download_thread = Process(
                target=GenomeDownloader,
                args=(output, genus, species, id))
            self.download_thread.start()
        else:
            wx.MessageDialog(None, 'Not enough data', '', wx.OK).ShowModal()

    def on_stop(self, event):
        self.state = State.NOT_STARTED

        dial = wx.MessageDialog(None, 'Are you sure you want to abort the process?', 'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.download_thread.terminate()
        else:
            event.Veto()
        self.panel_one.Show()
        self.loading_panel.Hide()
        self.Layout()


class DownloadPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)

        st1 = wx.StaticText(self, label='genus')
        self.genus = wx.TextCtrl(self)
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        hbox1.Add(self.genus, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st2 = wx.StaticText(self, label='species')
        self.species = wx.TextCtrl(self)
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        hbox2.Add(self.species, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st3 = wx.StaticText(self, label='accession')
        self.id = wx.TextCtrl(self)
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        hbox3.Add(self.id, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st4 = wx.StaticText(self, label='output')
        self.output = wx.TextCtrl(self)
        hbox4.Add(st4, flag=wx.RIGHT, border=8)
        hbox4.Add(self.output, proportion=1)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st5 = wx.StaticText(self, label='positive_strain')
        self.positive_strain = wx.TextCtrl(self)
        hbox5.Add(st5, flag=wx.RIGHT, border=8)
        hbox5.Add(self.positive_strain, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        st6 = wx.StaticText(self, label='negative_strain')
        self.negative_strain = wx.TextCtrl(self)
        hbox6.Add(st6, flag=wx.RIGHT, border=8)
        hbox6.Add(self.negative_strain, proportion=1)
        vbox.Add(hbox6, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        vbox.Add(wx.Size(50, 50))

        self.btnRun = wx.Button(self, label='RUN', size=(70, 30))
        hrun = wx.BoxSizer(wx.HORIZONTAL)
        hrun.Add(self.btnRun, flag=wx.LEFT, border=10)
        vbox.Add(hrun, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        self.SetSizer(vbox)


class LoadingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)
        hstatus = wx.BoxSizer(wx.HORIZONTAL)

        self.status = wx.StaticText(self, -1, 'Process in progress')

        hstatus.Add(self.status)
        vbox.Add(hstatus, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=1)

        hor = wx.BoxSizer(wx.HORIZONTAL)
        vbox.Add(hor)

        vbox.AddSpacer(50)

        self.btnStop = wx.Button(self, label='Stop', size=(70, 30))
        hstop = wx.BoxSizer(wx.HORIZONTAL)
        hstop.Add(self.btnStop, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        vbox.Add(hstop, flag=wx.ALL | wx.ALIGN_CENTER, border=10)
        self.SetSizer(vbox)
