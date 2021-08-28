# -*- coding: utf-8 -*-
import pandas as pd
import os
import networkx as nx

import requests
from bs4 import BeautifulSoup

master = pd.read_csv("master.csv", header=None)
master_vmh = master[master[10] == 'vmh']
master_bigg = master[master[10] == 'bigg']

def get_string_ids(model, lgenes):
    uniprot_ids = []
    
    for lgene in lgenes:
        url = '/'.join([model, 'genes', lgene])
        bigg_url = requests.get(url)
        bigg_html = BeautifulSoup(bigg_url.text, 'html.parser')
        old_id = bigg_html.find_all('ul')[-1].text.strip()
        uniprot_ids.append(old_id)
        
        # string_url = 'https://string-db.org/api/tsv/get_string_ids'
        # results = requests.post(string_url, data={"identifiers":old_id})
        # print(results.text)
        
        # for line in results.text.strip().split("\n"):
        #     l = line.split("\t")
        #     string_identifier = l[2]
            
        # string_ids.append(string_identifier)
        
    return uniprot_ids

def write_network(idx, node_number, edges):
    G=nx.complete_graph(node_number)
    nodenames = edges
    mapping = {i:nodename for i,nodename in enumerate(nodenames)}
    
    H=nx.relabel_nodes(G,mapping)
    
    if not os.path.isdir('networks/{}'.format(test.iloc[0])):
        os.mkdir('networks/{}'.format(test.iloc[0]))
    nx.write_edgelist(H, 'networks/{}/{}.edgelist'.format(test.iloc[0], idx), data=False)
    
            
test = master_bigg.iloc[0]
csv = pd.read_csv('CSV/{}/DGD.csv'.format(test.iloc[0]), header=None)

for idx in csv.index:
    line = csv.loc[idx]
    uniprot_ids = get_string_ids(test.iloc[8], line.tolist())
    write_network(idx, 2, uniprot_ids)