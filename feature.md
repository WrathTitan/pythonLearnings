# Pre Processing

**Steps Involved in Data Preprocessing:**

**1. Data Cleaning:**
The data can have many irrelevant and missing parts. To handle this part, data cleaning is done. It involves handling of missing data, noisy data etc.

- Missing Data:

  This situation arises when some data is missing in the data. It can be handled in various ways.

  Some of them are:

  1. **Ignore the tuples:**
     This approach is suitable only when the dataset we have is quite large and multiple values are missing within a tuple.
  2. **Fill the Missing values:**
     There are various ways to do this task. You can choose to fill the missing values manually, by attribute mean or the most probable value.

- Noisy Data:

  Noisy data is a meaningless data that can’t be interpreted by machines. It can be generated due to faulty data collection, data entry errors etc. It can be handled in following ways :

  **Binning Method:**
  This method works on sorted data in order to smooth it. The whole data is divided into segments of equal size and then various methods are performed to complete the task. Each segmented is handled separately. One can replace all data in a segment by its mean or boundary values can be used to complete the task.

  1. **Regression:**
     Here data can be made smooth by fitting it to a regression function. The regression used may be linear (having one independent variable) or multiple (having multiple independent variables).
  2. **Clustering:**
     This approach groups the similar data in a cluster. The outliers may be undetected or it will fall outside the clusters.

**2. Data Transformation:**
This step is taken in order to transform the data in appropriate forms suitable for mining process. This involves following ways:

1. **Normalization:**
   It is done in order to scale the data values in a specified range (-1.0 to 1.0 or 0.0 to 1.0)
2. **Attribute Selection:**
   In this strategy, new attributes are constructed from the given set of attributes to help the mining process.
3. **Discretization:**
   This is done to replace the raw values of numeric attribute by interval levels or conceptual levels.
4. **Concept Hierarchy Generation:**
   Here attributes are converted from level to higher level in hierarchy. For Example-The attribute “city” can be converted to “country”.

**3. Data Reduction:**
While working with huge volume of data, analysis became harder in such cases. In order to get rid of this, we uses data reduction technique. It aims to increase the storage efficiency and reduce data storage and analysis costs.

The various steps to data reduction are:

1. **Data Cube Aggregation:**
   Aggregation operation is applied to data for the construction of the data cube.
2. **Attribute Subset Selection:**
   The highly relevant attributes should be used, rest all can be discarded. For performing attribute selection, one can use level of significance and p- value of the attribute.the attribute having p-value greater than significance level can be discarded.
3. **Numerosity Reduction:**
   This enable to store the model of data instead of whole data, for example: Regression Models.
4. **Dimensionality Reduction:**
   This reduce the size of data by encoding mechanisms. It can be lossy or lossless. If after reconstruction from compressed data, original data can be retrieved, such reduction are called lossless reduction else it is called lossy reduction. The two effective methods of dimensionality reduction are: Wavelet transforms and PCA (Principal Component Analysis).

---

# Feature Engineering

## List of Techniques

- Imputation
- Handling Outliers
- Binning
- Log Transform
- One-Hot Encoding
- Grouping Operations
- Feature Split
- Scaling
- Extracting Date

---

#### Imputation

* Missing Values
* Numerical Values missing - Replace the missing values with some numerical value such as Mean, Median, Mode of the column/attribute.
* Categorical Values missing - Replace the missing values with some suitable estimate of the category of the data.

#### Handling Outliers

* Visualise the data and see what data points are out of the distribution of data, etc.
* Or use statistical measures such as standard deviation, 

#### Binning

Binning is done to make the model more **robust** and prevent **overfitting**, however, it has a cost to the performance. Every time you bin something, you sacrifice information and make your data more regularized. 

For example, if your data size is **100,000** rows, it might be a good option to unite the labels with a count less than **100** to a new category like **“Other”**.

#### Log Transformations

- It helps to handle skewed data and after transformation, the distribution becomes more approximate to normal.
- In most of the cases the magnitude order of the data changes within the range of the data.
- It also decreases the effect of the outliers, due to the normalization of magnitude differences and the model become more robust.

#### One Hot Encoding

 This method spreads the values in a column to multiple flag columns and assigns **0** or **1** to them. These binary values express the relationship between grouped and encoded column.

**Why One-Hot?:** If you have **N** distinct values in the column, it is enough to map them to **N-1** binary columns, because the missing value can be deducted from other columns.

#### Grouping Operations

Categorical Column Grouping

- Select the label with the **highest frequency**. 
- Make a **pivot table**. 
- Apply a **group by** function after applying **one-hot encoding**. 

Numerical columns are grouped using **sum** and **mean** functions

#### Feature Splitting

It depends on the characteristics of the column, how to split it.

#### Scaling

The continuous features become identical in terms of the range, after a scaling process

* Normalization (or **min-max normalization**) scale all values in a fixed range between **0** and **1**.
* Standardization (or **z-score normalization**) scales the values while taking into account standard deviation.

#### Extracting Date

- Extracting the parts of the date into different columns: Year, month, day, etc.
- Extracting the time period between the current date and columns in terms of years, months, days, etc.
- Extracting some specific features from the date: Name of the weekday, Weekend or not, holiday or not, etc.

---









