from video_detector import df
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)
print(df)
p = figure(width=500, height=400, x_axis_type="datetime", title="Video Capture Graph")
p.yaxis.minor_tick_line_color = None
# p.ygrid[0].ticker.desired_num_ticks = 1

tooltip = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(tooltip)
q = p.quad(left="Start", right="End", top=1, bottom=0, color="green", source=cds)

output_file("video_capture_graph.html")

show(p)
