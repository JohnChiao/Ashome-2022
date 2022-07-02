# 三个菜单：文件，编辑和关于
# 文件：新建、打开、保存和另存为
# 编辑：撤销，重做，复制，剪切，粘贴，查找和全选
# 关于：作者和版权
import wx
import os
import os.path
import sys
import win32ui
import re


class Notepad(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent=parent, id=wx.NewId(), title="笔记本",
                          pos=wx.Point(250, 100), size=(800, 550),
                          style=wx.DEFAULT_FRAME_STYLE, name="Notepad")
        self.panel = wx.Panel(self)
        # 显示菜单栏
        self.menuBar = wx.MenuBar()
        self.showMenuFile()
        self.showMenuEdit()
        self.showMenuAbout()
        self.SetMenuBar(self.menuBar)
        # 显示文本域，暂时隐藏，需要的时候才显示
        self.textArea = self.showTextArea()
        # 正在操作的文件的完整路径
        self.pathname = ""

    # 显示文本域
    def showTextArea(self):
        area = wx.TextCtrl(self.panel, -1, style=wx.TE_MULTILINE)
        area.Size = (800-17, 550-55)
        self.panel.Bind(wx.EVT_SIZE, self.sizeChange)
        area.Hide()
        return area

    # 菜单栏的“文件”
    def showMenuFile(self):
        # 按钮
        menu = wx.Menu()
        create = menu.Append(101, "Create...")
        self.Bind(wx.EVT_MENU, self.createFile, create)
        menu.AppendSeparator()
        opn = menu.Append(102, "Open...")
        self.Bind(wx.EVT_MENU, self.openFile, opn)
        menu.AppendSeparator()
        save = menu.Append(103, "Save")
        self.Bind(wx.EVT_MENU, self.saveFile, save)
        menu.AppendSeparator()
        saveAs = menu.Append(104, "Save As...")
        self.Bind(wx.EVT_MENU, self.saveFileAs, saveAs)
        menu.AppendSeparator()
        exitSystem = menu.Append(105, "Exit")
        self.Bind(wx.EVT_MENU, self.exitSystem, exitSystem)
        self.menuBar.Append(menu, "&File")

    # 菜单栏的“编辑”
    def showMenuEdit(self):
        # 撤销，重做，复制，剪切，粘贴，查找和全选
        menu = wx.Menu()
        undo = menu.Append(201, "Undo")
        self.Bind(wx.EVT_MENU, self.undo, undo)
        menu.AppendSeparator()
        redo = menu.Append(202, "Redo")
        self.Bind(wx.EVT_MENU, self.redo, redo)
        menu.AppendSeparator()
        copy = menu.Append(203, "Copy")
        self.Bind(wx.EVT_MENU, self.copy, copy)
        menu.AppendSeparator()
        cut = menu.Append(204, "Cut")
        self.Bind(wx.EVT_MENU, self.cut, cut)
        menu.AppendSeparator()
        paste = menu.Append(205, "Paste")
        self.Bind(wx.EVT_MENU, self.paste, paste)
        menu.AppendSeparator()
        search = menu.Append(206, "Search...")
        self.Bind(wx.EVT_MENU, self.search, search)
        menu.AppendSeparator()
        selectAll = menu.Append(207, "Select All")
        self.Bind(wx.EVT_MENU, self.selectAll, selectAll)
        self.menuBar.Append(menu, "&Edit")

    # 菜单栏的“关于”
    def showMenuAbout(self):
        # 作者和版权
        menu = wx.Menu()
        authorAndCopyright = menu.Append(301, "Author And Copyright")
        self.Bind(wx.EVT_MENU, self.authorAndCopyright, authorAndCopyright)
        self.menuBar.Append(menu, "&About")

    # 窗口大小改变的时候触发的事件
    def sizeChange(self, e):
        self.textArea.SetSize((e.GetSize().width, e.GetSize().height))

    # 创建新文件
    def createFile(self, e):
        self.pathname = ""
        self.textArea.Clear()
        self.textArea.Show()

    # 打开文件
    def openFile(self, e):
        dlg = win32ui.CreateFileDialog(1)
        dlg.SetOFNInitialDir(sys.path[0])
        dlg.DoModal()
        self.pathname = dlg.GetPathName()
        if "" == self.pathname:
            return;
        self.textArea.Show()
        with open(self.pathname, "rb+") as f:
            self.textArea.Clear()
            line = f.readline()
            while line:
                self.textArea.AppendText(line.decode())
                line = f.readline()
            f.close()

    # 保存文件
    def saveFile(self, e):
        if "" == self.pathname:
            self.saveFileAs(None)
            return
        with open(self.pathname, "rb+") as f:
            f.write(self.textArea.GetValue().encode())
            f.truncate()    # 去掉多余的部分
            f.close()
            wx.MessageBox("保存成功！", "提示信息")
            return
        wx.MessageBox("保存失败！", "提示信息")

    # 将文件另存为
    def saveFileAs(self, e):
        dlg = win32ui.CreateFileDialog(0)
        dlg.SetOFNInitialDir(sys.path[0])
        flag = dlg.DoModal()
        if 1 == flag:       # 点击“保存”按钮的时候
            self.pathname = dlg.GetPathName()
            if not os.path.exists(self.pathname):
                open(self.pathname, "w").close()     # 新建文件
            self.saveFile(None)

    # 退出笔记本
    def exitSystem(self, e):
        self.Close()

    # 撤销（只撤销一步）
    def undo(self, e):
        self.textArea.Undo()

    # 重做（只重做一步）
    def redo(self, e):
        self.textArea.Redo()

    # 复制（选中）
    def copy(self, e):
        self.textArea.Copy()

    # 剪切（选中）
    def cut(self, e):
        self.textArea.Cut()

    # 粘贴
    def paste(self, e):
        self.textArea.Paste()

    # 查询
    def search(self, e):
        dlg = wx.TextEntryDialog(None, "Please input the text witch you would like to search for ", "Search...")
        flag = dlg.ShowModal()
        if wx.ID_OK == flag:
            val = dlg.GetValue()
            if "" != val:
                wx.MessageBox("与“" + val + "”相匹配的有" + str(len(re.findall(val, self.textArea.GetValue()))) + "个")

    # 选择全部
    def selectAll(self, e):
        self.textArea.SelectAll()

    # 作者和版权
    def authorAndCopyright(self, e):
        win32ui.MessageBox("Author: John Chiao", "Author And Copyright")

def main():
    app = wx.App()
    pad = Notepad(None)
    pad.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()

