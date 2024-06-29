import numpy as np
import pickle 
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# read data
data = pd.read_csv("exit/final.csv")
train = data

# drop columns not in use
train = train.drop(["Organization Name","Equity Only Funding", "Announced Date"], axis = 1 )

# encode categorical columns
le=LabelEncoder()
cols = train.select_dtypes(include=['object']).columns.tolist()

# store integer value assigned to each unique label in each categorical column
cat_labels = {}
for col in cols:
    train[col] = le.fit_transform(train[col]) 
    cat_labels[col] = list(le.classes_)

# function to convert string to correct integer value
def str_to_label(col, val):
    if col in ["Money Raised" , "Total Funding", "Number of Founders"]:
        return float(val)
    return cat_labels[col].index(val) + 1   


# load model
model =  pickle.load(open('exit/exit_status_model_v1.pkl', 'rb'))

# label names
label_names = cat_labels["Funding Status"]

# predict outcome given input from frontend
def predict(inputs):

    in_data = []
    for key in inputs:
        in_data.append(str_to_label(key, inputs[key]))

    input_data = np.array(in_data).reshape(-1, len(in_data))
    result = np.argmax(model.predict(input_data))
    return label_names[result]
