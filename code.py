# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# code starts here
df  = pd.read_csv(path)
df.head()

df.isnull().sum()
df = df.dropna(how = 'any')
df.isnull().sum()

df = df[df.Country== 'United Kingdom']
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Return'] = df['InvoiceNo'].str.contains('C')
df['Purchase'] = np.where(df["Return"]==True,0,1)



# code ends here


# --------------
# code starts here
customers = pd.DataFrame(df['CustomerID'].unique(), columns = ['CustomerID'], dtype = int)
customers.head()

df['Recency'] = pd.to_datetime("2011-12-10") - df['InvoiceDate']
df['Recency']

df['Recency'] = df.Recency.dt.days
df['Recency']

df.drop(columns = 'Return', axis = 1, inplace = True)

temp = df[df['Purchase'] == 1]
print(temp.head())

recency = temp.groupby(['CustomerID'], as_index= False).min()

customers = customers.merge(recency[['CustomerID','Recency']])
print(customers.head())



# code ends here


# --------------
# code stars here
temp_1 = df[['CustomerID', 'InvoiceNo', 'Purchase']]
temp_1.drop_duplicates(subset = ['InvoiceNo'], inplace = True)
temp_1.head()

annual_invoice = temp_1.groupby(['CustomerID'], as_index= False).sum()
annual_invoice.head()

temp_1.rename(columns = {'Purchase': 'Frequency'}, inplace = True)

customers = customers.merge(annual_invoice, on = 'CustomerID')

customers.head()

# code ends here


# --------------
# code starts here
df['Amount'] = df['Quantity'] * df['UnitPrice']
df.head()

annual_sales = df.groupby(['CustomerID'], as_index= False).sum()
annual_sales.head()

annual_sales.rename(columns = {'Amount': 'monetary'}, inplace = True)
annual_sales.head()

customers = customers.merge(annual_sales[['CustomerID','monetary']],  on = 'CustomerID')
customers.head()



# code ends here


# --------------
# code ends here
customers['monetary']=np.where(customers['monetary']<0, 0, customers['monetary'])    

customers['Recency_log'] = np.log(customers['Recency'] + 0.1)

customers['Frequency_log'] = np.log(customers['Frequency'])

customers['Monetary_log'] = np.log(customers['monetary'] + 0.1) 

print(customers.head())


# code ends here


# --------------
# import packages
from sklearn.cluster import KMeans


# code starts here
dist = []

for i in range(1, 10):
    km = KMeans(n_clusters=i,init='k-means++', max_iter=300, n_init=10, random_state=0)
    km.fit(customers)
    dist.append(km.inertia_)

fig = plt.figure(figsize=(6,6))
plt.plot(range(1,10),dist)
plt.title("WCSS v/s No. of Clusters")
plt.xlabel("Number of Cluster")
plt.ylabel("WCSS")
plt.show()


# code ends here


# --------------
# code starts here
cluster = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)

customers['cluster'] = cluster.fit_predict(customers.iloc[:,1:7])

customers.plot.scatter(x= 'Frequency_log',y='Monetary_log',c='cluster', colormap='viridis')
plt.title("Clusters")
plt.xlabel("Frequency_log")
plt.ylabel("Monetary_log")
plt.show()

# code ends here


