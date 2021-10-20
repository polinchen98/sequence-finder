import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600,700))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("js.jpg"))
        img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("python.png"))
        vbox.Add(img1, wx.ID_ANY, wx.EXPAND)
        vbox.Add(img2, wx.ID_ANY, wx.EXPAND)

        mp = wx.Panel(panel)
        mp.SetBackgroundColour('#FFFFE5')
        vbox.Add(mp, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

        panel.SetSizer(vbox)

app = wx.App()
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
