import pandas as pd
import numpy as np
import networkx as nx
import math

from bokeh.io import output_file, show, save
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import figure
from bokeh.plotting import from_networkx
from bokeh.palettes import Plasma256 as palette
from bokeh.transform import linear_cmap
from bokeh.models import EdgesAndLinkedNodes, NodesAndLinkedEdges


df = pd.read_csv('networks/Abiotrophia_defectiva_ATCC_49176/results.csv')
dlg = pd.read_csv(r'CSV/Abiotrophia_defectiva_ATCC_49176/DGD.csv', header=None)

df['subsystem'] = df['subsystem'].astype('category')
df['sys_labels'] = df['subsystem'].cat.codes

G = nx.from_pandas_edgelist(dlg.replace("'", "", regex=True), 0, 1)
attrs = df.drop_duplicates().set_index('genename').to_dict('index')
nx.set_node_attributes(G, attrs)

#Establish which categories will appear when hovering over each node
HOVER_TOOLTIPS = [("Gene", "@index"), ("Function", "@subsystem"), ("KEGG ID", "@keggId")]

title = 'Lethals Interaction Network - Abiotrophia defectiva ATCC 49176'
# color_palette = Blues8
color_by_this_attribute = 'sys_labels'

#Choose colors for node and edge highlighting
node_highlight_color = 'white'
edge_highlight_color = 'black'

#Create a plot — set dimensions, toolbar, and title
plot = figure(tooltips = HOVER_TOOLTIPS,
              tools="pan,tap,wheel_zoom,save,reset", active_scroll='wheel_zoom',
            x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1), title=title)
plot.xaxis.visible=False
plot.yaxis.visible=False
plot.toolbar.logo = None

graph = from_networkx(G, nx.spring_layout(G, k=0.95/math.log(G.order())), scale=10, center=(0, 0))


minimum_value_color = min(graph.node_renderer.data_source.data[color_by_this_attribute])
maximum_value_color = max(graph.node_renderer.data_source.data[color_by_this_attribute])

#Set node size and color
graph.node_renderer.glyph = Circle(size=12, fill_color=linear_cmap(color_by_this_attribute, palette,
                                                                   minimum_value_color,
                                                                   maximum_value_color))
#Set node highlight colors
graph.node_renderer.hover_glyph = Circle(fill_color=node_highlight_color, line_width=2)
graph.node_renderer.selection_glyph = Circle(fill_color=edge_highlight_color, line_width=2)


#Set edge opacity and width
graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)
#Set edge highlight colors
graph.edge_renderer.selection_glyph = MultiLine(line_color=edge_highlight_color, line_width=2)
graph.edge_renderer.hover_glyph = MultiLine(line_color=edge_highlight_color, line_width=2)

    #Highlight nodes and edges
graph.selection_policy = NodesAndLinkedEdges()
graph.inspection_policy = NodesAndLinkedEdges()
plot.renderers.append(graph)

output_file("../networkx_graph.html")
show(plot)