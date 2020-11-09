from bokeh.plotting import figure
from bokeh.io import output_file, show

f = figure(height="500", width="400")

f.background_fill_color = "Red"
f.max_width = 1500
f.max_width = 1000

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

f.line(x, y)
show(f)
output_file("graph.html")
