import wx
import wx.html
import webbrowser
import os.path as op

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'No title-Notepad',(400,200),(800,600))#初始化框架
        self.InitUI()# 显示界面
    def InitUI(self):
        self.font = wx.Font(12,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL,faceName="宋体")#设置默认字体
        self.panel = wx.Panel(self)# 创建画板
        # 编辑区
        self.table = wx.TextCtrl(self.panel,style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_RICH)# 多行文本框，水平滚动条
        self.table.SetFont(self.font)# 设置字体
        self.table.Bind(wx.EVT_TEXT,self.Event_text)
        self.table.Bind(wx.EVT_MOUSE_EVENTS,self.Event_mouse)
        # 容器
        vbox = wx.BoxSizer(wx.VERTICAL) # 创建垂直容器
        vbox.Add(self.table, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 0)# 将文本框添加到容器中
        self.panel.SetSizer(vbox) # 设置容器
        # 初始化菜单
        self.InitMenu()
        # 一些全局变量
        self.find_value = ''
        # 初始化打印数据并设置一些默认值
        self.pdata = wx.PrintData()
        self.pdata.SetOrientation(wx.PORTRAIT)
        self.margins = (wx.Point(20, 25), wx.Point(20, 25))  # 页边距
    def InitMenu(self):
        menuBar = wx.MenuBar()# 创建菜单栏
        # 文件菜单
        filemenu = wx.Menu()# 创建一个菜单对象
        New = filemenu.Append(-1,"New(N)\tCtrl+N")# 将子菜单加入到菜单对象中
        Open = filemenu.Append(-1,"Open(O)\tCtrl+O")
        Save = filemenu.Append(-1,"Save(S)\tCtrl+S")
        Save_as = filemenu.Append(-1,"Save as(A)")
        filemenu.AppendSeparator()# 插入一条分割线
        Page_setup = filemenu.Append(-1,"Page setup(U)")
        Print = filemenu.Append(-1,"Print(P)\tCtrl+P")
        filemenu.AppendSeparator()
        Exit = filemenu.Append(-1,"Exit(X)")
        menuBar.Append(filemenu,"File(&F)")# 将File菜单添加到菜单栏
        # 编辑菜单
        self.editmenu = wx.Menu()
        Undo = self.editmenu.Append(2,"Undo(U)\tCtrl+Z")
        wx.Menu.Enable(self.editmenu, 2, False)
        self.editmenu.AppendSeparator()
        Cut = self.editmenu.Append(3,"Cut(T)\tCtrl+X")
        wx.Menu.Enable(self.editmenu, 3, False)
        Copy = self.editmenu.Append(4,"Copy(C)\tCtrl+C")
        wx.Menu.Enable(self.editmenu, 4, False)
        Paste = self.editmenu.Append(9,"Paste(P)\tCtrl+V")
        Delete = self.editmenu.Append(5,"Delete(L)\tDel")
        wx.Menu.Enable(self.editmenu, 5, False)
        self.editmenu.AppendSeparator()
        Find = self.editmenu.Append(6,"Find(F)\tCtrl+F")
        wx.Menu.Enable(self.editmenu, 6, False)
        Find_next = self.editmenu.Append(7,"Find next(N)\tF3")
        wx.Menu.Enable(self.editmenu, 7, False)
        Replace = self.editmenu.Append(-1,"Replace(R)\tCtrl+H")
        Go_to = self.editmenu.Append(8,"Go to(G)\tCtrl+G")
        self.editmenu.AppendSeparator()
        Select_all = self.editmenu.Append(-1,"Select all(A)\tCtrl+A")
        Date_time = self.editmenu.Append(-1,"Date/time(D)\tCtrl+F5")
        menuBar.Append(self.editmenu,"&Edit(E)")
        # 选项菜单
        optionsmenu = wx.Menu()
        self.Wrap = optionsmenu.Append(-1,"Wrap(W)",kind = wx.ITEM_CHECK)# 样式为勾选菜单类型
        Font = optionsmenu.Append(-1,"Font(F)...")
        menuBar.Append(optionsmenu,"&Options(O)")
        # 视图菜单
        self.viewmenu = wx.Menu()
        self.Status = self.viewmenu.Append(1,"Status(S)",kind = wx.ITEM_CHECK)
        menuBar.Append(self.viewmenu,"&View(V)")
        # 帮助菜单
        helpmenu = wx.Menu()
        Check_help = helpmenu.Append(-1,"Check help(H)")
        helpmenu.AppendSeparator()
        About_notepad = helpmenu.Append(-1,"About notepad(A)")
        menuBar.Append(helpmenu,"&Help(H)")
        #设置菜单条
        self.SetMenuBar(menuBar)
        # 绑定菜单事件
        self.Bind(wx.EVT_MENU, self.Event_new, New)
        self.Bind(wx.EVT_MENU, self.Event_open, Open)
        self.Bind(wx.EVT_MENU, self.Event_save, Save)
        self.Bind(wx.EVT_MENU, self.Event_save_as, Save_as)
        self.Bind(wx.EVT_MENU, self.Event_page_setup, Page_setup)
        self.Bind(wx.EVT_MENU, self.Event_print, Print)
        self.Bind(wx.EVT_MENU, self.Event_exit, Exit)
        self.Bind(wx.EVT_MENU, self.Event_undo, Undo)
        self.Bind(wx.EVT_MENU, self.Event_cut, Cut)
        self.Bind(wx.EVT_MENU, self.Event_copy, Copy)
        self.Bind(wx.EVT_MENU, self.Event_paste, Paste)
        self.Bind(wx.EVT_MENU, self.Event_delete, Delete)
        self.Bind(wx.EVT_MENU, self.Event_find, Find)
        self.Bind(wx.EVT_MENU, self.Event_find_next, Find_next)
        self.Bind(wx.EVT_MENU, self.Event_replace, Replace)
        self.Bind(wx.EVT_MENU, self.Event_go_to, Go_to)
        self.Bind(wx.EVT_MENU, self.Event_select_all, Select_all)
        self.Bind(wx.EVT_MENU, self.Event_date_time, Date_time)
        self.Bind(wx.EVT_MENU, self.Event_wrap, self.Wrap)
        self.Bind(wx.EVT_MENU, self.Event_font, Font)
        self.Bind(wx.EVT_MENU, self.Event_status, self.Status)
        self.Bind(wx.EVT_MENU, self.Event_check_help, Check_help)
        self.Bind(wx.EVT_MENU, self.Event_about_notepad, About_notepad)
        # 控制一些菜单
        clipbrd_text = self.Get_clipboard_data()
        if clipbrd_text:
            wx.Menu.Enable(self.editmenu,9,True)
        else:
            wx.Menu.Enable(self.editmenu, 9, False)
    def Event_new(self, event):
        if hasattr(self, 'path') == True:
            if self.IsModified == True:
                dlg = AskDialog(self.path)
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Write_file(self.path)
                    self.New_file()
                elif result == 0:
                    self.New_file()
            else:
                self.New_file()
        else:
            string = self.table.GetValue()
            if string == '':
                self.New_file()
            else:
                dlg = AskDialog('No title')
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Save_file()
                    self.New_file()
                elif result == 0:
                    self.New_file()
    def Event_open(self, event):
        if hasattr(self,'path')==True:
            if self.IsModified == True:
                dlg = AskDialog(self.path)
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Write_file(self.path)
                    self.Open_file()
                elif result == 0:
                    self.Open_file()
            else:
                self.Open_file()
        else:
            string = self.table.GetValue()
            if string == '':
                self.Open_file()
            else:
                dlg = AskDialog('No title')
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Save_file()
                    self.Read_file(self.path)
                    self.table.Bind(wx.EVT_TEXT, self.Event_text2)
                    self.IsModified = False
                elif result == 0:
                    self.Open_file()
    def Event_save(self, event):
        if hasattr(self, 'path') == True:
            self.Write_file(self.path)
        else:
            self.Save_file()
        self.IsModified=False
        self.table.Bind(wx.EVT_TEXT, self.Event_text2)
    def Event_save_as(self, event):
        self.Save_file()
        self.IsModified = False
        self.table.Bind(wx.EVT_TEXT, self.Event_text2)
    def Event_page_setup(self, event):
        data = wx.PageSetupDialogData()
        data.SetPrintData(self.pdata)
        data.SetDefaultMinMargins(True)
        data.SetMarginTopLeft(self.margins[0])
        data.SetMarginBottomRight(self.margins[1])
        dlg = wx.PageSetupDialog(self, data)
        if dlg.ShowModal() == wx.ID_OK:
            data = dlg.GetPageSetupData()
            self.pdata = wx.PrintData(data.GetPrintData())  # 执行一个拷贝
            self.pdata.SetPaperId(data.GetPaperId())
            self.margins = (data.GetMarginTopLeft(), data.GetMarginBottomRight())
        dlg.Destroy()
    def Event_print(self, event):
        data = wx.PrintDialogData(self.pdata)
        printer = wx.Printer(data)
        printout = TextDocPrintout(self.table.GetValue(),self.Title.split('-')[0], self.margins, self.font)
        printer.Print(self, printout, True)# 参数为True，打印之前显示打印对话框
        printout.Destroy()
    def Event_exit(self, event):
        self.Destroy()
    def Event_undo(self, event):
        self.table.Undo()
    def Event_cut(self, event):
        self.table.Cut()
    def Event_copy(self, event):
        self.table.Copy()
    def Event_paste(self, event):
        self.table.Paste()
    def Event_delete(self, event):
        pos = self.table.GetSelection()  # 获得选中部分的索引元组
        self.table.Remove(pos[0], pos[1])  # 根据索引元组删除
    def Event_find(self, event):
        dlg = FindDialog(self.Call,self.Call2,self.find_value)
        dlg.Show()
    def Event_find_next(self, event):
        if self.find_value == '':# 说明没有查找过
            dlg = FindDialog(self.Call, self.Call2, self.find_value)
            dlg.Show()
        else:
            self.table.Bind(wx.EVT_LEFT_UP, self.Event_mouse2)
            end = self.table.GetLastPosition()
            self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
            cursor = self.table.GetInsertionPoint()
            if self.direct == 1:
                string = self.table.GetRange(cursor, end)
            else:
                string = self.table.GetRange(0, cursor)
                string = string[::-1]
            value = self.find_value
            if self.cap == False:
                string = string.lower()
                value = value.lower()
            if value == '':
                pass
            else:
                if self.direct == 0:
                    value = value[::-1]
                index = string.find(value)
                if index == -1:
                    dlg = wx.MessageDialog(self, 'Cannot find the "' + value + '"', 'Notepad')
                    dlg.ShowModal()
                else:
                    if self.direct == 1:
                        self.table.SetStyle(cursor + index, cursor + index + len(value), wx.TextAttr('white', 'blue'))
                        self.table.SetInsertionPoint(cursor + index + len(value))
                    else:
                        self.table.SetStyle(cursor - index - len(value), cursor - index, wx.TextAttr('white', 'blue'))
                        self.table.SetInsertionPoint(cursor - index - len(value))
    def Event_replace(self, event):
        dlg = ReplaceDialog(self.Call,self.Call2,self.find_value)
        dlg.Show()
    def Event_go_to(self, event):
        linum = self.table.GetNumberOfLines()  # 获得所有行数
        pos = self.table.GetInsertionPoint()  # 获得光标所在索引值
        pla = self.table.PositionToXY(pos)  # 索引值转换为行列
        nowline = str(pla[2] + 1)  # 当前行数
        dlg = GotoDialog(linum, nowline)
        if dlg.ShowModal() != wx.ID_CANCEL:
            line = dlg.GetValue() - 1  # 真实行数（从0开始计数）
            pos = self.table.XYToPosition(0, line)  # 行列（列为0）转换为索引值
            self.table.ShowPosition(pos)  # 文本框滚动到索引处
            self.table.SetInsertionPoint(pos)  # 设置光标位于索引处
    def Event_select_all(self, event):
        self.table.SelectAll()
    def Event_date_time(self, event):
        datetime = time.strftime('%H:%M %Y/%m/%d', time.localtime(time.time()))  # 获取时间戳，并格式化
        self.table.WriteText(datetime)  # 在当前光标处插入时间
    def Event_wrap(self, event):
        table_size = self.table.GetSize()
        value = self.table.GetValue()
        self.table.Destroy()
        if self.Wrap.IsChecked():  # 若Wrap菜单处于选中状态
            self.table = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)  # 多行文本框，自动换行
            wx.Menu.Enable(self.viewmenu, 1, False)  # 设置status菜单无效
            wx.Menu.Enable(self.editmenu,8,False)# 转到菜单无效
            if self.Status.IsChecked():# 表示状态栏已经存在
                self.statusbar.Destroy()# 取消状态栏
        else:
            self.table = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.HSCROLL)  # 多行文本框，水平滚动条
            wx.Menu.Enable(self.viewmenu, 1, True)  # 设置status菜单有效
            wx.Menu.Enable(self.editmenu, 8, True)  # 转到菜单无效
        self.table.SetFont(self.font)  # 设置字体
        # 容器
        vbox = wx.BoxSizer(wx.VERTICAL)  # 创建垂直容器
        vbox.Add(self.table, proportion=1, flag=wx.EXPAND | wx.ALL, border=0)  # 将文本框添加到容器中
        self.panel.SetSizer(vbox)  # 设置容器
        self.table.SetSize(table_size)
        self.table.SetValue(value)
    def Event_font(self, event):
        dlg = wx.FontDialog(self, wx.FontData())  # 显示字体对话框
        if dlg.ShowModal() == wx.ID_OK:  # 对话框点击OK按钮
            self.font = dlg.GetFontData().GetChosenFont()  # 获取字体
            self.table.SetFont(self.font)  # 设置文本框字体
        dlg.Destroy()
    def Event_status(self, event):
        if self.Status.IsChecked():
            self.table.Bind(wx.EVT_LEFT_UP,self.Event_key_mouse) # 绑定鼠标抬起事件
            self.table.Bind(wx.EVT_KEY_UP, self.Event_key_mouse)  # 绑定键盘抬起事件
            self.statusbar = self.CreateStatusBar()  # 创建状态栏
            self.statusbar.SetFieldsCount(2)  # 状态栏分为2个区
            self.statusbar.SetStatusWidths([-4, -1])  # 调整分区比例
            self.statusbar.Show()
            self.Set_statustext()
        else:
            self.table.Unbind(wx.EVT_MOTION, handler=self.Event_key_mouse)# 取消绑定事件
            self.table.Unbind(wx.EVT_KEY_UP, handler=self.Event_key_mouse)
            self.statusbar.Destroy()
    def Event_check_help(self, event):
        webbrowser.open('http://www.baidu.com')  # 打开帮助网址
    def Event_about_notepad(self, event):
        dlg = AboutDialog()
        dlg.ShowModal()
        dlg.Destroy()
    def Event_key_mouse(self,event):
        event.Skip()# 加这一句防止鼠标事件影响鼠标的点击
        self.Set_statustext()
    def Event_text(self, event):
        wx.Menu.Enable(self.editmenu, 2, True)
        value = self.table.GetValue()
        if value == '':
            wx.Menu.Enable(self.editmenu, 6, False)
            wx.Menu.Enable(self.editmenu, 7, False)
        else:
            wx.Menu.Enable(self.editmenu, 6, True)
            wx.Menu.Enable(self.editmenu, 7, True)
    def Event_text2(self, event):
        self.IsModified = True
        event.Skip()
    def Event_mouse(self, event):
        event.Skip()
        value = self.table.GetStringSelection()
        if value == '':
            wx.Menu.Enable(self.editmenu, 3, False)
            wx.Menu.Enable(self.editmenu, 4, False)
            wx.Menu.Enable(self.editmenu, 5, False)
        else:
            wx.Menu.Enable(self.editmenu, 3, True)
            wx.Menu.Enable(self.editmenu, 4, True)
            wx.Menu.Enable(self.editmenu, 5, True)
    def Event_mouse2(self,event):
        end = self.table.GetLastPosition()
        self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
        event.Skip()
    def Set_statustext(self):
        pos = self.table.GetInsertionPoint()  # 获得光标索引值
        pla = self.table.PositionToXY(pos)  # 索引值转化为位置
        statu = " row " + str(pla[2] + 1) + ",columm " + str(pla[1] + 1)  # 状态栏显示的信息
        self.statusbar.SetStatusText(statu, 1)  # 设置状态栏显示信息和显示分区
    def Call(self):
        return self.table
    def Call2(self,data):
        self.find_value = data[0]
        self.cap = data[1]
        self.direct = data[2]
    def Read_file(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        self.table.SetValue(data)
    def Write_file(self,path):
        data = self.table.GetValue()
        file = open(path,'w')
        file.write(data)
        file.close()
    def New_file(self):
        self.table.Clear()
        self.SetTitle('No title-Notepad')
    def Open_file(self):
        wildcard = "Text Files(*.txt)|*.txt|All Files (*.*)|*.*"
        # 文件对话框，打开样式，打开上次打开的目录
        dlg = wx.FileDialog(self, 'Open', '', '', wildcard, wx.FD_OPEN | wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()  # 获得文件路径
            self.Read_file(self.path)
            self.table.Bind(wx.EVT_TEXT, self.Event_text2)
            self.SetTitle(op.basename(self.path)+'-Notepad')
            self.IsModified = False
    def Save_file(self):
        wildcard = "Text Files(*.txt)|*.txt|All Files (*.*)|*.*"
        # 文件对话框，保存样式，覆盖文件提示
        dlg = wx.FileDialog(self, 'Save as', '', '', wildcard,
                            wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT | wx.FD_CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.path = dlg.GetPath()
            self.Write_file(self.path)
            self.SetTitle(op.basename(self.path) + '-Notepad')
    def Callback_to_app(self):
        if hasattr(self,'path')==True:
            if self.IsModified == True:
                dlg = AskDialog(self.path)
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Write_file(self.path)
                    self.Destroy()
                elif result == 0:
                    self.Destroy()
            else:
                self.Destroy()
        else:
            string = self.table.GetValue()
            if string == '':
                self.Destroy()
            else:
                dlg = AskDialog('No title')
                result = dlg.ShowModal()
                if result == wx.ID_OK:
                    self.Save_file()
                    self.Destroy()
                elif result == 0:
                    self.Destroy()
    def Get_clipboard_data(self):
        text_data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(text_data)
            wx.TheClipboard.Close()
            if success:
                return text_data.GetText()  # 剪贴板内容
class AskDialog(wx.Dialog):
    def __init__(self, path):
        wx.Dialog.__init__(self, None, -1, 'Notepad', size=(364, 143))
        panel = wx.Panel(self, size=(364, 60))
        panel.SetBackgroundColour('white')
        text = wx.StaticText(panel, -1, "Save the Change to " + path + "?",(10, 20))
        bt_save = wx.Button(self, wx.ID_OK, 'Save(S)', (87, 70), (76, 26))
        bt_save.SetDefault()
        bt_ntsave = wx.Button(self, -1, "Not save(N)", (168, 70), (90, 26))
        bt_ntsave.Bind(wx.EVT_BUTTON, self.Event_ntsave)
        bt_cancel = wx.Button(self, wx.ID_CANCEL, 'Cancel', (263, 70), (76, 26))
        self.Center()
    def Event_ntsave(self,event):
        self.Destroy()
class FindDialog(wx.Dialog):
    def __init__(self,call,call2,find_value):
        wx.Dialog.__init__(self,None,-1,"Find",size=(430, 170))
        text = wx.StaticText(self,-1,"FindContent:",(5, 15))
        self.tc = wx.TextCtrl(self,-1,find_value,(84, 15),(223, 25),wx.TE_PROCESS_ENTER)
        self.tc.Bind(wx.EVT_TEXT_ENTER,self.Event_fdnt)
        self.tc.Bind(wx.EVT_TEXT, self.Event_checkvalue)
        self.bt_fdnt = wx.Button(self,-1,"FindNext(F)",(320, 12),(88, 30))
        self.bt_fdnt.Bind(wx.EVT_BUTTON, self.Event_fdnt)
        self.bt_fdnt.SetDefault()
        bt_cancel = wx.Button(self,wx.ID_CANCEL, "Cancel", (320, 48), (88, 30))
        self.cb = wx.CheckBox(self,-1,'Case sensitive(C)',(5, 93))
        self.rb = wx.RadioBox(self,-1,"Direction",(172, 55),(135, 60),["Up(U)", "Down(D)"],2,wx.RA_SPECIFY_COLS)
        self.rb.SetSelection(1)
        self.call = call
        self.call2 = call2
        if self.tc.GetValue()=='':
            self.bt_fdnt.Disable()
    def Event_checkvalue(self,event):
        value = self.tc.GetValue()
        if value == '':
            self.bt_fdnt.Disable()
        else:
            self.bt_fdnt.Enable()
    def Event_fdnt(self,event):
        cap = self.cb.GetValue()
        direct = self.rb.GetSelection()
        self.table = self.call()
        self.table.Bind(wx.EVT_SET_FOCUS,self.Event_getfocus)
        end = self.table.GetLastPosition()
        self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
        cursor = self.table.GetInsertionPoint()
        if direct == 1:
            string = self.table.GetRange(cursor,end)
        else:
            string = self.table.GetRange(0,cursor)
            string = string[::-1]
        value = self.tc.GetValue()
        self.call2((value,cap,direct))
        if cap == False:
            string = string.lower()
            value = value.lower()
        if value == '':
            pass
        else:
            if direct == 0:
                value = value[::-1]
            index = string.find(value)
            if index == -1:
                dlg = wx.MessageDialog(self,'Cannot find the "'+value+'"','Notepad')
                dlg.ShowModal()
            else:
                if direct == 1:
                    self.table.SetStyle(cursor + index, cursor + index + len(value), wx.TextAttr('white', 'blue'))
                    self.table.SetInsertionPoint(cursor + index + len(value))
                else:
                    self.table.SetStyle(cursor - index - len(value), cursor - index, wx.TextAttr('white', 'blue'))
                    self.table.SetInsertionPoint(cursor - index - len(value))
    def Event_getfocus(self,event):
        end = self.table.GetLastPosition()
        self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
        event.Skip()
class ReplaceDialog(wx.Dialog):
    def __init__(self,call,call2,find_value):
        wx.Dialog.__init__(self,None,-1,"Replace",size=(420,238))
        self.text1 = wx.StaticText(self,-1,"FindContent(N):",(5,20))
        self.text2 = wx.StaticText(self,-1,"ReplaceTo(P):",(5,55))
        self.tc1 = wx.TextCtrl(self,-1,find_value,(95,15),(200,25))
        self.tc1.Bind(wx.EVT_TEXT,self.Event_text)
        self.tc2 = wx.TextCtrl(self,pos=(95,50),size=(200,25))
        self.bt_fdnt = wx.Button(self,-1,"FindNext(F)",(305,8),(88,30))
        self.bt_fdnt.Bind(wx.EVT_BUTTON,self.Event_fdnt)
        self.bt_fdnt.SetDefault()
        self.bt_repl = wx.Button(self,-1,"Replace(R)",(305,43),(88,30))
        self.bt_repl.Bind(wx.EVT_BUTTON,self.Event_repl)
        self.bt_real = wx.Button(self,-1,"ReplaceAll(A)",(305,78),(88,30))
        self.bt_real.Bind(wx.EVT_BUTTON,self.Event_real)
        bt_cancel = wx.Button(self,wx.ID_CANCEL,"Cancel",(305,113),(88,30))
        self.cb = wx.CheckBox(self,-1,'Case sensitive(C)',(8,134))
        self.call = call
        self.call2 = call2
        if self.tc1.GetValue()=='':
            self.bt_fdnt.Disable()
            self.bt_repl.Disable()
            self.bt_real.Disable()
    def Event_text(self,event):
        if self.tc1.GetValue() == '':
            self.bt_fdnt.Disable()
            self.bt_repl.Disable()
            self.bt_real.Disable()
        else:
            self.bt_fdnt.Enable()
            self.bt_repl.Enable()
            self.bt_real.Enable()
    def Event_fdnt(self,event):
        self.Find()
    def Event_repl(self,event):
        value = self.tc2.GetValue()
        if hasattr(self,'table')==True:
            self.table.Replace(self.pos_start,self.pos_end,value)
        self.Find()
    def Event_real(self,event):
        self.table = self.call()
        string = self.table.GetValue()
        value = self.tc1.GetValue()
        value2 = self.tc2.GetValue()
        self.table.SetValue(string.replace(value,value2))
    def Event_getfocus(self,event):
        end = self.table.GetLastPosition()
        self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
        event.Skip()
    def Find(self):
        cap = self.cb.GetValue()
        self.table = self.call()
        self.table.Bind(wx.EVT_SET_FOCUS, self.Event_getfocus)
        end = self.table.GetLastPosition()
        self.table.SetStyle(0, end, wx.TextAttr('black', 'white'))
        cursor = self.table.GetInsertionPoint()
        string = self.table.GetRange(cursor, end)
        value = self.tc1.GetValue()
        self.call2((value, cap, 1))
        if cap == False:
            string = string.lower()
            value = value.lower()
        if value == '':
            pass
        else:
            index = string.find(value)
            if index == -1:
                dlg = wx.MessageDialog(self, 'Cannot find the "' + value + '"', 'Notepad')
                dlg.ShowModal()
            else:
                self.pos_start = cursor + index
                self.pos_end = cursor + index + len(value)
                self.table.SetStyle(cursor + index, cursor + index + len(value), wx.TextAttr('white', 'blue'))
                self.table.SetInsertionPoint(cursor + index + len(value))
class GotoDialog(wx.Dialog):
    def __init__(self, linum, nowline):
        wx.Dialog.__init__(self,None,-1,"Go to the line",size=(306, 167))
        self.nowline = nowline
        self.linum = linum
        text = wx.StaticText(self, label="Line number(L):", pos=(15, 15))
        self.tc = wx.TextCtrl(self, -1, self.nowline, (15, 38), (260, 30), wx.TE_PROCESS_ENTER, CharValidator())
        self.tc.Bind(wx.EVT_TEXT_ENTER, self.Event_confirm)
        bt_confirm = wx.Button(self,label="Goto", pos=(95, 84), size=(90, 30))
        bt_confirm.Bind(wx.EVT_BUTTON, self.Event_confirm)
        bt_confirm.SetDefault()
        bt_cancel = wx.Button(self, wx.ID_CANCEL,"Cancel",(190, 84),(90, 30))
    def GetValue(self):
        return self.value
    def Event_confirm(self,event):
        value = self.tc.GetValue()
        value = int(value)
        if 0 < value <= self.linum:
            self.value = value
            self.Destroy()
        else:
            dlg = JumpDialog()
            if dlg.ShowModal() == wx.ID_OK:
                self.value = str(self.linum)
                self.tc.SetValue(self.value)
                self.tc.SetFocus()
                pos = self.tc.GetLastPosition()
                self.tc.SetSelection(0, pos)
class JumpDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Notepad-Jump line", size=(154, 163))
        panel = wx.Panel(self,size=(154, 70))
        panel.SetBackgroundColour("white")
        text = wx.StaticText(panel,-1,"Line number out",(10, 20))
        bt_ok = wx.Button(self,wx.ID_OK,"OK",(32, 85),(90, 30))
class AboutDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self,None,-1,'About Notepad',size=(548, 504))
        html = HtmlWindow(self)
        html.SetPage('<br><br><br><br><br><br><br><br><br><br><br><br>'
                     '<br><br><br><br><br><br><br><br><br><br><br><br>'
                     '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                     '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
                     '&nbsp;<a href="#">许可条款</a>')
class CharValidator(wx.Validator):
    def __init__(self):
        wx.Validator.__init__(self)
        self.Bind(wx.EVT_CHAR, self.OnChar)  # 绑定字符事件
    def Clone(self):
        return CharValidator()
    def TransferToWindow(self):
        return True
    def OnChar(self, evt):  # 数据处理
        keycode = evt.GetKeyCode()
        if keycode <48:
            if keycode !=8 and keycode !=13:
                return
        elif keycode >57:
            return
        evt.Skip()
class TextDocPrintout(wx.Printout):
    def __init__(self, text, title, margins,font):
        wx.Printout.__init__(self, title)
        self.lines = text.split('\n')# 打印内容所有行的列表
        self.margins = margins
        self.title = title
        self.font = font
    def HasPage(self, page):
        # 这一个方法没有会导致只有1页
        return True
    def GetPageInfo(self):
        return (1, self.numPages, 1, self.numPages)
    def CalculateScale(self, dc):
        # 调整DC比例，直到打印输出大致与屏幕比例相同。
        ppiPrinterX, ppiPrinterY = self.GetPPIPrinter()
        ppiScreenX, ppiScreenY = self.GetPPIScreen()
        logScale = float(ppiPrinterX)/float(ppiScreenX)

        # 如果页面宽度==DC宽度那么不变，否则我们调小DC尺寸。
        pw, ph = self.GetPageSizePixels()
        dw, dh = dc.GetSize()
        scale = logScale *float(dw)/float(pw)

        # 设置DC的范围
        dc.SetUserScale(scale, scale)

        # 找到每毫米的逻辑单元（用来计算空白）
        self.logUnitsMM = float(ppiPrinterX)/(logScale*25.4)
    def CalculateLayout(self, dc):
        # 检测边距位置和页面/行高
        topLeft, bottomRight = self.margins
        dw, dh = dc.GetSize()
        self.x1 = topLeft.x * self.logUnitsMM
        self.y1 = topLeft.y * self.logUnitsMM
        self.x2 = dc.DeviceToLogicalXRel(dw) - bottomRight.x * self.logUnitsMM
        self.y2 = dc.DeviceToLogicalYRel(dh) - bottomRight.y * self.logUnitsMM

        # 沿着盒子内侧使用1mm的缓存，在每条线里添加一点像素
        self.pageHeight = self.y2 - self.y1 - 2*self.logUnitsMM
        self.pageWidth = self.x2 - self.x1 - 2*self.logUnitsMM
        dc.SetFont(self.font)
        self.lineHeight = dc.GetCharHeight()
        self.CharWidth = dc.GetCharWidth()
        self.maxlength = int(self.pageWidth/self.CharWidth)
        self.linesPerPage = int(self.pageHeight/self.lineHeight)-3#这个控制一页内行的数量
    def Recursion(self,string,limit,temp=[]):
        byte_len = 0
        for i, j in enumerate(string):
            if len(j.encode('utf-8')) == 1:
                byte_len += 1
            else:
                byte_len += 2
            if byte_len > limit:
                temp.append(string[:i])
                return self.Recursion(string[i:], limit)
        if byte_len <= limit:
            temp.append(string)
            return temp
    def OnPreparePrinting(self):
        # 计算页码数
        dc = self.GetDC()
        self.CalculateScale(dc)
        self.CalculateLayout(dc)
        new_list = []
        for i in self.lines:
            temp = self.Recursion(i, self.maxlength)
        new_list.extend(temp)
        self.lines = new_list
        self.numPages = len(self.lines) / self.linesPerPage# 最终页码数
        if len(self.lines) % self.linesPerPage != 0:
            self.numPages += 1
    def Get_string_lenth(self,string):
        '''返回字符串所包含的字节实际长度'''
        byte_num = 0
        for i in string:
            if len(i.encode('utf-8')) == 1:
                byte_num += 1
            else:
                byte_num += 2
        byte_length = byte_num * self.CharWidth
        return byte_length
    def OnPrintPage(self, page):
        dc = self.GetDC()
        self.CalculateScale(dc)
        self.CalculateLayout(dc)
        # 画出页面中的文本线
        line = (page-1) * self.linesPerPage
        x = self.x1 + self.logUnitsMM
        y = self.y1 + self.logUnitsMM
        y_end = y+self.lineHeight*(self.linesPerPage+2)
        footer = '第' + str(page) + '页'
        title_length = self.Get_string_lenth(self.title)
        footer_length = self.Get_string_lenth(footer)
        x_title = (self.x2-self.x1)/2+self.x1-title_length/2
        x_footer = (self.x2-self.x1)/2+self.x1-footer_length/2
        dc.DrawText(self.title, x_title, y)
        y += self.lineHeight
        while line < (page * self.linesPerPage):
            dc.DrawText(self.lines[line], x, y)
            y += self.lineHeight
            line += 1
            if line >= len(self.lines):
                break
        dc.DrawText(footer,x_footer,y_end)
        return True
class HtmlWindow(wx.html.HtmlWindow):
    def __init__(self,parent):
        wx.html.HtmlWindow.__init__(self,parent,-1,style=wx.html.HW_NO_SELECTION)
        bt_confirm = wx.Button(self, wx.ID_OK, "Confirm", (435, 425), (90, 30))
        line = wx.StaticLine(self, -1, (20, 85), (495, 2))  # 分割线
        text = wx.StaticText(self, -1, "XNotepad", (60, 105))
        text = wx.StaticText(self, -1, "版本 2.7.0", (60, 125))
    def OnLinkClicked(self,link):
        webbrowser.open('http://www.baidu.com')
class MainApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        self.frame.Bind(wx.EVT_CLOSE,self.OnClose,self.frame)
        self.frame.Show()
        return 1
    def OnClose(self,event):
        self.frame.Callback_to_app()

def main():
    app = MainApp()
    app.MainLoop()
