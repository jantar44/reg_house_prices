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

trainX['Alley'].fillna(2, inplace = True)
trainX['GarageType'].fillna(6, inplace = True)
trainX['GarageYrBlt'].fillna(0, inplace = True)
trainX['GarageFinish'].fillna(3, inplace = True)
trainX['BsmtQual'].fillna(4, inplace = True)
trainX['MasVnrArea'].fillna(0, inplace = True)
trainX['LotFrontage'].fillna(0, inplace = True)
trainX['PoolQC'].fillna(3, inplace = True)

# testX['Alley'].fillna(2, inplace = True)
# testX['GarageType'].fillna(6, inplace = True)
# testX['GarageYrBlt'].fillna(0, inplace = True)
# testX['GarageFinish'].fillna(3, inplace = True)
# testX['BsmtQual'].fillna(4, inplace = True)
# testX['MasVnrArea'].fillna(0, inplace = True)
# testX['LotFrontage'].fillna(0, inplace = True)
# testX['PoolQC'].fillna(3, inplace = True)


# print(trainX['Alley'].unique())
print(testX.info())
print(testX['KitchenQual'].unique())