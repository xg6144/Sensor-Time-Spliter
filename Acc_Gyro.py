from tkinter import *
from tkinter import filedialog
import os
import pandas as pd

def cut_df_acc(cat_acc):
    goal = 45375
    cut_data = list()

    cat_acc_numpy = cat_acc.to_numpy()

    # 가속도 센서 값 자르기
    for i in range(cat_acc_numpy.shape[0]):
        out_name = f'Cat_Acc_{cat_acc_numpy[i-goal][1]}~{cat_acc_numpy[i][1]}.csv'
        out_dir = './Acc_Result'
        if i < goal:
            cut_data.append(cat_acc_numpy[i])
            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 2:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 3:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 4:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 5:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 6:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 7:
            cut_data.append(cat_acc_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (g)',
                                               'y-axis (g)',
                                               'z-axis (g)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()


def cut_df_gyro(cat_gyro):
    goal = 45375
    cut_data = list()

    cat_gyro_numpy = cat_gyro.to_numpy()
    # 자이로 센서 값 자르기
    for i in range(cat_gyro_numpy.shape[0]):
        out_name = f'Cat_Gyro_{cat_gyro_numpy[i - goal][1]}~{cat_gyro_numpy[i][1]}.csv'
        out_dir = './Gyro_Result'
        if i < goal:
            cut_data.append(cat_gyro_numpy[i])
            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 2:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 3:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 4:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 5:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 6:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()
        elif i < goal * 7:
            cut_data.append(cat_gyro_numpy[i])

            if len(cut_data) == goal:
                cut_df = pd.DataFrame(cut_data,
                                      columns=['epochs(ms)', 'timestamp (+0900)', 'elapsed (s)', 'x-axis (deg/s)',
                                               'y-axis (deg/s)',
                                               'z-axis (deg/s)'])
                if not os.path.exists(out_dir):
                    os.mkdir(out_dir)

                dir_name = os.path.join(out_dir, out_name)

                cut_df.to_csv(dir_name, index=False)
                cut_data.clear()

root = Tk()
root.filename_acc = filedialog.askopenfilename(initialdir = "~/Desktop",title = "가속도 파일을 선택해주세요.",filetypes = (("csv files","*.csv"),("all files","*.*")))
root.filename_gyro = filedialog.askopenfilename(initialdir = "~/Desktop",title = "자이로 센서 파일을 선택해주세요.",filetypes = (("csv files","*.csv"),("all files","*.*")))

data_path_acc = root.filename_acc
acc_df = pd.read_csv(data_path_acc)

data_path_gyro = root.filename_gyro
gyro_df = pd.read_csv(data_path_gyro)

cut_df_acc(acc_df)
cut_df_gyro(gyro_df)
