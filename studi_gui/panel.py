import wx


class Glowne(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        # self.SetSize((800, 600))

        font = wx.Font(18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        wx.StaticText(self, wx.ID_ANY, 'HELLO', (350, 10))
        self.SetFont(font)

        self.btn = wx.Button(self, wx.ID_ANY, "Change panel", (345, 100))


class Glowne1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        # self.SetSize((800, 600))

        font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        statictext = wx.StaticText(self, wx.ID_ANY, 'Panel 2', (300, 10))
        statictext.SetFont(font)
        self.btn = wx.Button(self, wx.ID_ANY, "Change panel1", (345, 100))


class Program(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, 'Program')

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        self.panel_one = Glowne(self)
        sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.panel_one.btn.Bind(wx.EVT_BUTTON, self.show_panel_two)

        self.panel_two = Glowne1(self)
        sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.panel_two.btn.Bind(wx.EVT_BUTTON, self.show_panel_one)
        self.panel_two.Hide()
        self.SetSize((800, 600))
        self.Centre()

    def show_panel_one(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.Layout()

    def show_panel_two(self, event):
        self.panel_two.Show()
        self.panel_one.Hide()
        self.Layout()


# if __name__ == "__main__":
app = wx.App(False)
frame = Program()
frame.Show()
app.MainLoop()
