import pandas as pd

train_data = pd.read_csv('data/train.csv', header=0, index_col = 0)
test_data = pd.read_csv('data/train.csv', header=0, index_col = 0)

def standarize_data(data_series):
    values = sorted(data_series.dropna().unique())
    n_val = [i for i in range(len(values))]
    map_values = dict(zip(values, n_val))
    return data_series.map(map_values)


# standarize_data(train_data['Neighborhood'])


to_standarize = ['MSSubClass', 'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',\
       'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',\
       'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'ExterQual', 'ExterCond', 'Foundation',\
       'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',\
       'Heating', 'HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional',\
       'FireplaceQu', 'GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive',\
       'PoolQC', 'Fence', 'MiscFeature', 'MiscVal', 'MoSold', 'SaleType', 'SaleCondition']

for series in to_standarize:
    train_data[series] = standarize_data(train_data[series])
    test_data[series] = standarize_data(test_data[series])

print(train_data.info)