import pandas as pd
import numpy as np

def data_filter(data, type_ = "Economatica"):
    
    if type_ == "Economatica":
        df = data.iloc[2:,:]
        tickers = df.iloc[0,:]
        tickers = [i.split("\n")[-1] for i in tickers]
        df.columns = tickers
        df = df.set_index("Data").drop(["Data"], axis = 0)

    return df.replace("-", np.nan).ffill(axis=0)

def rate_to_quota(data, period = "year", unit = 100, weekends = False):
    
    data.index = pd.to_datetime(data.index)
    
    if weekends == True:
        oper = "D"
    else:
        oper = "B"
    data = data.resample(oper).ffill()

    if (period == "month") or (period == "m"):
        data["quota"] = (1+ data.iloc[:,0])**(1/12)
    elif(period == "year") or (period == "y"):
        data["quota"] = (1+ data.iloc[:,0])**(1/252)
    else:
        data["quota"] = data.iloc[:,0]
    
    data.iloc[0,1] =  unit
    data["quota"] = data["quota"].cumprod()

    return data[["quota"]]

def ticker_not_repeat(data, index = False):
    if index == True:
        list_ = list(data.index)
    else:
        list_ = data
    
    if len(list_) <=1:
        return list_

    verf = []
    for tk in list_:
        if tk[:4] not in verf:
            verf.append(tk[:4])
        else:
            list_.remove(tk)
            
    if index == True:
        list_ = data.loc[list_]

    return list_

def complete_df(df1, df2, how = "left"):
    pass

def get_prices(asset, start, end):
    pass
