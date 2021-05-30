from numpy import nan
import pandas as pd
try:
    train_data = pd.read_csv('data/train.csv', header=0, index_col = 0)
    test_data = pd.read_csv('data/test.csv', header=0, index_col = 0)
except FileNotFoundError:
    print('Wrong path')

def null_clean(data):
    data = data.replace(['NA'], None)

null_clean(train_data)
null_clean(test_data)

def standarize_data(data_series, counter):
    if counter % 2 == 0:
        values = sorted(data_series.dropna().unique())
        n_val = [int(i) for i in range(len(values))]
        map_values = dict(zip(values, n_val,))
        labels[data_series.name] = map_values
    return data_series.map(labels[data_series.name])

to_standarize = ['MSSubClass', 'MSZoning', 'Street', 'Alley', 'LotShape',\
        'LandContour', 'Utilities', 'LotConfig', 'LandSlope',  'Neighborhood',\
        'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle',\
        'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual',\
        'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure',\
        'BsmtFinType1', 'BsmtFinType2', 'Heating', 'HeatingQC', 'CentralAir',\
        'Electrical', 'KitchenQual', 'Functional', 'FireplaceQu', 'GarageType',\
        'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive', 'PoolQC',\
        'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'SaleType', 'SaleCondition']

labels = dict()

_i = 0
for series in to_standarize:
    train_data[series] = standarize_data(train_data[series], _i)
    _i+=1
    test_data[series] = standarize_data(test_data[series], _i)
    _i+=1

def get_data():
    return train_data, test_data

def get_labels():
    return labels

def get_inverted_labels3():
    inverted_labels = dict()
    for srs in to_standarize:
        inverted_labels[srs] = {v: k for k, v in labels[srs].items()}
    return inverted_labels
