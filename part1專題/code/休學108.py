import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False


def read_data():
    file_path = 'part1專題/data/學13-1於學年底處於休學狀態之人數-以系(所)統計.csv'
    df = pd.read_csv(file_path,
                     header=0,
                     dtype={'學年度': str, '學校統計處代碼': str, '系所代碼': str},
                     low_memory=False)
    df = df.rename(columns={'於學年底處於休學狀態之人數-總計': '總計',
                            '於學年底處於休學狀態之人數-因傷病': '因傷病',
                            '於學年底處於休學狀態之人數-因經濟困難': '因經濟困難',
                            '於學年底處於休學狀態之人數-因學業成績': '因學業成績',
                            '於學年底處於休學狀態之人數-因志趣不合': '因志趣不合',
                            '於學年底處於休學狀態之人數-因工作需求': '因工作需求懷孕',
                            '於學年底處於休學狀態之人數-因懷孕': '因懷孕',
                            '於學年底處於休學狀態之人數-因育嬰': '因育嬰',
                            '於學年底處於休學狀態之人數-因兵役': '因兵役',
                            '於學年底處於休學狀態之人數-因出國': '因出國',
                            '於學年底處於休學狀態之人數-因論文': '因論文',
                            '於學年底處於休學狀態之人數-因適應不良': '因適應不良',
                            '於學年底處於休學狀態之人數-因家人傷病': '因家人傷病',
                            '於學年底處於休學狀態之人數-因考試訓練': '因考試訓練',
                            '於學年底處於休學狀態之人數-因逾期未註冊、繳費、選課': '因逾期未註冊、繳費、選課',
                            '於學年底處於休學狀態之人數-其他': '其他'})
    return df


def create_labels(bar):
    bar_width = 0.5
    for item in bar:
        width = item.get_width()
        plt.text(
            width*1.05,
            item.get_y()+item.get_height()/2.,
            '%d' % int(width) if width -
            int(width) == 0 else '%.2f' % width,
            # '%d' % int(width),
            ha="center",
            va="bottom",
            fontsize=7
        )


def drop_108_School(s, df108_school):
    df108_school = df108_school.sort_values(['總計'])
    df108_school = df108_school.reset_index()

    # plt.subplot(2, 1, 1)
    plt.figure(figsize=(10, 5))
    b = plt.barh(y=range(10), width=df108_school['總計'].tail(
        10), align='center')
    plt.title('前10休學人數最高學校'+s)
    plt.xlabel("人數")
    plt.ylabel("學校")
    plt.xticks(fontsize=7)
    plt.yticks(range(10), df108_school['學校名稱'].tail(10), fontsize=7)
    create_labels(b)
    plt.savefig('part1專題/image/前10休學人數最高學校'+s)
    plt.show()

    df108_school['休學率'] = (df108_school['總計'] /
                           df108_school['在學學生數'] * 100).round(2)
    df108_school = df108_school.sort_values(['休學率'])
    df108_school = df108_school.reset_index()

    # plt.subplot(2, 1, 2)
    plt.figure(figsize=(10, 5))
    b = plt.barh(y=range(10), width=df108_school['休學率'].tail(
        10), align='center')
    plt.title('前10休學率最高'+s)
    plt.xlabel("休學率(%)")
    plt.ylabel("學校")
    plt.xticks(fontsize=7)
    plt.yticks(range(10), df108_school['學校名稱'].tail(10), fontsize=7)
    plt.xlim(0, 40)
    create_labels(b)
    plt.savefig('part1專題/image/前10休學率最高'+s)
    plt.show()


df = read_data()

# 學校類別
# 108學年度 休學比例最高 前10個一般大學
df108_normal = df[df['學年度'] == '108'][df['在學學生數'] != 0][df['學校類別'] == '一般大學']
df108_normal = df108_normal.groupby(['學校名稱']).sum()
drop_108_School('一般大學', df108_normal)
# # 108學年度 休學比例最高 前10個技專校院
# df108_tech = df[df['學年度'] == '108'][df['在學學生數'] != 0][df['學校類別'] == '技專校院']
# df108_tech = df108_tech.groupby(['學校名稱']).sum()
# drop_108_School('技專校院', df108_tech)


# # 公私立
# # 108學年度 休學比例最高/最低 前10個公立學校
# df108_public = df[df['學年度'] == '108'][df['在學學生數']
#                                       != 0][df['學校類別'] != '宗教研修學院'][df['設立別'] == '公立']
# df108_public = df108_public.groupby(['學校名稱']).sum()
# drop_108_School('公立學校', df108_public)
# # 108學年度 休學比例最高/最低 前10個私立學校
# df108_private = df[df['學年度'] == '108'][df['在學學生數']
#                                        != 0][df['學校類別'] != '宗教研修學院'][df['設立別'] == '私立']
# df108_private = df108_private.groupby(['學校名稱']).sum()
# drop_108_School('私立學校', df108_private)


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# plt.savefig("test.png",                         # 儲存圖檔
#             bbox_inches='tight',               # 去除座標軸占用的空間
#             pad_inches=0.0)


#
#
#
#
# ax = df108_school['總計'].tail(10).plot.barh(rot = 0, figsize = (10, 5), title = '前10休學人數學校', xlabel = '人數', ylabel = '學校')
# ax.xticks = df108_school.總計
# plt.xticks(df108_school.總計)

# df108_school = df108_school.groupby(['學校名稱'], as_index=False).sum()

# img = df108_school['總計'].tail(10).plot.barh(
#     rot=0, figsize=(10, 5), title='前10休學人數學校')
# fig = img.get_figure()

# # img = df_school_all.tail(10).plot.barh(rot=0, figsize=(10, 5))
# # fig = img.get_figure()
# # fig.savefig('學校-於學年底處於休學狀態之人數.png')

#
#
#
# print(df_school.describe())
# df_school = df_school.pivot_table(
#     index='學校名稱', columns='學年度', values='於學年底處於休學狀態之人數-總計')
# df_school_108 = df_school[df_school.學年度 == 108]
