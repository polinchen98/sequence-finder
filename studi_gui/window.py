import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))
        # общий сайзер с виджетами по вертикали
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        btnOk = wx.Button(panel, label='RUN', size=(70, 30))
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(btnOk, flag=wx.LEFT, border=10)
        vbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?', 'Вопрос',
                     wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()


app = wx.App()
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()
