# Customer-Segmentation-for-Online-Retail
## Project Overview<br/>
Aim is to check out the customers behavior based on the CutomerId,InvoiceNo,Quantity,UnitPriceand Countryetc. This is an unsupervised leaning project.

## Learnings from the project<br/>
### Concepts utilised<br/>

- [x] Data preprocessing<br/> 
- [x] Data Visualisation<br/>
- [x] k means clustering<br/>

## Approach taken to solve the problem<br/>
### Steps involved:

- Subsetting the data. We will be working only on data from United Kingdom.<br/>
-  Create customer-level dataset - The original dataset was organized long, with invoices nested within customer. Our aim is to create a customer-level dataset and add recency, frequency, and monetary value data to it.first calculate the recency. The recency variable refers to the number of days that have elapsed since the customer last purchased something (so, smaller numbers indicate more recent activity on the customer’s account).<br/>
-  Frequency refers to the number of invoices with purchases during the year. Now let's calculate the frequency of purchase.<br/>
-  Calculate the Monetary - Some customers have negative monetary values. These customers probably returned something during the year that they had purchased before the year started.<br/>
-  Standardizing the input variables by taking the log of the features.<br/>
-  Use the elbow method to find the optimum number of clusters.<br/>
-  Use Kmeans to cluster data.<br/>
