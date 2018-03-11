
# coding: utf-8

# ### Analyzing the Stroop Effect
# Perform the analysis in the space below. Remember to follow [the instructions](https://docs.google.com/document/d/1-OkpZLjG_kX9J6LIQ5IltsqMzVWjh36QpnP2RYpVdPU/pub?embedded=True) and review the [project rubric](https://review.udacity.com/#!/rubrics/71/view) before submitting. Once you've completed the analysis and write up, download this file as a PDF or HTML file and submit in the next section.
# 
# 
# (1) What is the independent variable? What is the dependent variable?

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('pylab', 'inline')

stroop_data=pd.read_csv('stroopdata.csv')
stroop_data.head()


# --write answer here--<br>
# independent variable is not affected by other so it is the congruency of the  words<br>
# dependent variable is  affected by other so it is the response time

# (2) What is an appropriate set of hypotheses for this task? What kind of statistical test do you expect to perform? Justify your choices.

# --write answer here--<br>
# a.H0:μ_congruent = μ_incongruent there is no difference in the mean of the response time to read the words<br><br>
#   HA:  μ_congruent ≠ μ_incongruent there is  difference in the mean of the response time to read the words<br><br>
#   μ_congruent is the population mean of the response time to read congruent words<br><br>
#   μ_Incongruent is the population mean of the response time to read incongruent words<br><br>
# b.we used dependent samples t-test. because we test the relationship between two related variables and the dataset is small (equals 24)
# 

# (3) Report some descriptive statistics regarding this dataset. Include at least one measure of central tendency and at least one measure of variability. The name of the data file is 'stroopdata.csv'.

# In[2]:


# Perform the analysis here

#mean of congruent
c_mean =stroop_data['Congruent'].mean()


#mean of Incongruent
i_mean=stroop_data['Incongruent'].mean()


#the standard deviation of Congruent 
c_std=stroop_data['Congruent'].std()


#the standard deviation of Incongruent 
i_std=stroop_data['Incongruent'].std()

c_mean,i_mean,c_std,i_std


# --write answer here--

# (4) Provide one or two visualizations that show the distribution of the sample data. Write one or two sentences noting what you observe about the plot or plots.

# In[3]:


# Build the visualizations here

plt.hist((stroop_data['Congruent'],stroop_data['Incongruent']), 20, color=['red', 'green'], label=['Congruent','Incongruent'], alpha=0.75)
plt.legend(prop={'size': 10})

plt.title('Congruent and Incongruent')
plt.ylabel('Frequency')
plt.xlabel('Time')

plt.show()


# --write answer here--<br>
# The response time of Incongruent is less than Ccongruent

# (5) Now, perform the statistical test and report the results. What is the confidence level and your critical statistic value? Do you reject the null hypothesis or fail to reject it? Come to a conclusion in terms of the experiment task. Did the results match up with your expectations?

# In[31]:


#confidence level =95%

#degree of freedoms = 24-1 =23

#t-crtitical from t-table =2.069

#the difference between the means

diff_mean=i_mean -c_mean 

#to find the standard deviation we divide the sum of squares by n minus 1, then we take the square root

stroop_data['DIFF'] = stroop_data['Congruent'] - stroop_data['Incongruent']


diff_f_mean= stroop_data['DIFF'] - stroop_data['DIFF'].mean()

#we get the squares 
stroop_data['Sqr_diff'] = diff_f_mean*diff_f_mean

#the sum of squares
Sqrd_diff = stroop_data['Sqr_diff'].sum()

#the length of observations

n=len(stroop_data)

#the variance by dividing the sum of squares by n minus 1
variance = Sqrd_diff/(n-1)

#finally calculate the standard deviation
from math import *
std = sqrt(variance)


#t-statistic

t = diff_mean/(std/(sqrt(n)))
t


# --write answer here--<br>
# 
# we find the t-statistic is bigger than the t-critical so we reject the Null Hypothesis which states that there is no difference in the mean of the response time to read the words
