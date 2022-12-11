from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os
from PIL import Image, ImageTk
from threading import Thread
class Application_UI(object):
    path = os.path.abspath(".")
    file_types = [".png", ".jpg", ".jpeg", ".ico", ".gif"]
    scroll_visiblity = True
    font = 11
    font_type = "Courier New"

    def __init__(self):

        # 设置UI界面

        window = Tk()

        self.root = window

        win_width = 800

        win_height = 600

        screen_width, screen_height = window.maxsize()

        x = int((screen_width - win_width) / 2)

        y = int((screen_height - win_height) / 2)

        window.title("文件管理工具")

        window.geometry("%sx%s+%s+%s" % (win_width, win_height, x, y))

        menu = Menu(window)

        window.config(menu = menu)

        selct_path = Menu(menu, tearoff = 0)

        selct_path.add_command(label = "打开", accelerator="Ctrl + O", command = self.open_dir)

        selct_path.add_command(label = "保存", accelerator="Ctrl + S", command = self.save_file)

        menu.add_cascade(label = "文件", menu = selct_path)

        about = Menu(menu, tearoff = 0)

        about.add_command(label = "版本", accelerator = "v1.0.0")

        about.add_command(label = "作者", accelerator = "样子")

        menu.add_cascade(label = "关于", menu = about)

        # 顶部frame

        top_frame = Frame(window, bg = "#fff")

        top_frame.pack(side = TOP, fill = X)

        label = Label(top_frame, text = "当前选中路径：", bg = "#fff")

        label.pack(side = LEFT)

        self.path_var = StringVar()

        self.path_var.set("无")

        label_path = Label(top_frame, textvariable = self.path_var, bg = "#fff", fg = "red", height = 2)

        label_path.pack(anchor = W)

        paned_window = PanedWindow(window, showhandle = False, orient=HORIZONTAL)

        paned_window.pack(expand = 1, fill = BOTH)

        # 左侧frame

        self.left_frame = Frame(paned_window)

        paned_window.add(self.left_frame)

        self.tree = ttk.Treeview(self.left_frame, show = "tree", selectmode = "browse")

        tree_y_scroll_bar = Scrollbar(self.left_frame, command = self.tree.yview, relief = SUNKEN, width = 2)

        tree_y_scroll_bar.pack(side = RIGHT, fill = Y)

        self.tree.config(yscrollcommand = tree_y_scroll_bar.set)

        self.tree.pack(expand = 1, fill = BOTH)

        # 右侧frame

        right_frame = Frame(paned_window)

        paned_window.add(right_frame)

        # 右上角frame

        right_top_frame = Frame(right_frame)

        right_top_frame.pack(expand = 1, fill = BOTH)

        self.number_line = Text(right_top_frame, width = 0, takefocus = 0, border = 0, font = (self.font_type, self.font), cursor = "")

        self.number_line.pack(side = LEFT, fill = Y)

        # 右上角Text

        text = Text(right_top_frame, font = (self.font_type, self.font), state = DISABLED, cursor = "", wrap = NONE)

        self.text_obj = text

        text_x_scroll = Scrollbar(right_frame, command = text.xview, orient = HORIZONTAL)

        text_y_scroll = Scrollbar(right_top_frame, command = text.yview)

        self.text_scroll_obj = text_y_scroll

        text.config(xscrollcommand = text_x_scroll.set, yscrollcommand = text_y_scroll.set)

        text_y_scroll.pack(side = RIGHT, fill = Y)

        text_x_scroll.pack(side = BOTTOM, fill = X)

        text.pack(expand = 1, fill = BOTH)

        # 右下角frame

        right_bottom_frame = Frame(right_frame)

        right_bottom_frame.pack(side = BOTTOM, fill = X)

        self.folder_img = PhotoImage(file = r"./image/folder.png")

        self.file_img = PhotoImage(file = r"./image/text_file.png")

        php_img = PhotoImage(file = r"./image/php.png")

        python_img = PhotoImage(file = r"./image/python.png")

        image_img = PhotoImage(file = r"./image/img.png")

        # 设置文件图标

        self.icon = {".php": php_img, ".py": python_img, ".pyc": python_img, ".png": image_img, ".jpg": image_img, ".jpeg": image_img, ".gif": image_img, ".ico": image_img}

        # 加载目录文件

        self.load_tree("", self.path)

        self.tree.bind("<>", lambda event: self.select_tree())

        text.bind("", lambda event : self.update_line())

        self.number_line.bind("", self.focus_in_event)

        self.number_line.bind('', self.button_ignore)

        self.number_line.bind('', self.button_ignore)

        self.number_line.bind('', self.button_ignore)

        self.number_line.bind('', self.button_ignore)

        self.number_line.bind('', self.button_ignore)

        self.number_line.bind('', self.button_ignore)

        self.text_scroll_obj.bind('', lambda event: self.update_line())

        self.text_obj.bind('', lambda event: self.update_line())

        text.bind("", lambda event: self.save_file())
        text.bind("", lambda event: self.save_file())
        text.bind("", lambda event: self.toUndo())
        text.bind("", lambda event: self.toRedo())
window.mainloop()
