import pandas as pd  # for read, write csv

# read csv file. file should be in same directory with this file.
data = pd.read_csv('good.csv')

# print data. index=False is an option.
print(data.to_string(index=False))

# edit
data['a'][2] = 12345

#test
# write csv file. sep='\t' option means you'll seperate data with tab.
data.to_csv('good2.csv', sep='\t')