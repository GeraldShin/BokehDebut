import pandas as pd
import matplotlib.pyplot as plt
from bokeh.io import output_file, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Slider
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, column, row
from bokeh.core.properties import value
#Importing and cleaning up the csv file
df=pd.read_csv("H:\chkingpctgrowth.csv")
df=df.drop(df.index[7])
df['Date'] = pd.to_datetime(df['Date'])

#source creation
source = ColumnDataSource(
data={'Date':df['Date'], 'Checking HHs': df['Checking HHs'], 'Savings HHs':df['Savings HHs'],
'Num HHs': df['Num HHs'], 'Num HHP':df['Num HHP']}
)

hover = HoverTool(tooltips=[('Date', '@Date{%F}'), ('Checking Growth', '@{Checking HHs}{0.000%}'), ('Savings Growth', '@{Savings HHs}{0.000%}')],
formatters={'Date':'datetime'})
hover1 = HoverTool(tooltips=[('Date', '@Date{%F}'), ('Overall Household Growth', '@{Num HHP}{0.000%}')],
formatters={'Date':'datetime'})
#create plot
plot = figure(x_axis_label='Date', x_axis_type='datetime',
y_axis_label='Percentage Growth', title='Percentage Growth 2017-2018 YTD',
tools=[hover, 'pan', 'box_zoom', 'wheel_zoom', 'reset', 'save'])
plot2 = figure(x_axis_label = 'Date', x_axis_type='datetime',
y_axis_label='Total Households', title='Total Household Growth 2017-2018 YTD',
tools=[hover1, 'pan', 'box_zoom', 'wheel_zoom', 'reset', 'save'])
#add lines, shared axis
plot.line('Date', 'Checking HHs', color='navy', source=source, line_width=2, legend=value('Checking HHs'))
plot.line('Date', 'Savings HHs', color='red', source=source, line_width=2, legend=value('Savings HHs'))
plot.legend.location = 'top_right'
plot2.line('Date', 'Num HHP', color='brown', source=source, line_width=2, legend=value('Household Growth'))
plot2.line('Date', 0, color='black', source=source, legend=value('Positive Growth Line'))
plot2.legend.location = 'bottom_left'
plot.x_range=plot2.x_range
plot.y_range=plot2.y_range
#plot2.diamond('Date', 'Num HHP'<0, color='blue', source=source)
layout =row(plot, plot2)
show(layout)
