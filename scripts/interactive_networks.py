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

master = pd.read_csv(r'master.csv', header=None)
vmh_orgs = master[master[10] == 'vmh'][0].str.replace('&nbsp;', '_').values.tolist()

for org in vmh_orgs:
    try:
        df = pd.read_csv('networks/{}/results.csv'.format(org))
        
        dlg = pd.read_csv(r'CSV/{}/DGD.csv'.format(org), header=None)
        tlg = pd.read_csv(r'CSV/{}/TGD.csv'.format(org), header=None)
        
        dlg_clean = dlg.replace("'", "", regex=True)
        tlg_clean = tlg.replace("'", "", regex=True)

        df['subsystem'] = df['subsystem'].astype('category')
        df['sys_labels'] = df['subsystem'].cat.codes
        
        df['type'] = df['genename'].apply(lambda x: 'Double & Triple' if x in dlg_clean.values
                                                                  and x in tlg_clean.values else
                                                    ('Triple' if x in tlg_clean.values else
                                                    'Double')
                                        )
        
        # df['subsystem'] = df['subsystem'].astype('category')
        # df['sys_labels'] = df['subsystem'].cat.codes
        
        G = nx.from_pandas_edgelist(dlg_clean, 0, 1)
        attrs = df.drop_duplicates().set_index('genename').to_dict('index')
        nx.set_node_attributes(G, attrs)
        
        H = nx.from_pandas_edgelist(tlg_clean, 0, 1)
        attrs = df.drop_duplicates().set_index('genename').to_dict('index')
        nx.set_node_attributes(H, attrs)
        
        F = nx.compose(G, H)
        
        #Establish which categories will appear when hovering over each node
        HOVER_TOOLTIPS = [("Gene", "@index"), ("Function", "@subsystem"), ("KEGG ID", "@keggId"),
                          ("Lethal Type", "@type")]
        
        title = 'Lethals Interaction Network - {}'.format(org.replace('_', ' '))
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
        
        graph = from_networkx(F, nx.spring_layout(F, k=0.95/math.log(F.order())), scale=10, center=(0, 0))
        
        
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
        
        output_file("./networks/{}/networkx_graph.html".format(org))
        save(plot)
        
        print(org)
    
    except FileNotFoundError:
        continue;