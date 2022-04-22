import pandas as pd
import numpy as np
import sys
import os

zipcode = '98075'
city = 'Sammamish'

raw_data_folder = 'raw_data'
extracted_data_folder = 'extracted_data'

raw_filename = os.path.join(raw_data_folder, f'{zipcode}.xlsx')
extracted_filename = os.path.join(extracted_data_folder, f'{zipcode}_extract.xlsx') 

def getList(input_str):
    list = [s for s in input_str.split('\n') if s is not None and len(s) > 0]
    return list

def getListRes(list):
    res = []
    states = ['Sold', 'Pending', 'Listed']
    for i in range(0, len(list)):
        # find price
        if '$' in list[i]:
            price = list[i]
            date = ''
            state = ''
            # find date and state
            for j in range(i, 0, -1):
                # find date
                if 'Date' in list[j]:
                    date = list[j - 1]

                # find state
                for st in states:
                    if st in list[j]:
                        state = list[j]

                if len(date) != 0 and len(state) != 0:
                    break

            res.append((price, date, state))
    return res

def getRecent(res):
    recent = []
    pre = None
    cur = None
    res.append(None)
    for i in range(0, len(res)):
        cur = res[i]
        if i == 0:
            pre = cur
        elif cur is None:
            recent.append(pre)
        elif cur is not None:
            if cur[1] != pre[1]:
                recent.append(pre)
                pre = cur

    if len(recent) < 3:
        for i in range(len(recent), 3):
            recent.append(None)

    return recent[:3]

def extractHistory(history):
    list = getList(history)
    res = getListRes(list)
    recent = getRecent(res)
            
    return recent

def extractPendingDate(history):
    list = [s for s in history.split('\n') if s is not None and len(s) > 0]
    res = []
    
    for i in range(0, len(list)):
        # find price
        if 'Pending' in list[i]:
            date = ''
            state = list[i]
            # find date and state
            for j in range(i, 0, -1):
                # find date
                if 'Date' in list[j]:
                    date = list[j - 1]

                if len(date) != 0 :
                    break   
            res.append((date,state))
            if len(date) != 0 :
                break  
    return res

def status(x) : 
    describe_table = x.describe(include='all')
    null_count = x.isnull().sum()
    null_rate = (x.isnull().sum())/(x.count()+x.isnull().sum())
    df_null_count = pd.DataFrame(null_count, columns = ['null_count'])
    df_null_rate = pd.DataFrame(null_rate, columns = ['null_rate'])
    status_table = pd.concat([df_null_count.T, df_null_rate.T,describe_table])
    return status_table