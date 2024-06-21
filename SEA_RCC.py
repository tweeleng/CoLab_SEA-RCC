# -*- coding: utf-8 -*-

import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import calendar
from dateutil.relativedelta import relativedelta

def interface():
    models = ['ECMWF','NCEP','UKMO','JMA','DWD','MF','ECCC']
    curDate = dt.datetime.now()
    yearRange = np.arange(2023,curDate.year+1)
    #monthRange = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthRange = [('Jan',1),('Feb',2),('Mar',3),('Apr',4),('May',5),('Jun',6),('Jul',7),('Aug',8),('Sep',9),('Oct',10),('Nov',11),('Dec',12)]
    productRange = ['Anomalies', 'Tercile Probabilities', 'Quintiles Probabilities', 'Extremes Probabilities']

    print('Choose the following to suit your needs.\n \n Choose the model of your interest:')
    checkboxes = [widgets.Checkbox(value=True, description=label) for label in models]
    modelOutput = widgets.VBox(children=checkboxes)
    display(modelOutput)

    print(' ')
    print('Choose the model outlook initilaisation date:')
    yearOutput = widgets.Dropdown(
        options=yearRange,
        value=curDate.year,
        description='Year:',
        disabled=False,
    )
    display(yearOutput)
    monthOutput = widgets.Dropdown(
        options=monthRange,
        #value=monthRange[curDate.month-1],
        value=curDate.month,
        description='Month:',
        disabled=False,
    )
    display(monthOutput)

    print(' ')
    print('Choose the leadtime:\n(number of month(s) ahead of the initialisation time)')
    leadtimeOutput = widgets.SelectionSlider(
        options=np.arange(1,5),
        value=1,
        description='Leadtime:',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='d'
    )
    display(leadtimeOutput)

    print(' ')
    print('Choose the type of product to display:')
    productOutput = widgets.ToggleButtons(
        options = productRange,
        description = 'Product Type',
        disable = True,
        button_style = '',
        tooltips = ['Anomalies', 'Tercile Probabilities', 'Quintiles Probabilities', 'Extremes Probabilities']
    )
    display(productOutput)
    return checkboxes, yearOutput, monthOutput, leadtimeOutput, productOutput


def Display_Choice(output):
    selected_models = []
    for i in range(0, len(output[0])):
      if output[0][i].value == True:
        selected_models = selected_models + [output[0][i].description]
    
    print('Models selected: ')
    print(selected_models)
    print(' ')
    print("Initialisation month: " + calendar.month_name[output[2].value] + ' ' + str(output[1].value) )
    tmpDateIni = dt.datetime(output[1].value,output[2].value,18)
    if (tmpDateIni - dt.datetime.now()).days > 0:
      print('Please chosen an earlier initialisation date.')
      return
    
    outlook_date = dt.datetime(output[1].value,output[2].value,1)+ relativedelta(months=output[3].value)
    print("Outlook period: " + calendar.month_name[outlook_date.month] + ' ' + str(outlook_date.year) )
    print('Processing: ' + output[4].value)
    
    initialisationDate = str(output[1].value) + '%02d'%tmpDateIni.month
    outlookDate = '%02d'%outlook_date.month + '01'
    #print(initialisationDate)
    #print(outlookDate)
    
    return selected_models, initialisationDate, outlookDate, output[4].value

#def download_data():

#def MME_outlook(): # to combine the outlook accordingly to the respective choices
#    return XR_outlook

#def MME_verification(): # to combine the skill map accordingly to the respective choices
#    return XR_verification

#def MME_plot(XR_outlook, XR_verification): # to plot the outlook and skill map

