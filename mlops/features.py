import argparse
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('--input_file', type=str)
parser.add_argument('--output_file', type=str)

input_file = parser.parse_args().input_file
output_file = parser.parse_args().output_file
df = pd.read_csv(input_file)
df.dropna(inplace=True)

X = df[['Current Weight (lbs)', 'Physical Activity Level']]
y = df['Final Weight (lbs)']

X = pd.get_dummies(X, drop_first=True)

preprocessed_df = pd.concat([X, y], axis=1)
preprocessed_df.to_csv(output_file, index=False)

print('Предобработка выполнена')
