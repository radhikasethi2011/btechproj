import pandas as pd 

colnames=['FoldID', 'EventID', 'seq', 'Bound'] 
df = pd.read_csv('Data/datasetpy/non_motif.txt', delimiter = ' ',  names = colnames, header=None)
print(df.head())

df.set_index('FoldID')

df.to_csv(r'Data/datasetpy/sampledataset1.seq', index=None, sep=' ', mode='a')