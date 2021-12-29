import wx


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        vbox = wx.BoxSizer(wx.VERTICAL)

        vbox.Add(wx.Size(100, 50))
        prepare = wx.BoxSizer(wx.HORIZONTAL, )
        blast = wx.BoxSizer(wx.HORIZONTAL)
        primer = wx.BoxSizer(wx.HORIZONTAL)
        info = wx.BoxSizer(wx.HORIZONTAL)

        vbox.Add(prepare, flag=wx.ALIGN_CENTER)
        vbox.Add(wx.Size(20, 50))
        vbox.Add(blast, flag=wx.ALIGN_CENTER)
        vbox.Add(wx.Size(20, 50))
        vbox.Add(primer, flag=wx.ALIGN_CENTER)
        vbox.Add(wx.Size(40, 50))
        vbox.Add(info, flag=wx.LEFT | wx.BOTTOM)

        self.btn_prepare = wx.Button(self, wx.ID_ANY, label="Step 1: Data preparation")
        self.btn_blast = wx.Button(self, wx.ID_ANY, label="Step 2: Search for species-specific areas")
        self.btn_primer = wx.Button(self, wx.ID_ANY,
                                    label="Step 3: Selection of fragments for the construction of PCR primers")
        btn_info = wx.Button(self, wx.ID_ANY, label='Info')
        btn_info.Bind(wx.EVT_BUTTON, self.get_info)

        prepare.Add(self.btn_prepare)
        blast.Add(self.btn_blast)
        primer.Add(self.btn_primer)
        info.Add(btn_info, flag=wx.ALL, border=8)
        self.SetSizer(vbox)
        self.Layout()

    def get_info(self, event):
        info_window = InfoWindow(parent=wx.Panel(self))
        info_window.Show()


class InfoWindow(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title='Info', size=(600, 450))
        panel = wx.Panel(self)
        text = '\n' + '   At the first step, all genomes of the target genus are downloaded from the NCBI database' + '\n' +\
               '   and two local databases, so called “positive” and “negative” databases, are formed. ' + '\n' + '\n' +\
               '   At the second step, the search for unique sequences is carried out and mapping finding ' + '\n' +\
               '   sequences on target genome. ' + '\n' + '\n' +\
               '   At the last step the program makes primers'
        static_text = wx.StaticText(panel, wx.ID_ANY, label=text, style=wx.ALIGN_LEFT)
        font = wx.Font(14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        static_text.SetFont(font)
