import multiprocessing

import wx
import threading
from src.logic import GenomeDownloader


# Окно с программой для закачки геномов
class PrepareWindow(wx.Frame):
    download_thread = None

    def __init__(self, parent):
        super().__init__(parent, title='Downloading and making database', size=(600, 450))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        self.panel_one = DownloadPanel(self)
        vbox.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btnRun.Bind(wx.EVT_BUTTON, self.OnRun)

        self.panel_two = LoadingPanel(self)
        vbox.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btnStop.Bind(wx.EVT_BUTTON, self.OnStop)
        self.panel_two.Hide()
        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.download_thread.terminate()

        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?', 'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

    def OnRun(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.Layout()

        output = self.panel_one.output.GetValue()
        genus = self.panel_one.genus.GetValue()
        species = self.panel_one.species.GetValue()
        id = self.panel_one.id.GetValue()

        self.download_thread = multiprocessing.Process(
            target=lambda: GenomeDownloader(self.log, 'download', 'pectobacterium', 'parmentieri', 'CP027260.1'))
        self.download_thread.start()

    def OnStop(self, event):
        self.download_thread.terminate()

        self.panel_one.Show()
        self.panel_two.Hide()
        self.Layout()

    def log(self, *text):
        print('self.text', *text)

        self.panel_two.status.SetLabel('" ".join(map(str, text))')


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
        self.btnStop = wx.Button(self, label='Stop', size=(70, 30))
        hstop = wx.BoxSizer(wx.HORIZONTAL)
        hstop.Add(self.btnStop, flag=wx.LEFT)
        vbox.Add(hstop, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        self.SetSizer(vbox)

        self.status = wx.StaticText(self, -1, 'Process in progress', pos=(100, 100))
