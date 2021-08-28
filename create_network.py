import os
import pandas as pd
import math

import networkx as nx
from matplotlib import pyplot as plt

for idx, org in enumerate(os.listdir(r'CSV/')):
    try:
        dlg = pd.read_csv(r'CSV/{}/DGD.csv'.format(org), header=None)
        tlg = pd.read_csv(r'CSV/{}/TGD.csv'.format(org), header=None)
        
        G=nx.from_pandas_edgelist(dlg, 0, 1)
        H=nx.from_pandas_edgelist(tlg, 0, 1, 2)
        
        if not os.path.isdir('networks/{}'.format(org)):
            os.mkdir('networks/{}'.format(org))
            
        nx.write_edgelist(G, "networks/{}/DLG.edgelist".format(org), data=False)
        nx.write_edgelist(H, "networks/{}/TLG.edgelist".format(org), data=False)
        
        nx.draw(G, with_labels=True, pos=nx.spring_layout(G, k=5/math.sqrt(G.order())),
                font_size=8, font_color='blue', node_size=100, node_color='yellow', node_shape='s')
        plt.savefig('networks/{}/DLG.png'.format(org), dpi=300, bbox_inches='tight')
        plt.close()
        
        nx.draw(H, with_labels=True, pos=nx.spring_layout(H, k=5/math.sqrt(H.order())),
                font_size=8, font_color='blue', node_size=100, node_color='yellow', node_shape='s')
        plt.savefig('networks/{}/TLG.png'.format(org), dpi=300, bbox_inches='tight')
        plt.close()
        
        print(idx+1)
        
    except FileNotFoundError:
        continue;
    
    
