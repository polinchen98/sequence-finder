import wx

APP_EXIT = 1


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        it_min = self.Append(wx.ID_ANY, 'Минимизировать')
        it_max = self.Append(wx.ID_ANY, 'Распахнуть')
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)

    def onMinimize(self, event):
        self.parent.Iconize()

    def onMaximize(self, event):
        self.parent.Maximize()


class MyFrame(wx.Frame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')
        fileMenu.AppendSeparator()
        item = wx.MenuItem(fileMenu, APP_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        fileMenu.Append(item)
        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.onQuit, id=APP_EXIT)

        self.ctx = AppContextMenu(self)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, 'Выход', wx.Bitmap())
        toolbar.Realize()

    def OnRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition()) #MouseEvent

    def onQuit(self, event):
        self.Close()


app = wx.App()
wnd = MyFrame(None, "Hello World!")
wnd.Show()
app.MainLoop()

