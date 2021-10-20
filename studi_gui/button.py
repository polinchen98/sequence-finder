import wx

BOTTON1 = 1
BOTTON2 = 2
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        panel = wx.Panel(self)
        btn = wx.Button(panel, wx.ID_ANY, "Нажать")

        btn.Bind(wx.EVT_BUTTON, self.onButton)
        panel.Bind(wx.EVT_BUTTON, self.onButtonPanel)
        self.Bind(wx.EVT_BUTTON, self.onButtonFrame)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def onButton(self, event):
        print("Уровень кнопки")
        event.Skip()

    def onButtonPanel(self, event):
        print("Уровень панели")
        event.Skip()

    def onButtonFrame(self, event):
        print("Уровень окна")

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
