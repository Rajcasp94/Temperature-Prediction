# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import pandas as pd
import numpy as np
from statsmodels.tsa.ar_model import AR
from statsmodels.tsa.holtwinters import SimpleExpSmoothing


def get_max_min_temp_list(data):
    max_temp=[]
    min_temp=[]
    data_len=int(data[0])
    for i in range(2,data_len+2):
        temp_list=data[i].split()
        max_temp.append(temp_list[2])
        min_temp.append(temp_list[3])
    return max_temp,min_temp

def get_min_max_temp_index(max_min_temp_list):
    max_temp_list=max_min_temp_list[0]
    min_temp_list=max_min_temp_list[1]
    max_missing_temps_index=[]
    min_missing_temps_index=[]
    for j in max_temp_list:
        if missing in j:
            max_missing_temps_index.append(max_temp_list.index(j))
    for k in min_temp_list:
        if missing in k:
            min_missing_temps_index.append(min_temp_list.index(k))
    return max_missing_temps_index,min_missing_temps_index

def model_fit(fit_data):
    model = SimpleExpSmoothing(fit_data)
    fit = model.fit()
    return fit

def predict_missing_min_max_temps(max_min_temp_missing_index,max_min_temp_list):
    max_missing_temps_index=max_min_temp_missing_index[0]
    min_missing_temps_index=max_min_temp_missing_index[1]
    max_temp_list=max_min_temp_list[0]
    min_temp_list=max_min_temp_list[1]
    for i in max_missing_temps_index:
        temp_data_max=max_temp_list[:i]
        temp_data_max=np.asarray(temp_data_max)
        temp_data_max=temp_data_max.astype(float)
        fit=model_fit(temp_data_max)
        predicted=int(fit.predict(len(temp_data_max), len(temp_data_max)))
        del max_temp_list[i]
        max_temp_list.insert(i,predicted)
    for i in min_missing_temps_index:
        temp_data_min=min_temp_list[:i]
        temp_data_min=np.asarray(temp_data_min)
        temp_data_min=temp_data_min.astype(float)
        fit=model_fit(temp_data_min)
        predicted=int(fit.predict(len(temp_data_min), len(temp_data_min)))
        del min_temp_list[i]
        min_temp_list.insert(i,predicted)
    return max_temp_list,min_temp_list

data = sys.stdin.readlines()
missing ='Missing'
max_min_temp_list=get_max_min_temp_list(data)
max_min_temp_missing_index=get_min_max_temp_index(max_min_temp_list)

predicted_temps=predict_missing_min_max_temps(max_min_temp_missing_index,max_min_temp_list)

max_predicted_temps=predicted_temps[0]
min_predicted_temps=predicted_temps[1]



#def sorting_and display()


