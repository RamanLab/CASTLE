import pandas as pd
import requests

df = pd.read_csv('master.csv', header=None)

df = df[df[10] == 'bigg'].reset_index()

orgs = df[0]
url_pres = df[8]

for org, url_pre in zip(orgs, url_pres):
    org = org.replace('&nbsp;', '_')
    
    foldername = "./CSV/{}/SGD.csv".format(org)
    
    genes = pd.read_csv(foldername).values.tolist()
    
    for gene in genes:
        gene = gene[0]
        full_url = '/'.join([url_pre, 'genes', gene])
        
        response = requests.get(full_url).text
        
        with open('example_files/{}_{}.html'.format(org, gene), 'w') as f:
            f.write(response)