import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('heart.csv')

new_columns=['age','sex','chest_pain','resting_bp','cholesterol','fasting_bs','resting_ecg','max_hr','exercise_angina'
            ,'oldpeak','st_slope','heart_disease']


df.columns=new_columns


df[df['cholesterol']==0]


df[df['resting_bp']==0]


df=df.drop(df.index[449])

df[df['resting_bp']==0]


numerical = ['age','resting_bp','cholesterol','max_hr','oldpeak']
categorical = ['sex','chest_pain','fasting_bs','resting_ecg','st_slope','exercise_angina']

df_data=df


y=df_data.heart_disease

x=df_data[numerical+categorical]
le = preprocessing.LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['chest_pain'] = le.fit_transform(df['chest_pain'])
df['chest_pain'] = le.fit_transform(df['chest_pain'])
df['resting_ecg'] = le.fit_transform(df['resting_ecg'])
df['st_slope'] = le.fit_transform(df['st_slope'])
df['exercise_angina'] = le.fit_transform(df['exercise_angina'])

x=df.drop(['heart_disease'], axis=1)
y=df.heart_disease

train_x, val_x, train_y, val_y = train_test_split(x, y,test_size=0.3,random_state = 0)
model = RandomForestClassifier(random_state = 0)

model.fit(train_x, train_y)

