import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import pandas as pd
from Cut_Process import acc_cut, gyro_cut
import sys

class csv_file_cut():
    def __init__(self):
        self.camera_num = ''
        self.root = Tk()
        self.root.title("csv 파일 커팅기")
        self.root.geometry("640x400+100+100")
        self.root.resizable(False, False)

        self.n1_check = tkinter.IntVar()
        self.n2_check = tkinter.IntVar()
        self.n3_check = tkinter.IntVar()
        self.n4_check = tkinter.IntVar()
        self.n5_check = tkinter.IntVar()
        self.n6_check = tkinter.IntVar()

        self.n1_check.set(False)
        self.n2_check.set(False)
        self.n3_check.set(False)
        self.n4_check.set(False)
        self.n5_check.set(False)
        self.n6_check.set(False)

        self.check_n1_true = tkinter.Checkbutton(self.root, text='1번 카메라', var=self.n1_check)
        self.check_n1_true.pack()
        self.check_n2_true = tkinter.Checkbutton(self.root, text='2번 카메라', var=self.n2_check)
        self.check_n2_true.pack()
        self.check_n3_true = tkinter.Checkbutton(self.root, text='3번 카메라', var=self.n3_check)
        self.check_n3_true.pack()
        self.check_n4_true = tkinter.Checkbutton(self.root, text='4번 카메라', var=self.n4_check)
        self.check_n4_true.pack()
        self.check_n5_true = tkinter.Checkbutton(self.root, text='5번 카메라', var=self.n5_check)
        self.check_n5_true.pack()
        self.check_n6_true = tkinter.Checkbutton(self.root, text='6번 카메라', var=self.n6_check)
        self.check_n6_true.pack()

        Button(self.root, text='입력', command=self.click_check).pack()

        if self.camera_num is not None:
            self.root.filename_acc = filedialog.askopenfilename(initialdir="~/Desktop", title="가속도 파일을 선택해주세요.",
                                                                filetypes=(
                                                                    ("csv files", "*.csv"), ("all files", "*.*")))
            self.root.filename_gyro = filedialog.askopenfilename(initialdir="~/Desktop", title="자이로 센서 파일을 선택해주세요.",
                                                                 filetypes=(
                                                                     ("csv files", "*.csv"), ("all files", "*.*")))
            if not self.root.filename_gyro or not self.root.filename_acc:
                messagebox.showerror('Error', '파일을 선택해주세요.')
                sys.exit()

            self.data_path_acc = self.root.filename_acc
            self.acc_df = pd.read_csv(self.data_path_acc)

            self.data_path_gyro = self.root.filename_gyro
            self.gyro_df = pd.read_csv(self.data_path_gyro)
        self.root.mainloop()

    def click_check(self):
        if self.n1_check.get() == 1:
            self.camera_num = 'N1'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
        elif self.n2_check.get() == 1:
            self.camera_num = 'N2'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
        elif self.n3_check.get() == 1:
            self.camera_num = 'N3'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
        elif self.n4_check.get() == 1:
            self.camera_num = 'N4'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
        elif self.n5_check.get() == 1:
            self.camera_num = 'N5'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
        elif self.n6_check.get() == 1:
            self.camera_num = 'N6'
            acc_cut(cat_acc=self.acc_df, camera_num=self.camera_num)
            gyro_cut(cat_acc=self.acc_df, cat_gyro=self.gyro_df, camera_num=self.camera_num)
            sys.exit()
if __name__ == '__main__':
    csv_file_cut()
