# CodeAlpha — Exploratory Data Analysis of Supermarket Sales

## 📊 Project Overview

This project was completed as **Task 2: Exploratory Data Analysis (EDA)** for the **CodeAlpha Data Analytics Internship**.

The analysis explores a supermarket transaction dataset to understand **sales performance, customer behavior, product performance, payment methods, time-based patterns, relationships between variables, and potential data-quality issues**.

The project applies descriptive statistics, data-quality checks, data visualization, correlation analysis, outlier detection, and hypothesis testing to generate meaningful business insights.

---

## 🎯 Objectives

The main objectives of this project are to:

* Understand the structure and data types of the dataset.
* Ask meaningful business questions before performing analysis.
* Identify sales trends, patterns, and anomalies.
* Examine relationships between numerical variables.
* Compare customer groups and business categories.
* Detect potential data-quality issues and unusual observations.
* Perform statistical hypothesis testing.
* Generate meaningful insights from supermarket transactions.

---

## 📁 Dataset

The dataset contains **1,000 supermarket transactions**.

Important variables include:

* Invoice / transaction information
* Branch
* City
* Customer type
* Gender
* Product line
* Unit price
* Quantity
* Tax
* Sales
* Cost of goods sold (COGS)
* Gross margin percentage
* Gross income
* Payment method
* Rating
* Date
* Time

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **SciPy**
* **Jupyter Notebook (ON Colab)**

---

# 🔎 Analysis Performed

## 1. Data Structure and Quality

The dataset was inspected to understand its overall structure and quality.

The analysis included:

* Number of rows and columns
* Data types
* Missing values
* Duplicate records
* Unique categorical values
* Potential unusual observations

---

## 2. Descriptive Statistics

Descriptive statistics were used to understand the distribution and characteristics of numerical variables.

The analysis included:

* Mean
* Median
* Standard deviation
* Minimum
* Maximum
* Quartiles

---

## 3. Product-Line Analysis

Sales and quantity were analyzed across different product lines.

### Key observations

* **Food and Beverages** recorded the highest total sales.
* **Health and Beauty** recorded the lowest total sales.
* **Electronic Accessories** recorded the highest quantity sold.

These results help identify differences between product categories in terms of revenue and sales volume.

---

## 4. Branch Analysis

Total sales were compared across the three supermarket branches.

### Key observation

* **Giza** recorded the highest total sales.
* **Alex** and **Cairo** recorded very similar total sales.

Branch-level analysis helps provide a clearer view of sales distribution across locations.

---

## 5. Customer Analysis

Sales behavior was compared between:

* **Member customers**
* **Normal customers**

### Key observations

* Member customers had more transactions in the dataset.
* Members also had a higher average transaction value.

This comparison helps explore differences in purchasing behavior between customer groups.

---

## 6. Payment Method Analysis

The frequency of different payment methods was examined.

### Key observation

**E-wallet** was the most frequently used payment method, followed closely by **cash**.

This provides insight into customer payment preferences within the dataset.

---

## 7. Relationship Analysis

The relationship between **Quantity** and **Sales** was investigated using correlation analysis.

The analysis produced a correlation coefficient of approximately:

> **r = 0.706**

This indicates a **positive relationship** between quantity purchased and total sales.

In general, transactions with higher quantities tended to have higher total sales values.

However, correlation does not by itself establish causation.

---

## 8. Outlier Analysis

Potential unusual transactions were investigated using:

* Box plots
* Interquartile Range (IQR) method

The analysis identified potential high-value transaction outliers.

These observations were treated as **transactions requiring further investigation rather than automatically being classified as errors**.

---

## 9. Time-Based Analysis

The transaction `Time` variable was converted into an hourly variable to examine sales patterns throughout the day.

### Hourly Sales

* **Peak sales hour:** 19:00
* **Lowest sales hour:** 20:00

### Day-of-Week Analysis

Sales were also analyzed by day of the week.

* **Highest-sales day:** Saturday
* **Lowest-sales day:** Monday

These patterns can help identify periods of relatively higher and lower sales activity.

---

## 10. Hypothesis Testing

An **independent two-sample t-test** was performed to compare the average transaction values between Member and Normal customers.

### Results

| Metric                 |  Result |
| ---------------------- | ------: |
| T-statistic            |  1.8862 |
| P-value                | 0.05957 |
| Significance level (α) |    0.05 |

### Interpretation

The null hypothesis was:

> There is no statistically significant difference in average transaction values between Member and Normal customers.

Because the **p-value (0.05957) is greater than 0.05**, the null hypothesis was **not rejected**.

Therefore, based on this test and at the 5% significance level, there was **insufficient statistical evidence to conclude that the average transaction values differed significantly between Member and Normal customers**.

---

# 📈 Key Insights

The exploratory analysis revealed meaningful differences and patterns across several dimensions:

* **Product performance:** Food and Beverages generated the highest total sales.
* **Sales volume:** Electronic Accessories had the highest quantity sold.
* **Branch performance:** Giza recorded the highest total sales.
* **Customer behavior:** Members had more transactions and a higher average transaction value in this dataset.
* **Payment behavior:** E-wallet was the most frequently used payment method.
* **Quantity and sales:** Quantity and Sales showed a positive correlation of approximately **0.706**.
* **Time patterns:** 19:00 was the peak sales hour, while 20:00 had the lowest sales.
* **Weekly patterns:** Saturday had the highest sales, while Monday had the lowest.
* **Outliers:** Potential high-value transactions were identified for further investigation.
* **Statistical testing:** The t-test did not provide sufficient evidence of a statistically significant difference in average transaction values between Member and Normal customers at the 5% significance level.

---

# 📂 Project Structure

```text
codealpha_exploratory_data_analysis
│
├
│── supermarket_sales.csv
│

│── exploratory_data_analysis.ipynb
│
├── README.md
└── requirements.txt
```

#

---

# 💡 Business Questions Explored

The analysis was guided by practical business questions such as:

1. Which product lines generate the highest sales?
2. Which products have the highest sales volume?
3. Which branch generates the highest total sales?
4. How do Member and Normal customers differ in purchasing behavior?
5. Which payment methods are most frequently used?
6. Is there a relationship between quantity purchased and total sales?
7. Are there unusual or high-value transactions?
8. When do sales peak during the day?
9. Which days of the week generate the highest sales?
10. Is there statistically significant evidence of a difference in average transaction values between customer groups?

---

# 🎓 Internship

This project was completed as part of the:

**CodeAlpha Data Analytics Internship — Task 2: Exploratory Data Analysis**

---

# 👤 Author

**Dawit Tamirat**

**Data Analyst | Aspiring Data Scientist**

---

## 📌 Project Focus

This project demonstrates practical skills in:

**Data Cleaning → Exploratory Data Analysis → Visualization → Statistical Analysis → Business Insights**

It represents an end-to-end exploratory analysis workflow using Python and real-world-style supermarket transaction data.
