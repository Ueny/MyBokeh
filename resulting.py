import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.models.widgets import Select
from bokeh.transform import factor_cmap
from bokeh.models import HoverTool, Title

file1 = 'latimes-state-totals.csv'
file2 = 'cdph-race-ethnicity.csv'

def get_y(cur_data, col_name):
    percent = cur_data[col_name]
    population_percent = cur_data['population_percent']
    y = sum(zip(percent, population_percent), ())
    return y

def get_Xy(data, col_name):
    races = pd.unique(data['race'])
    default_date = '2020-10-14'

    percents = [col_name, 'population_percent']

    cur_data = data[data['date'] == default_date]
    x = [(race, percent) for race in races for percent in percents]
    y = get_y(cur_data, col_name)
    source = ColumnDataSource(data=dict(x=x, y=y))

    # Set up plot
    p = figure(x_range=FactorRange(*x), plot_height=600, title=col_name + " and population_percent by race")
    r = p.vbar(x='x', top='y', width=0.9, line_color='white', source=source,
               fill_color=factor_cmap('x', palette=['#718dbf', '#e84d60'], factors=percents, start=1, end=2))
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    p.add_tools(HoverTool(
        tooltips=[
            ('Object Classification', '@x'),
            ("Percentage", "@y")
        ]
    ))
    p.add_layout(Title(text="Data access: https://github.com/datadesk/california-coronavirus-data",
                       text_font_style="italic"), 'above')
    p.add_layout(Title(text="Data provided by The Times database", text_font_style="italic"), 'above')
    p.add_layout(Title(text="Data access: https://www.cdph.ca.gov/Programs/CID/DCDC/Pages/COVID-19/Race-Ethnicity.aspx",
                       text_font_style="italic"), 'above')
    p.add_layout(Title(text="Data provided by California Department of Public Health", text_font_style="italic"), 'above')
    p.add_layout(Title(text="Data published from the day at latimes.com/coronavirustracker", text_font_style="italic"), 'above')
    p.add_layout(Title(text="Data of last update: 10/15/2020", text_font_style="italic"), 'above')

    return p, r, source

def update_plot1(attrname, old, new):
    cur_data1 = data[data['date'] == datetime1.value]
    y1 = get_y(cur_data1, col_name1)
    r1.data_source.data['y'] = y1

def update_plot2(attrname, old, new):
    cur_data2 = data[data['date'] == datetime2.value]
    y2 = get_y(cur_data2, col_name1)
    r2.data_source.data['y'] = y2

# 3 (a)
data = pd.read_csv(file1)
data = data[['date', 'new_confirmed_cases']]
data = data[(data['date'] >= '2020-08-01') & (data['date'] <= '2020-08-31')]
data['date_time'] = pd.to_datetime(data['date'])
p = figure(x_axis_type='datetime', y_axis_label='New Confirmed Cases',
           title='New confirmed Coronavirus cases in California')
p.line('date_time', 'new_confirmed_cases', source=data, line_width=3, color='#718dbf')
p.circle('date_time', 'new_confirmed_cases', source=data, size=8, color='#e84d60')
p.add_tools(HoverTool(
    tooltips=[
        ('date time', '@date_time{%Y-%m-%d}'),
        ("new cases", "@new_confirmed_cases")
    ],

    formatters={
        '@date_time': 'datetime',
    }
))
p.add_layout(Title(text="Data access: https://github.com/datadesk/california-coronavirus-data", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data available: The Times database", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data provided by local public health agencies", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data published through the day at latimes.com/coronavirustracker", text_font_style="italic"), 'above')
p.add_layout(Title(text="Data of last update: 10/15/2020", text_font_style="italic"), 'above')

# 3 (b)(c)
# Set up data
data = pd.read_csv(file2)
data = data[data['age'] == 'all']
timeline = list(pd.unique(data['date']))

# the first plot
col_name1 = 'confirmed_cases_percent'
p1, r1, source1 = get_Xy(data, col_name1)
datetime1 = Select(title='Datetime', options=timeline, value=timeline[0])
datetime1.on_change('value', update_plot1)

# the second plot
col_name2 = 'deaths_percent'
p2, r2, source2 = get_Xy(data, col_name2)
datetime2 = Select(title='Datetime', options=timeline, value=timeline[0])
datetime2.on_change('value', update_plot2)


# Set up layouts and add to document
curdoc().add_root(row(p, width=1000))
curdoc().add_root(row(p1, column(datetime1), width=1000))
curdoc().add_root(row(p2, column(datetime2), width=1000))
curdoc().title = "Visualizations"
