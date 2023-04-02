# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:12:47 2023

@author: SSD
""" 
#importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def indexingfile(data, file):
    data = pd.read_csv(file)
    #data_tr=pd.DataFrame.transpose(data)
    data.index = data['Country Name']
    data.drop(['Country Name', 'Country Code', 'Indicator Name',
                               'Indicator Code'], axis=1, inplace=True)
    data = data.loc[['Argentina', 'Brazil', 'Colombia', 'Germany', 'Jamaica',
                     'India','United States', 'Indonesia'],:]

    return data


def barplot(data, titles):
    plt.figure()
    ax = plt.subplot()
    width = 0.75/len(data.columns)
    offset = width/2
    for i, j in enumerate(data.columns):
        ax.bar([width*i+offset+k for k in range(len(data.index))],
               data[j], width=width, label=j)
    ax.set_xlabel('Country Name')
    ax.set_ylabel(titles[0])
    ax.set_title(titles[1])
    ax.set_xticks([j+0.4 for j in range(len(data.index))])
    ax.set_xticklabels(data.index, rotation=90)
    ax.legend()
    plt.show()


def transpose(data):
    data_tr=pd.DataFrame.transpose(data)
    data_tr.header=data_tr.iloc[0,:]
    data_tr=data_tr.iloc[1:,:]
    
    return data_tr
    
    
def country(dataset,names,country_name):
    country=pd.DataFrame()
    for b in range(len(dataset)):
        country[names[b]]=dataset[b].loc['1995':'2010',country_name]
    
    return country


def correlation_heatmap(data,title,color):
    
    
    for c in data.columns:
        data[c]=data[c].astype(dtype=np.int64)
    corr=data.corr().to_numpy()
    
    
    fig = plt.subplots(figsize=(8,8))
    plt.imshow(corr,cmap=color,interpolation='nearest')
    plt.colorbar(orientation='vertical',fraction=0.05)
    
    
    plt.xticks(range(len(data.columns)),data.columns,rotation=90,fontsize=15)
    plt.yticks(range(len(data.columns)),data.columns,rotation=0,fontsize=15)
    
    
    for c in range(len(data.columns)):
        for d in range(len(data.columns)):
            plt.text(c,d, corr[c,d].round(2),ha='center',va='center',
                     color='black')
            
    plt.title(title)
    plt.show()
    
        
years=['1995','2000','2005','2010','2015','2020']

New_Electricity=indexingfile('electricity','Electricity_Access.csv')
New_Electricity=New_Electricity.loc[:,years]
print('electrity')
print(New_Electricity)
titles=['Electricity','Electricity_Access']
bar_Electricity=barplot(New_Electricity,titles)


New_Agriculture_Land=indexingfile('Agriculture_land','Agriculture_Land.csv')
New_Agriculture_Land=New_Agriculture_Land.loc[:,years]
print('Agriculture')
print(New_Agriculture_Land)
titles=['Agriculture','Agriculturein SQ.KM']
bar_Agriculture=barplot(New_Agriculture_Land,titles)


New_Total_Pop=indexingfile('Total_Pop','Total_Pop.csv')
New_Total_Pop=New_Total_Pop.loc[:,years]
print('pop')
print(New_Total_Pop)
titles=['population','Total Population']
bar_population=barplot(New_Total_Pop,titles)


#New_Death_rate=indexingfile('Death_rate','Death_rate.csv')
#New_Death_rate=New_Death_rate.loc[:,years]
#print('Death')
#print(New_Death_rate)
#titles=['Deaths','Death_rate']
#bar_Land=barplot(New_Death_rate,titles)


New_Electric=indexingfile('Electric_Consumption',
                         'Eletric power consumption.csv')
New_Electric=New_Electric.loc[:,years]
print('electric')
print(New_Electric) 
titles=['Power Consumption','Electric Power Consumption']  
bar_Electric=barplot(New_Electric,titles)


New_Annual_freshwater=indexingfile('freshwater','Annual_freshwater.csv')
New_Annual_freshwater=New_Annual_freshwater.loc[:,years]
print('water')
print('New_Annual_freshwater')
titles=['freshwater','Annual_freshwater']
bar_water=barplot(New_Annual_freshwater,titles)

New_Electricity_tr=transpose(New_Electricity)
New_Agriculture_Land_tr=transpose(New_Agriculture_Land)
New_Total_Pop_tr=transpose(New_Total_Pop)
#New_Death_rate_tr=transpose(New_Death_rate)
New_Electric_tr=transpose(New_Electric)
New_Annual_freshwater_tr=transpose(New_Annual_freshwater)



names=['Electricity_access','Agric_land','Total_pop','Electric_consum',
       'Annual fresh water']

dataset=[New_Electricity_tr,New_Agriculture_Land_tr,New_Total_Pop_tr,
         New_Electric_tr,New_Annual_freshwater_tr]

India= country(dataset,names,'India')
correlation_heatmap(India,'India','Spectral_r')

Argentina=country(dataset,names,'Argentina')
correlation_heatmap(Argentina,'Argentina','Greens')

Brazil=country(dataset,names,'Brazil')
correlation_heatmap(Brazil,'Brazil','Greens_r')

Colombia=country(dataset,names,'Colombia')
correlation_heatmap(Colombia,'Colombia','Blues_r')

Germany=country(dataset,names,'Germany')
correlation_heatmap(Germany,'Germany','Blues')

Jamaica=country(dataset,names,'Jamaica')
correlation_heatmap(Jamaica,'jamaica','cool_r')

United_States=country(dataset,names,'United States')
correlation_heatmap(United_States,'United States','summer')

Indonesia=country(dataset,names,'Indonesia')
correlation_heatmap(Indonesia,'Indonesia','winter')