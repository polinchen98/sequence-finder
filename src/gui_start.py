from multiprocessing import Process

import wx
from gui import MainPanel
from gui import PreparePanel
from gui import BlastPanel
from gui import LoadingBlastPanel
from gui import MappingPanel
from gui import PrimerPanel
from src import GenomeMapping
from src import Blast
from src import PrimersMaking
import multiprocessing


class MyFrame(wx.Frame):
    blast_thread = None

    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(700, 400))

        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)

        self.main_panel = MainPanel(self)
        vbox.Add(self.main_panel, 1, wx.EXPAND)
        self.main_panel.btn_prepare.Bind(wx.EVT_BUTTON, self.open_prepare_panel)
        self.main_panel.btn_blast.Bind(wx.EVT_BUTTON, self.open_blast_panel)
        self.main_panel.btn_primer.Bind(wx.EVT_BUTTON, self.open_primer_panel)

        self.prepare_panel = PreparePanel(self)
        vbox.Add(self.prepare_panel, 1, wx.EXPAND)
        self.prepare_panel.btnRun.Bind(wx.EVT_BUTTON, self.open_blast_panel)
        self.prepare_panel.Hide()
        self.Centre()

        self.blast_panel = BlastPanel(self)
        vbox.Add(self.blast_panel, 1, wx.EXPAND)
        self.blast_panel.btnReturn.Bind(wx.EVT_BUTTON, self.open_prepare_panel)
        self.blast_panel.btnRun.Bind(wx.EVT_BUTTON, self.blast_analise)
        self.blast_panel.Hide()
        self.Centre()

        self.loading_blast_panel = LoadingBlastPanel(self)
        vbox.Add(self.loading_blast_panel, 1, wx.EXPAND)
        self.loading_blast_panel.btnRun.Bind(wx.EVT_BUTTON, self.open_mapping_panel)
        self.loading_blast_panel.btnReturn.Bind(wx.EVT_BUTTON, self.hide_loading_panel)
        self.loading_blast_panel.btnStop.Bind(wx.EVT_BUTTON, self.stop_blast)
        self.loading_blast_panel.Hide()
        self.Centre()

        self.mapping_panel = MappingPanel(self)
        vbox.Add(self.mapping_panel, 1, wx.EXPAND)
        self.mapping_panel.btnRun.Bind(wx.EVT_BUTTON, self.start_mapping)
        self.mapping_panel.btnReturn.Bind(wx.EVT_BUTTON, self.open_blast_panel)
        self.mapping_panel.btnPrimers.Bind(wx.EVT_BUTTON, self.open_primer_panel)
        self.mapping_panel.Hide()
        self.Centre()

        self.primer_panel = PrimerPanel(self)
        vbox.Add(self.primer_panel, 1, wx.EXPAND)
        self.primer_panel.btnRun.Bind(wx.EVT_BUTTON, self.start_primer_making)
        self.primer_panel.btnReturn.Bind(wx.EVT_BUTTON, self.open_mapping_panel)
        self.primer_panel.Hide()
        self.Centre()

        self.Bind(wx.EVT_CLOSE, self.on_close_window)

    def on_close_window(self, event):
        dial = wx.MessageDialog(None, 'Do you want to exit?', '?',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

    def open_blast_panel(self, event):
        self.blast_panel.Show()
        self.main_panel.Hide()
        self.prepare_panel.Hide()
        self.mapping_panel.Hide()
        self.Layout()

    def open_prepare_panel(self, event):
        self.prepare_panel.Show()
        self.main_panel.Hide()
        self.blast_panel.Hide()
        self.Layout()

    def open_mapping_panel(self, event):
        self.mapping_panel.Show()
        self.primer_panel.Hide()
        self.loading_blast_panel.Hide()
        self.Layout()

    def hide_loading_panel(self, event):
        self.blast_thread.terminate()
        self.loading_blast_panel.Hide()
        self.blast_panel.Show()
        self.Layout()

    def open_primer_panel(self, event):
        self.primer_panel.Show()
        self.main_panel.Hide()
        self.mapping_panel.Hide()
        self.Layout()

    def blast_analise(self, event):
        input_data = self.blast_panel.input.GetValue()
        database = self.blast_panel.database.GetValue()
        output = self.blast_panel.output.GetValue()
        e_value = self.blast_panel.evalue.GetValue()
        num_threads = self.blast_panel.num_threads.GetValue()
        task = self.blast_panel.rbox.GetStringSelection()
        file_format = 'fasta'
        if input_data != '' and database != '' and output != '' and e_value != '' and num_threads != '':
            self.loading_blast_panel.Show()
            self.blast_panel.Hide()
            self.Layout()
            self.blast_thread = Process(
                target=Blast,
                args=(input_data, database, output, file_format, e_value, num_threads, task))
            self.blast_thread.start()

        else:
            wx.MessageDialog(None, 'Not enough data', '', wx.OK).ShowModal()

    def stop_blast(self, event):
        self.blast_thread.terminate()

    def start_mapping(self, event):
        input_file = self.mapping_panel.input.GetValue()
        output_folder = self.mapping_panel.output.GetValue()
        if input_file != '' and output_folder != '':
            GenomeMapping(input_file, output_folder)
        else:
            wx.MessageDialog(None, 'Not enough data', '', wx.OK).ShowModal()

    def start_primer_making(self, event):
        input_file = self.primer_panel.input.GetValue()
        output_folder = self.primer_panel.output.GetValue()
        length = self.primer_panel.length.GetValue()
        opt = self.primer_panel.opt.GetValue()
        min = self.primer_panel.min.GetValue()
        max = self.primer_panel.max.GetValue()
        opt_tm = self.primer_panel.tm_opt.GetValue()
        min_tm = self.primer_panel.tm_min.GetValue()
        max_tm = self.primer_panel.tm_max.GetValue()
        if input_file != '' and output_folder != '' and length != '' and opt != '' and \
                min != '' and opt_tm != '' and min_tm != '' and max_tm != '':
            PrimersMaking(input_file, output_folder, int(length), int(opt), int(min), int(max),
                          float(opt_tm), float(min_tm), float(max_tm))
        else:
            wx.MessageDialog(None, 'Not enough data', '', wx.OK).ShowModal()


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    app = wx.App()
    wnd = MyFrame(None, "S3Finder")
    wnd.Show()
    app.MainLoop()
