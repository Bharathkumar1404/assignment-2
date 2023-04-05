# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:12:47 2023

@author: SSD
""" 
#importing the libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def readingfile(file):
    '''
    This function creates a dataframe from given pathfile

    Parameters
    ----------
    file : STR
        String of filepath.

    Returns
    -------
    data : Dataframe
        Dataframe with csv filepath.

    '''
    data = pd.read_csv(file)
    data.index = data['Country Name']
    data.drop(['Country Code', 'Indicator Name',
                               'Indicator Code'], axis=1, inplace=True)
    data = data.loc[['Argentina', 'Brazil', 'Colombia', 'Germany',
                     'India', 'United States', 'Indonesia'], :]

    return data


def barplot(data, titles):
    '''
    

    Parameters
    ----------
    data : Str
        String with certain years.
    titles : list 
        list cointains y label and title of the bar plot.

    Returns
    -------
    bar-plot.

    '''
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
    '''
    

    Parameters
    ----------
    data : pandas.Dataframe
        transpose the given data.

    Returns
    -------
    data_tr : Str
        Returns the transpose data .

    '''
    data_tr=pd.DataFrame.transpose(data)
    #=data_tr.header=data.iloc[0, :]
    data_tr=data_tr.iloc[1:,:]
    
    return data_tr
def country(dataset,names,country_name):
    '''
    

    Parameters
    ----------
    dataset : TYPE
        DESCRIPTION.
    names : TYPE
        DESCRIPTION.
    country_name : TYPE
        DESCRIPTION.

    Returns
    -------
    country : TYPE
        DESCRIPTION.

    '''
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
  
years1=['1990','1992','1994','1998','2000','2002','2004','2006','2008',
        '2010','2012','2014','2016','2018','2020']
years=['1995','2000','2005','2010','2015','2020']


Electricity=readingfile('Electricity_Access.csv')
t=Electricity.describe()
print(t)
Electricity_tr=transpose(Electricity)
Electricity_B=Electricity.loc[:,years]
Electricity_L=Electricity_tr.loc[years1,:]



Agriculture_Land=readingfile('Agriculture_Land.csv')
Agriculture_Land_tr=transpose(Agriculture_Land)
Agriculture_Land_L=Agriculture_Land_tr.loc[years1,:]
Agriculture_Land_B=Agriculture_Land.loc[:,years]


Total_Pop=readingfile('Total_Pop.csv')
Total_Pop_tr=transpose(Total_Pop)
Total_Pop_L=Total_Pop_tr.loc[years1,:]
Total_Pop_B=Total_Pop.loc[:,years]


Death_rate=readingfile('Death_rate.csv')
Death_rate_tr=transpose(Death_rate)
Death_rate_L=Death_rate_tr.loc[years1,:]
Death_rate_B=Death_rate.loc[:,years]


Electric=readingfile('Eletric power consumption.csv')
Electric_tr=transpose(Electric)
Electric_L=Electric_tr.loc[years1,:]
Electric_B=Electric.loc[:,years]


Annual_freshwater=readingfile('Annual_freshwater.csv')
Annual_freshwater_tr=transpose(Annual_freshwater)
Annual_freshwater_L=Annual_freshwater_tr.loc[years1,:]
Annual_freshwater_B=Annual_freshwater.loc[:,years]

Electricity_production=readingfile('Electrcity production from oil and gas.csv')
Electricity_production_tr=transpose(Electricity_production)
Electricity_production_L=Electricity_production_tr.loc[years1,:]
Electricity_production_B=Electricity_production.loc[:,years]


nitrous=readingfile('nitrous.csv')
nitrous_tr=transpose(nitrous)
nitrous_L=nitrous_tr.loc[years1,:]
nitrous_B=nitrous.loc[:,years]


Forest_area=readingfile('forest area.csv')
Forest_area_tr=transpose(Forest_area)


for i in Total_Pop_B.columns:
    Total_Pop_B[i]=Total_Pop_B[i]/1000000
titles=['population','Total Population']
bar_population=barplot(Total_Pop_B,titles)

for i in Agriculture_Land_B.columns:
    Agriculture_Land_B[i]=Agriculture_Land_B[i]/1000000
titles=['Agriculture','Agriculturein SQ.KM']
bar_Agriculture=barplot(Agriculture_Land_B,titles)

titles=['%nitrous','nitrous']
bar_n=barplot(nitrous_B,titles)


#line plot
plt.figure()
for i in Electricity_L.columns:
    plt.plot(Electricity_L.index,Electricity_L[i], label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('% Electricity')
plt.title('Electricity_access')
plt.xticks(Electricity_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

plt.figure()
for i in Agriculture_Land_L.columns:
    plt.plot(Agriculture_Land_L.index,Agriculture_Land_L[i], 
             label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('% Agriculture')
plt.title('Agriculture_land')
plt.xticks(Agriculture_Land_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

plt.figure()
for i in Total_Pop_L.columns:
    plt.plot(Total_Pop_L.index,Total_Pop_L[i],label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('Pop_rate')
plt.title('Total_Pop')
plt.xticks(Total_Pop_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

plt.figure()
for i in Electric_L.columns:
    plt.plot(Electric_L.index,Electric_L[i], label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('E_Consumption')
plt.title('Electric-consumption')
plt.xticks(Total_Pop_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

plt.figure()
for i in Annual_freshwater_L.columns:
    plt.plot(Annual_freshwater_L.index,Annual_freshwater_L[i], 
             label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('% Freshwater')
plt.title('Annual_freshwater')
plt.xticks(Total_Pop_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

plt.figure()
for i in Death_rate_L.columns:
    plt.plot(Death_rate_L.index,Death_rate_L[i], label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('% Death')
plt.title('Death_rate')
plt.xticks(Total_Pop_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()


plt.figure()
for i in Electricity_production_L.columns:
    plt.plot(Electricity_production_L.index,Electricity_production_L[i], 
             label=i, linestyle=':')
plt.xlabel('Year')
plt.ylabel('% Production')
plt.title('Production_rate')
plt.xticks(Total_Pop_L.index[::2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

#correlation
names=['Agric_land','Total_pop','Electric_consum',
       'Annual fresh water','forest_area','nitrous']

dataset=[Agriculture_Land_tr,Total_Pop_tr,
         Electric_tr,Annual_freshwater_tr,Forest_area_tr,nitrous_tr]

India= country(dataset,names,'India')
correlation_heatmap(India,'India','ocean_r')

Argentina=country(dataset,names,'Argentina')
correlation_heatmap(Argentina,'Argentina','gist_rainbow')

Brazil=country(dataset,names,'Brazil')
correlation_heatmap(Brazil,'Brazil','YlGnBu')

