import pandas as pd
import os
from collections import Counter


print(os.listdir("../rds1/data"))
data = pd.read_csv('../rds1/data/data.csv')


temp_list = [i.split('|') for i in data['genres']]


def list_unrar(list_of_lists):
    result=[]
    for list in list_of_lists:
      result.extend(list)
    return result

temp_counter=Counter(list_unrar(temp_list))

print(temp_counter.most_common(1))
