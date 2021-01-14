import pandas as pd
import seaborn as sns
import lambdata_james_slagle.my_mod as js

# # Demo enlarge(int)
# x = 5
# print(f"Number before enlarging = {x}")
# print(f"Number after enlarging = {js.enlarge(x)}")

# # Demo null_count(df)
# penguins = sns.load_dataset("penguins")
# print(f"Null values before removing = {js.null_count(penguins)}")
# penguins.dropna(inplace=True)
# print(f"Null values after removing = {js.null_count(penguins)}")

# # Demo split_dates(string/Datetime raw_dates)
# # Use Tanzania well data
# DATA_PATH = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-2-Kaggle-Challenge/master/data/'
# train_val = pd.merge(pd.read_csv(DATA_PATH+'waterpumps/train_features.csv', na_values=[0, -2.000000e-08]),
#                  pd.read_csv(DATA_PATH+'waterpumps/train_labels.csv')).set_index('id')
# YMD = js.year_month_day(train_val.date_recorded)
# print(YMD)
