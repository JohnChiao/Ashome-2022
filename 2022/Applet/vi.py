from tkinter import *  # �ؼ��������������������������µ����к�������ֱ�ӵ���
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from urllib.parse import quote

class MainWindow():
    # ��ʼ��
    def __init__(self):
        top_button_width = 10 #�������ð�ť���
        button_relief = RAISED #��������ͼ��Ч����������Ϊ͹��

        # �������㴰��
        root = Tk()
        self.src_filename = None
        self.count = StringVar()
        self.count.set('0')
        root.title('Notebook')
        # ������Ϊ���ɱ�,Ĭ��ΪTrue
        root.resizable(width=False, height=False)

        # �ϲ��ؼ�
        Button(root, text='Open file', relief=button_relief, width=top_button_width, command=self.open_button_event).grid(row=0, column=0)
        Button(root, text='New text file', relief=button_relief, width=top_button_width, command=self.new_button_event).grid(row=0, column=1)
        Button(root, text='Save', relief=button_relief, width=top_button_width,
               command=self.save_button_event).grid(row=0, column=3)
        Button(root, text='Save as...', relief=button_relief, width=top_button_width,
               command=self.other_save_button_event).grid(row=0, column=4)
        Button(root, text='clear this file', width=top_button_width, command=self.clear_button).grid(row=0, column=5)

        # ��һ��
        Label(root, text='').grid(row=1)

        # ���ؼ�
        Button(root, text='Find', relief=button_relief, width=top_button_width, command=self.find_button_event) \
            .grid(row=2, column=0, sticky=N)
        self.find_text = Text(root, width=top_button_width, height=2)
        self.find_text.grid(row=2, column=1)
        Label(root, text='Count:').grid(row=3, column=0, sticky=N)
        self.count_label = Label(root, textvariable=self.count)
        self.count_label.grid(row=3, column=1)
        Button(root, text='Replace:', relief=button_relief, width=top_button_width, command=self.replace_button_event).grid(
            row=4, column=0, sticky=N)
        self.replace_text = Text(root, width=top_button_width, height=2)
        self.replace_text.grid(row=4, column=1, sticky=N)
        Button(root, text='Uppercase', relief=button_relief, width=top_button_width, command=self.upper_button_event).grid(
            row=5, column=0, sticky=N)
        Button(root, text='Lowercase', relief=button_relief, width=top_button_width, command=self.lower_button_event).grid(
            row=5, column=1, sticky=N)
        #�Ҳ��ı���
        self.text = Text(root)
        self.text.grid(row=2, column=2, columnspan=6, rowspan=15)
    #��
    def open_button_event(self):
        self.new_button_event()
        # ��ȡ�ļ���
        self.src_filename = filedialog.askopenfilename(filetypes=[('Text file', 'txt'), ('All file', '*')])
        if self.src_filename:
            # ��ȡ����
            data = open(self.src_filename).read()
            # ��䵽text�ؼ�
            #self.text.delete(1.0, END)
            self.text.insert(INSERT, data)
    #�½�
    def new_button_event(self):
        data = self.__get()
        if data and messagebox.askokcancel('Notebook', 'Save this file?'):
            if self.src_filename:
                self.__sava_data(self.src_filename)
            else:
                self.other_save_button_event()
        self.text.delete(1.0, END)
    #���水ť
    def save_button_event(self):
        filename = self.src_filename if self.src_filename else filedialog.askopenfilename(filetypes=[('Text file', 'txt'), ('All file', '*')])
        if filename:
            self.__sava_data(filename)
    #���Ϊ
    def other_save_button_event(self):
        f = filedialog.asksaveasfile(filetypes=[('Text file', 'txt'), ('All file', '*')])
        if f:
            f.write(self.__get())
    #����
    def find_button_event(self):
        data = self.__get()
        find_data = self.find_text.get(1.0, END).strip()
        if find_data not in data:
            messagebox.showinfo('Error', 'This text is not found')
        else:
            self.count.set(str(data.count(find_data)))
    #�滻
    def replace_button_event(self):
        find_data = self.find_text.get(1.0, END).strip()
        replace_data = self.replace_text.get(1.0, END).strip()
        data = self.__get()
        data = data.replace(find_data, replace_data)
        self.__del_and_set(data)
    #��д
    def upper_button_event(self):
        data = self.__get().upper()
        self.__del_and_set(data)
    #Сд
    def lower_button_event(self):
        data = self.__get().lower()
        self.__del_and_set(data)
    #���
    def clear_button(self):
        self.text.delete(1.0, END)
    #�����ļ�
    def __sava_data(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__get())
        messagebox.showinfo('Notebook', 'Save success')
    #��ȡ�ı�
    def __get(self):
        # ����һ��Ҫ��strip
        return self.text.get(1.0, END).strip()
    #����
    def __del_and_set(self, data):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, data)

def vi():
    main = MainWindow()
    mainloop()  
