import wx
import os


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400, 600))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()  # 创建位于窗口的底部的状态栏

        # 设置菜单
        filemenu = wx.Menu()
        menufile = filemenu.Append(wx.ID_OPEN, '文件', '选择文件')
        menuSave = filemenu.Append(wx.ID_SAVE, '保存', '保存文件')
        menuNew = filemenu.Append(wx.ID_NEW, '新建', '新建文件')
        menuAbout = filemenu.Append(wx.ID_ABOUT, '关于', '关于程序的信息')
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT, '退出', '终止应用程序')

        # 创建菜单栏
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, '文件')  # 在菜单栏添加菜单
        self.SetMenuBar(menuBar)  # 在frame中添加菜单栏

        # 设置events
        self.Bind(wx.EVT_MENU, self.OnOpen, menufile)
        self.Bind(wx.EVT_MENU, self.OnSave, menuSave)
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "一个小的文本编辑器.",
                               "关于编辑器", wx.OK)  # 语法是（self,内容，标题，id） #这里加不加wx.ok都是一样的效果
        dlg.ShowModal()  # 显示对话框
        dlg.Destroy()  # 当结束之后关闭对话框

    def OnExit(self, e):
        self.Close(True)  # 关闭整个frame

    def OnOpen(self, e):
        """打开一个文件"""
        self.dirname = ""
        dlg = wx.FileDialog(self, "选择一个文件", self.dirname,
                            "", "*.*", wx.FD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

    def OnNew(self, e):
        dlg = wx.TextEntryDialog(self, '输入文件名', '新建文件')
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetValue() + '.txt'
            file = open(self.filename, 'w+')
            file.write(self.control.GetValue())
            file.close()

    def OnSave(self, e):
        """保存一个文件"""
        try:
            file = open(self.filename, 'w')
            file.write(self.control.GetValue())
            file.close()
        except:
            dlg = wx.TextEntryDialog(self, '输入文件名', '新建文件')
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetValue() + '.txt'
                file = open(filename, 'w+')
                file.write(self.control.GetValue())
                file.close()


app = wx.App(False)
frame = MainWindow(None, "记事本")
app.MainLoop()
