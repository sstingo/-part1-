import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False


def read_data():
    file_path = 'part1專題/data/學12-1新生註冊率-以「系(所)」統計.csv'
    df = pd.read_csv(file_path,
                     header=0,
                     dtype={'學年度': str, '學校統計處代碼': str, '系所代碼': str},
                     low_memory=False)
    return df


def create_labels(bar):
    bar_width = 0.5
    for item in bar:
        width = item.get_width()
        plt.text(
            width*1.05,
            item.get_y()+item.get_height()/2.,
            '%d' % int(width) if width - int(width) == 0 else '%.2f' % width,
            ha="center",
            va="bottom",
            fontsize=7
        )


def enroll_108_School(s, df108_school):
    df108_school = df108_school.sort_values(
        ['當學年度總量內核定新生招生名額(A)'], ascending=False)
    df108_school = df108_school.reset_index()

    plt.figure(figsize=(10, 5))
    b = plt.barh(y=range(10), width=df108_school['當學年度總量內核定新生招生名額(A)'].tail(
        10), align='center')
    plt.title('前10註冊人數最低'+s)
    plt.xlabel("人數")
    plt.ylabel("學校")
    plt.xticks(fontsize=7)
    plt.yticks(range(10), df108_school['學校名稱'].tail(10), fontsize=7)
    create_labels(b)
    plt.savefig('part1專題/image/前10註冊人數最低'+s)
    plt.show()

    # 當學年度新生註冊率(%)D =〔(C+E)/(A-B+E)〕＊100％
    df108_school['註冊率'] = (
        df108_school['當學年度新生註冊率(%)']).round(2)
    df108_school = df108_school.sort_values(
        ['當學年度新生註冊率(%)'], ascending=False)
    df108_school = df108_school.reset_index()

    plt.figure(figsize=(10, 5))
    b = plt.barh(y=range(10), width=df108_school['當學年度新生註冊率(%)'].tail(
        10), align='center')
    plt.title('前10註冊率最低'+s)
    plt.xlabel("註冊率(%)")
    plt.ylabel("學校")
    plt.xticks(fontsize=7)
    plt.yticks(range(10), df108_school['學校名稱'].tail(10), fontsize=7)
    plt.xlim(0, 100)
    create_labels(b)
    plt.savefig('part1專題/image/前10註冊率最低'+s)
    plt.show()


df = read_data()

# # 學校類別
# 108學年度 休學比例最高 前10個一般大學
df108_normal = df[df['學年度'] == '108'][df['學校類別'] == '一般大學']
df108_normal = df108_normal.groupby(['學校名稱']).agg({'當學年度總量內核定新生招生名額(A)': 'sum',
                                                   '當學年度新生保留入學資格人數(B)': 'sum',
                                                   '當學年度總量內新生招生核定名額之實際註冊人數(C)': 'sum',
                                                   '當學年度各學系境外(新生)學生實際註冊人數 (E)': 'sum',
                                                   '當學年度新生註冊率(%)': 'mean'})
enroll_108_School('一般大學', df108_normal)
# # 108學年度 休學比例最高 前10個技專校院
# df108_tech = df[df['學年度'] == '108'][df['學校類別'] == '技專校院']
# df108_tech = df108_tech.groupby(['學校名稱']).agg({'當學年度總量內核定新生招生名額(A)': 'sum',
#                                                '當學年度新生保留入學資格人數(B)': 'sum',
#                                                '當學年度總量內新生招生核定名額之實際註冊人數(C)': 'sum',
#                                                '當學年度各學系境外(新生)學生實際註冊人數 (E)': 'sum',
#                                                '當學年度新生註冊率(%)': 'mean'})
# enroll_108_School('技專校院', df108_tech)


# # 公私立
# # 108學年度 休學比例最高/最低 前10個公立學校
# df108_public = df[df['學年度'] == '108'][df['學校類別']
#                                       != '宗教研修學院'][df['設立別'] == '公立']
# df108_public = df108_public.groupby(['學校名稱']).agg({'當學年度總量內核定新生招生名額(A)': 'sum',
#                                                    '當學年度新生保留入學資格人數(B)': 'sum',
#                                                    '當學年度總量內新生招生核定名額之實際註冊人數(C)': 'sum',
#                                                    '當學年度各學系境外(新生)學生實際註冊人數 (E)': 'sum',
#                                                    '當學年度新生註冊率(%)': 'mean'})
# enroll_108_School('公立學校', df108_public)
# # 108學年度 休學比例最高/最低 前10個私立學校
# df108_private = df[df['學年度'] == '108'][df['學校類別']
#                                        != '宗教研修學院'][df['設立別'] == '私立']
# df108_private = df108_private.groupby(['學校名稱']).agg({'當學年度總量內核定新生招生名額(A)': 'sum',
#                                                      '當學年度新生保留入學資格人數(B)': 'sum',
#                                                      '當學年度總量內新生招生核定名額之實際註冊人數(C)': 'sum',
#                                                      '當學年度各學系境外(新生)學生實際註冊人數 (E)': 'sum',
#                                                      '當學年度新生註冊率(%)': 'mean'})
# enroll_108_School('私立學校', df108_private)
