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
    This function creates a dataframe from given pathfile and reading the file 
    and indexing and droping the indexs and locating the certain countries

    Parameters
    ----------
    file : STR
        String of  csv filepath.

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
    
ploting the bar plot by enumerate the data 
    Parameters
    ----------
    data : Str
        String will do subplot and having thw width certain years.
    titles : list 
        list cointains y label and title of the bar plot.

    Returns
    -------
    bar-plot with certain countries and years.

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
     it transpose the given data and returns the transposed  data 

    Parameters
    ----------
    data : pandas.Dataframe
        transpose the given data and locating the index number and 
        transpose the data .

    Returns
    -------
    data_tr : Str
        Returns the transpose data .

    '''
    data_tr=pd.DataFrame.transpose(data)
    data_tr.columns=data_tr.iloc[0, :]
    data_tr=data_tr.iloc[1:,:]
    
    return data_tr
def country(dataset,names,country_name):
    '''
    

    Parameters
    ----------
    dataset : str
        using the transposed data and locate the certain years and countries.
    names : list
        it contains the names of the data and represent the names of 
        the indicators.
    country_name : str
        it returns the values of data to certain country with different 
        types of indicators.

    Returns
    -------
    country : str
        it returns a country  with differnt types of indicators .

    '''
    country=pd.DataFrame()
    for b in range(len(dataset)):
        country[names[b]]=dataset[b].loc['1995':'2010',country_name]
    
    return country
def correlation_heatmap(data,title,color):
    '''
    

    Parameters
    ----------
    data : str
        certain country with different indicators shows the 
        correlation coefficient.
    title : str
        name of the country  in difinte name.
    color : str
        it plots the heatmap with given type of color.

    Returns
    -------
    returns the correlation heatmap with certain values .

    '''
    
    
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
#required years for the line plot and bar plot 
years1=['1990','1992','1994','1998','2000','2002','2004','2006','2008',
        '2010','2012','2014','2016','2018','2020']
years2=['1990','1992','1994','1998','2000','2002','2004','2006','2008',
        '2010','2012','2014']
years=['1995','2000','2005','2010','2015','2020']

#reading the file path and returns the datframe
Electricity=readingfile('Electricity_Access.csv')
Agriculture_Land=readingfile('Agriculture_Land.csv')
Total_Pop=readingfile('Total_Pop.csv')
Death_rate=readingfile('Death_rate.csv')
Electric_consumption=readingfile('Eletric power consumption.csv')
Annual_freshwater=readingfile('Annual_freshwater.csv')
nitrous_oxide_emission=readingfile('nitrous.csv')
Forest_area=readingfile('forest area.csv')
Electricity_production=readingfile('Electrcity production from oil and gas.csv')


#transposing the datframe and returning the datframe
Electricity_tr=transpose(Electricity)
Agriculture_Land_tr=transpose(Agriculture_Land)
Total_Pop_tr=transpose(Total_Pop)
Death_rate_tr=transpose(Death_rate)
Electric_consumption_tr=transpose(Electric_consumption)
Annual_freshwater_tr=transpose(Annual_freshwater)
Electricity_production_tr=transpose(Electricity_production)
nitrous_tr=transpose(nitrous_oxide_emission)
Forest_area_tr=transpose(Forest_area)


#plotting the datframe and returns the line graph dataframe

Electricity_production_L=Electricity_production_tr.loc[years2,:]



# plotting the datagframe in bar plot type datframe
Agriculture_Land_B=Agriculture_Land.loc[:,years]
Total_Pop_B=Total_Pop.loc[:,years]
nitrous_B=nitrous_oxide_emission.loc[:,years]


#it describes the dataframe and returns the values of mean,max,std,min,count
# and all the values
total_pop_describe=Total_Pop.describe()
print(total_pop_describe)
Electricity_production=Electricity_production.describe()
print(Electricity_production
      )


#slicing the percentage values 
for i in Total_Pop_B.columns:
    Total_Pop_B[i]=Total_Pop_B[i]/1000000
#it represents the  y label and plot tilte 
titles=['population','Total Population']
#plotintg the barplot 
bar_population=barplot(Total_Pop_B,titles)
#slicing the percentage values 
for i in Agriculture_Land_B.columns:
    Agriculture_Land_B[i]=Agriculture_Land_B[i]/1000000
#it represents the  y label and plot tilte 
titles=['% Agri_land','Agricultural land (% of land area)']
#plotintg the barplot
bar_Agriculture=barplot(Agriculture_Land_B,titles)
#it represents the  y label and plot tilte 
titles=['emission of nitrous',
        'Nitrous oxide emissions (thousand metric tons of CO2 equivalent)']
#plotintg the barplot
bar_n=barplot(nitrous_B,titles)



#ploting the line plot and showing the x label amd y label 
#and titke of the plot and shows the plot
plt.figure()
for i in Electricity_production_L.columns:
    plt.plot(Electricity_production_L.index,Electricity_production_L[i], 
             label=i, linestyle=':',marker='*')
plt.xlabel('Year')
plt.ylabel('%Production_rate')
plt.title('Electricity_Production_rate from oil&gas')
plt.xticks(Electricity_production_L.index[::-2])
plt.legend(title='Country',bbox_to_anchor=(1, 1))
plt.show()

#ploting the correlation coefficint of the dataframe and
# represent the names for the plot 
#name represnts the names 
#datsets are the transposed data
names=['Agric_land','Total_pop','Electric_consumption',
       'Annual fresh water','forest_area','nitrous_oxide_emission']

dataset=[Agriculture_Land_tr,Total_Pop_tr,
         Electric_consumption_tr,Annual_freshwater_tr,Forest_area_tr,nitrous_tr]

India= country(dataset,names,'India')
correlation_heatmap(India,'India','ocean_r')

Argentina=country(dataset,names,'Argentina')
correlation_heatmap(Argentina,'Argentina','gist_rainbow')

Brazil=country(dataset,names,'Brazil')
correlation_heatmap(Brazil,'Brazil','YlGnBu')