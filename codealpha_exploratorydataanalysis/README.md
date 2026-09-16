\# CodeAlpha — Exploratory Data Analysis of Supermarket Sales



\## Project Overview



This project was completed as \*\*Task 2: Exploratory Data Analysis (EDA)\*\* for the CodeAlpha Data Analytics Internship.



The analysis explores a supermarket transaction dataset to understand sales performance, customer behavior, product performance, payment methods, time-based patterns, relationships between variables, and potential data-quality issues.



The project applies descriptive statistics, data-quality checks, visualization, correlation analysis, outlier detection, and hypothesis testing.



\## Objectives



The analysis aims to:



\* Understand the structure and data types of the dataset.

\* Ask meaningful business questions before analysis.

\* Identify trends, patterns, and anomalies.

\* Examine relationships between numerical variables.

\* Test a statistical hypothesis.

\* Detect potential data-quality issues.

\* Generate meaningful insights from supermarket transactions.



\## Dataset



The dataset contains \*\*1,000 supermarket transactions\*\*.



Important variables include:



\* Invoice/customer transaction information

\* Branch

\* City

\* Customer type

\* Gender

\* Product line

\* Unit price

\* Quantity

\* Tax

\* Sales

\* Cost of goods sold (COGS)

\* Gross margin percentage

\* Gross income

\* Payment method

\* Rating

\* Date

\* Time



\## Technologies Used



\* Python

\* Pandas

\* NumPy

\* Matplotlib

\* Seaborn

\* SciPy

\* Jupyter Notebook



\## Analysis Performed



\### 1. Data Structure and Quality



The dataset was inspected for:



\* Number of rows and columns

\* Data types

\* Missing values

\* Duplicate records

\* Unique categorical values

\* Potential unusual observations



\### 2. Descriptive Statistics



Statistical measures including:



\* Mean

\* Median

\* Standard deviation

\* Minimum

\* Maximum

\* Quartiles



were used to understand the numerical variables.



\### 3. Product Analysis



Sales and quantity were analyzed across product lines.



Key observations included:



\* Food and beverages had the highest total sales.

\* Health and beauty had the lowest total sales.

\* Electronic accessories recorded the highest quantity sold.



\### 4. Branch Analysis



Total sales were compared across branches.



Giza recorded the highest total sales, while Alex and Cairo had very similar totals.



\### 5. Customer Analysis



Sales behavior was compared between Member and Normal customers.



Members had more transactions and a higher average transaction value in the dataset.



\### 6. Payment Analysis



Payment-method usage was examined.



E-wallet was the most frequently used payment method, followed closely by cash.



\### 7. Relationship Analysis



The correlation between Quantity and Sales was examined.



The analysis produced a correlation coefficient of approximately \*\*0.706\*\*, indicating a positive relationship between quantity purchased and total sales.



\### 8. Outlier Analysis



Box plots and the Interquartile Range (IQR) method were used to identify potential high-value transaction outliers.



Potential outliers were treated as observations requiring further investigation rather than automatically being classified as errors.



\### 9. Time-Based Analysis



The transaction time was converted into an hourly variable to identify sales patterns throughout the day.



Key observations:



\* Peak sales hour: \*\*19:00\*\*

\* Lowest sales hour: \*\*20:00\*\*



Sales were also analyzed by day of the week.



\* Highest-sales day: \*\*Saturday\*\*

\* Lowest-sales day: \*\*Monday\*\*



\### 10. Hypothesis Testing



An independent two-sample t-test was performed to compare average transaction values between Member and Normal customers.



Results:



\* \*\*T-statistic:\*\* 1.8862

\* \*\*P-value:\*\* 0.05957

\* \*\*Significance level:\*\* 0.05



Since the p-value was greater than 0.05, the null hypothesis was not rejected. Therefore, there was insufficient statistical evidence at the 5% significance level to conclude that average transaction values differed significantly between the two customer groups.



\## Key Insights



The analysis demonstrated meaningful differences in:



\* Product-line sales

\* Sales volume

\* Branch performance

\* Customer behavior

\* Payment-method usage

\* Hourly sales activity

\* Day-of-week sales



The analysis also identified a positive relationship between quantity and sales and highlighted potential high-value transactions for further investigation.



\## Project Structure



```text

CodeAlpha\_ExploratoryDataAnalysis/

│

├── data/

│   └── supermarket\_sales.csv

│

├── notebooks/

│   └── exploratory\_data\_analysis.ipynb

│

├── README.md

├── requirements.txt

└── .gitignore

```



\## How to Run



Clone the repository:



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



Move into the project directory:



```bash

cd CodeAlpha\_ExploratoryDataAnalysis

```



Install the required packages:



```bash

pip install -r requirements.txt

```



Launch Jupyter Notebook:



```bash

jupyter notebook

```



Open:



```text

notebooks/exploratory\_data\_analysis.ipynb

```



and run the notebook cells sequentially.



\## Internship



This project was completed as part of the \*\*CodeAlpha Data Analytics Internship — Task 2: Exploratory Data Analysis\*\*.



\## Author



\*\*Dawit Tamirat Higissa\*\*



Data Analytics | Python | Data Science



