from motion_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource
import pandas

# start_test = df["Start"]
# # print(start_test)

# for time in start_test:
#     print(time)

df["Start_string"] = pandas.to_datetime(
    df["Start"]).dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = pandas.to_datetime(
    df["End"]).dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=500, width=500,
           sizing_mode="stretch_width", title="Motion Graph")

hover = HoverTool(
    tooltips=[("Start", "@Start_string"), ("End", "@End_string")])

p.add_tools(hover)

p.yaxis.minor_tick_line_color = None
# It will remove x axis grid line (its not a typo it removes x axis grid lines)
# p.ygrid.grid_line_color = None
p.ygrid.visible = False

# p.ygrid.ticker.desired_num_ticks = 1 # Not working

q = p.quad(top=1, right='End', bottom=0,
           left='Start', color="green", source=cds)

output_file("Graph1.html")
show(p)
