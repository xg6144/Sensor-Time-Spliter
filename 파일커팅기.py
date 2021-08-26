from tkinter import *
from tkinter import filedialog
import pandas as pd
from Cut_Process import acc_cut, gyro_cut

root = Tk()
root.filename_acc = filedialog.askopenfilename(initialdir = "~/Desktop",title = "가속도 파일을 선택해주세요.",filetypes = (("csv files","*.csv"),("all files","*.*")))
root.filename_gyro = filedialog.askopenfilename(initialdir = "~/Desktop",title = "자이로 센서 파일을 선택해주세요.",filetypes = (("csv files","*.csv"),("all files","*.*")))

data_path_acc = root.filename_acc
acc_df = pd.read_csv(data_path_acc)

data_path_gyro = root.filename_gyro
gyro_df = pd.read_csv(data_path_gyro)

acc_cut(cat_acc=acc_df)
gyro_cut(cat_acc=acc_df, cat_gyro=gyro_df)

