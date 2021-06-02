import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn
import load_data

train = load_data.get_data()[0]
testX = load_data.get_data()[1]
inv_labels = load_data.get_inverted_labels()

trainX = train[:-1]
trainY = train['SalePrice']

def info_discrete(column):
    scatter = seaborn.catplot(x = column, y = train['SalePrice'], kind='swarm', data = train)
    plt.show()

def correlation_heatmap():
    correlation = train.corrwith(train.SalePrice)
    for col_name, corr_value in correlation.items():
        if corr_value > 0.3 or corr_value < -0.3:
            print(col_name, corr_value)
    #     print(i)
    # print(train[0:-2].corrwith(train.SalePrice).keys())
    # heatmap = seaborn.heatmap(train.corr())
    # plt.show()


print(correlation_heatmap())
# print(info_discrete(train['MSZoning']))

# lis = [1,2,3]
# plot2 = plt.plot(lis)
# plt.show()