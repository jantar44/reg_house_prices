import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn
import load_data

train = load_data.get_data()[0]
testX = load_data.get_data()[1]
inv_labels = load_data.get_inverted_labels()

trainX = train.drop(['SalePrice'], axis = 1)
trainY = train['SalePrice']

def info_discrete(column):
    scatter = seaborn.stripplot(x = column, y = train['SalePrice'], data = train)
    if column in inv_labels.keys():
        scatter.set_xticklabels(inv_labels[column].values())
    else:
        pass
    plt.show()

def unsignificant_deletion():
    correlation = train.corrwith(train.SalePrice)
    to_delete = list()
    for col_name, corr_value in correlation.items():
        if corr_value < 0.35 and corr_value > -0.35:
            to_delete.append(col_name)
    
    return to_delete

trainX.drop(unsignificant_deletion(), axis = 1, inplace = True)
testX.drop(unsignificant_deletion(), axis = 1, inplace = True)
