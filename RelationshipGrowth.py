import pandas as pd
import matplotlib.pyplot as plt
from bokeh.io import output_file, show, curdoc
from bokeh.models import ColumnDataSource, HoverTool, Slider
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, column, row

dailysl=pd.read_csv("H:\BOKEH DEBUT\SHARE AND LOAN\SL BOKEH VIS.csv")
df = pd.DataFrame(dailysl)
dfd=df.dropna()
dfd['Date'] = pd.to_datetime(df['Date'])

source = ColumnDataSource(
data= {'Date':dfd['Date'], 'TotalShares':dfd['Total Shares'], 'TotalLoans':dfd['Total Loans']}
)
# Create Plots
hover = HoverTool(tooltips=[('Date','@Date{%F}'),('Shares', '@TotalShares{$000,000,000,000}')],
formatters={'Date':'datetime'}
)
hover2 = HoverTool(tooltips=[('Date','@Date{%F}'),('Loans', '@TotalLoans{$000,000,000,000}')],
formatters={'Date':'datetime'}
)
plot = figure(x_axis_label='Date', x_axis_type='datetime', y_axis_label='Total Shares', title='Total Shares - Last 5 Years',
tools=[hover, 'pan', 'box_zoom', 'wheel_zoom', 'reset', 'save'])
plot2 = figure(x_axis_label='Date', x_axis_type='datetime', y_axis_label='Total Loans', title='Total Loans - Last 5 Years',
tools=[hover2, 'pan', 'box_zoom', 'wheel_zoom', 'reset', 'save'])
# Create Widgets

plot.line('Date','TotalShares', color='navy',source=source, line_width=2)
plot2.line('Date', 'TotalLoans', color='red', source=source, line_width=2)
plot.x_range=plot2.x_range
plot.y_range=plot2.y_range
layout = row(plot, plot2)
output_file('bokeh_debut2.html', title='The Bokeh Debut')
show(layout)
