#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[80]:


census_df= pd.read_csv('census_data_2022.csv')


# In[81]:


type(census_df)


# In[91]:


print(census_df.head())


# In[93]:


# Print the original column names
print(census_df.columns)


# In[94]:


# Rename the columns
census_df = census_df.rename(columns={
    'NAME': 'Zipcode',
    'DP05_0001E': 'Total Population',
    'DP05_0002E':'Total Population Male',
    'DP05_0001M': 'Total Population Margin of Error',
    'DP05_0003E':'Total Population Female',
    'DP05_0004E': 'Sex ratio (males per 100 females)',
    'DP05_0002M': 'Total Population Male Margin of Error',
    'DP05_0002PE':'Total Population Male Percent',
    #'DP05_0002PM':'Male Percent Margin of error',
    'DP05_0003M':'Total Population Female Margin of Error',
    'DP05_0003PE':'Total Population Female Percent',
    #'DP05_0003PM':'Female Percent Margin of error',
    'DP05_0005E': 'Total Population Under 5 years',
    'DP05_0019E': 'Total Population under 18',
    'DP05_0088E': 'Total Housing Units'

    # Add more columns here as needed
})


# In[95]:


# Print the new column names
print("New column names:")
print(census_df.columns)


# In[96]:


census_df=census_df[['Zipcode','Total Population', 'Total Population Male', 'Total Population Female', 'Sex ratio (males per 100 females)','Total Population Male Margin of Error','Total Population Male Percent', 'Total Population Female Margin of Error','Total Population Female Percent', 'Total Population Under 5 years','Total Population under 18','Total Housing Units'      ]]


# In[110]:


print(census_df.head())


# In[98]:


census_df['Zipcode']=census_df['Zipcode'].replace('ZCTA5', '', regex=True)


# <b> Geographic analysis: the distribution of population and housing units across different zip codes. <b>

# In[99]:


geo_df = census_df[['Zipcode', 'Total Population', 'Total Housing Units']]


# In[101]:


# Print the total population and housing units for each zip code
geo_df = geo_df.groupby('Zipcode').sum()
print(geo_df.head())


# In[102]:


geo_df = geo_df.sort_values(by=[ 'Total Housing Units'], ascending=False)


# In[103]:


fig = px.bar(geo_df, x=geo_df.index, y=['Total Population', 'Total Housing Units'], 
             labels={'x':'Zipcode', 'variable':'Metric', 'value':'Count'})

fig.show()


# Neighborhoods with high population density need more resources like housing, schools, hospitals, and public transportation.

# <b>Demographic analysis: calculate ratio to compare the number of Total Population under 18 to Total Population by Zipcode<b>

# In[104]:


census_df['Minor Ratio']=census_df['Total Population under 18']/census_df['Total Population']


# In[105]:


print(census_df.head())


# In[106]:


census_df = census_df.sort_values(by=[ 'Minor Ratio'], ascending=False)


# In[107]:


# Create a bar chart of the minor ratio by Zipcode
fig = px.bar(census_df, x='Zipcode', y='Minor Ratio', title='Minor Ratio by Zipcode')


# In[108]:


fig.show()


# Neighborhoods with higher minor ratio require more investment in education, childcare, and other social services for young people.

# In[109]:


# Write the DataFrame to a new CSV file

census_df.to_csv('new_census_data_2022.csv')

