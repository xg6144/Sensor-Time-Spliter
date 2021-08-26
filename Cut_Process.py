import pandas as pd
import os
from tqdm import tqdm


def acc_cut(cat_acc):
    goal = 45375
    cut_data = list()
    cat_acc_numpy = cat_acc.to_numpy()  # 가속도 데이터

    # 가속도 센서 값 자르기
    for i in tqdm(range(cat_acc_numpy.shape[0])):
        out_name = f'Cat_Acc_{cat_acc_numpy[i + 1 - goal][1]}~{cat_acc_numpy[i][1]}.csv'
        out_dir = './Acc_Result'
        if i <= goal:
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
        elif i <= goal * 2:
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
        elif i <= goal * 3:
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
        elif i <= goal * 4:
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
        elif i <= goal * 5:
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
        elif i <= goal * 6:
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
        elif i <= goal * 7:
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


def gyro_cut(cat_acc, cat_gyro):
    goal = 45375
    cut_data = list()

    cat_acc_time = pd.DataFrame()
    cat_gyro_time = pd.DataFrame()

    cat_acc_time['acc_time'] = cat_acc['timestamp (+0900)']
    cat_gyro_time['gyro time'] = cat_gyro['timestamp (+0900)']

    cat_concat = pd.concat([cat_acc_time, cat_gyro_time], axis=1)
    cat_concat = cat_concat.drop_duplicates(keep=False)
    cat_time_df = pd.DataFrame(cat_concat, columns=['acc_time', 'gyro_time'])
    cat_gyro['timestamp (+0900)'] = cat_time_df['acc_time']
    cat_gyro_numpy = cat_gyro.to_numpy()  # 자이로 데이터


    # 자이로 센서 값 자르기
    # 자이로 데이터가 가속도 데이터 보다 개수가 두개에서 세개 정도 더많음
    # 그래서 같은 시간일 때만 자른다.

    for i in tqdm(range(cat_gyro_numpy.shape[0])):
        out_name = f'Cat_Gyro_{cat_gyro_numpy[i + 1 - goal][1]}~{cat_gyro_numpy[i][1]}.csv'
        out_dir = './Gyro_Result'
        if i <= goal:
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
        elif i <= goal * 2:
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
        elif i <= goal * 3:
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
        elif i <= goal * 4:
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
        elif i <= goal * 5:
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
        elif i <= goal * 6:
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
        elif i <= goal * 7:
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
