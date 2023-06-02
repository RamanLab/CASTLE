import os
import pandas as pd
import numpy as np
import math
from collections import Counter

import networkx as nx
from bokeh.io import output_file, show
from bokeh.plotting import figure, from_networkx

import requests
from matplotlib import pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx

master = pd.read_csv(r'master.csv', header=None)
vmh_orgs = master[master[10] == 'vmh'][0].str.replace('&nbsp;', '_').values.tolist()
# gene_functions = {}

for idx, org in enumerate(vmh_orgs):   
    result_dicts = []
    try:
        dlg = pd.read_csv(r'CSV/{}/DGD.csv'.format(org), header=None)
        tlg = pd.read_csv(r'CSV/{}/TGD.csv'.format(org), header=None)
        
        for id_, gene in enumerate(pd.unique(np.append(dlg.values.ravel(), tlg.values.ravel()))):
            response = requests.post(''.join(['http://vmh.life/_api/microbegenereactions/', gene.replace("'", "")]))
            subsystems = []
            for result in response.json()['results']:
                subsystems.append(result['subsystem'])
                
            result['subsystem'] = Counter(subsystems).most_common(1)[0][0]
            result['genename'] = gene.replace("'", "")
            result_dicts.append(result)
            print(id_)

        # G=nx.from_pandas_edgelist(dlg, 0, 1)
        
        # plot = figure(title="Networkx Integration Demonstration", x_range=(-1.1,1.1), y_range=(-1.1,1.1),
        #               tools="", toolbar_location=None)

        # graph = from_networkx(G, nx.spring_layout, scale=2, center=(0,0))
        # plot.renderers.append(graph)
        
        # output_file("../networkx_graph.html")
        # show(plot)
        # H=nx.from_pandas_edgelist(tlg, 0, 1, 2)
        
        # if not os.path.isdir('networks/{}'.format(org)):
        #     os.mkdir('networks/{}'.format(org))
            
        # nx.write_edgelist(G, "networks/{}/DLG.edgelist".format(org), data=False)
        # nx.write_edgelist(H, "networks/{}/TLG.edgelist".format(org), data=False)
        # You were missing the position.
        # pos=nx.spring_layout(G)
        # val_map = dict(zip(gene_functions.keys(), pd.Series(gene_functions.values()).factorize()[0]))
        # #I had this list for the name corresponding t the color but different from the node name
        # ColorLegend = dict(zip(pd.Series(gene_functions.values()).factorize()[1], range(len(pd.Series(gene_functions.values()).factorize()[1]))))
        # values = [val_map.get(node, 0) for node in G.nodes()]
        # # Color mapping
        # jet = cm = plt.get_cmap('jet')
        # cNorm  = colors.Normalize(vmin=0, vmax=max(values))
        # scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)
        
        # # Using a figure to use it as a parameter when calling nx.draw_networkx
        # f = plt.figure(1, figsize=())
        # ax = f.add_subplot(1,1,1)
        
        # for label in ColorLegend:
        #     ax.plot([0],[0],color=scalarMap.to_rgba(ColorLegend[label]),label=label)
        
        # # Just fixed the color map
        # nx.draw_networkx(G, pos, cmap = jet, vmin=0, vmax= max(values),node_color=values,with_labels=False,ax=ax)
        
        # # Setting it to how it was looking before.                                                                                                              
        # plt.axis('off')
        # f.set_facecolor('w')
        
        # plt.legend()
        
        # f.tight_layout()
        # plt.show()
        
        # # nx.draw_networkx(G, with_labels=False, pos=nx.spring_layout(G, k=0.5), 
        # #                  nodelist=gene_functions.keys(), 
        # #                  node_color=pd.Series(gene_functions.values()).factorize()[0])
        # # plt.show()
        # # plt.savefig('networks/{}/DLG.png'.format(org), dpi=300, bbox_inches='tight')
        # # plt.close()
        
        # # nx.draw(H, with_labels=True, pos=nx.spring_layout(H, k=5/math.sqrt(H.order())),
        # #         font_size=8, font_color='blue', node_size=100, node_color='yellow', node_shape='s')
        # # plt.savefig('networks/{}/TLG.png'.format(org), dpi=300, bbox_inches='tight')
        # # plt.close()
        
        pd.DataFrame(result_dicts).to_csv('networks/{}/results.csv'.format(org), index=None)
        print(org)
        
        # break;
        
    except:
        continue;
    
    
