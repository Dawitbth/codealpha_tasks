# CodeAlpha Web Scraping — Books Dataset

## 📌 Project Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship — Task 1: Web Scraping**.

The project uses Python, Requests, BeautifulSoup, and Pandas to collect structured book information from the **Books to Scrape** website.

The scraper automatically navigates through multiple catalogue pages, extracts relevant information, cleans the collected data, performs basic data-quality checks, and saves the final dataset as a CSV file.

## 🎯 Objectives

The main objectives of this project are to:

* Extract structured information from public web pages.
* Use Python and BeautifulSoup for HTML parsing.
* Navigate through multiple web pages automatically.
* Create a structured and reusable dataset.
* Clean and transform scraped data.
* Perform basic data-quality checks.
* Save the final dataset in CSV format for further analysis.

## 📊 Dataset

The final dataset contains **1,000 book records** collected from the website.

The dataset includes the following variables:

| Column         | Description                                          |
| -------------- | ---------------------------------------------------- |
| `Title`        | Title of the book                                    |
| `Price`        | Book price in GBP                                    |
| `Availability` | Availability/stock information                       |
| `URL`          | URL of the individual book page                      |
| `Rating`       | Book rating converted to a numeric scale from 1 to 5 |

## 🛠️ Technologies Used

* **Python**
* **Requests**
* **BeautifulSoup**
* **Pandas**
* **Jupyter Notebook**

## 🔄 Project Workflow

```text
Public Website
      ↓
Requests
      ↓
Download HTML
      ↓
BeautifulSoup
      ↓
Extract Book Information
      ↓
Navigate Multiple Pages
      ↓
Create Pandas DataFrame
      ↓
Clean Price & Rating
      ↓
Data Quality Checks
      ↓
CSV Dataset
```

## 📁 Project Structure

```text
CodeAlpha_WebScraping/
│
├── data/
│   └── scraped_books_dataset.csv
│
├── notebooks/
│   └── Task 1-CodeAlpha.ipynb
│
├── src/
│   └── scraper.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔍 Data Extraction

The scraper extracts:

* Book title
* Price
* Rating
* Availability
* Product URL

BeautifulSoup is used to identify and extract the required information from the HTML structure of each book listing.

## 🧹 Data Cleaning

The scraped data was cleaned before being saved.

### Price

The currency symbol was removed and the price was converted into a numeric format.

### Rating

The original text-based ratings were converted into numerical values:

```text
One   → 1
Two   → 2
Three → 3
Four  → 4
Five  → 5
```

## ✅ Data Quality Checks

The dataset was checked for:

* Missing values
* Duplicate records
* Number of unique titles
* Rating distribution
* Price statistics
* Valid data types

The completed dataset contains **1,000 records across 5 columns**, with all five columns containing non-null values.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd codealpha_webscraping
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the scraper

```bash
cd src
python scraper.py
```

The scraper will collect the available book records and save the resulting dataset in the `data` folder.

## 📓 Jupyter Notebook

The notebook contains the step-by-step development process, including:

1. Sending an HTTP request
2. Parsing HTML with BeautifulSoup
3. Inspecting the webpage structure
4. Extracting book information
5. Handling pagination
6. Creating the DataFrame
7. Cleaning the data
8. Performing data-quality checks
9. Exporting the dataset

## 🌐 Data Source

**Books to Scrape**

The website is a practice website designed for learning web scraping.

## 🎓 Internship

This project was developed for:

**CodeAlpha Data Analytics Internship**

**Task 1 — Web Scraping**

The project follows the internship requirement to extract relevant data from public web pages and create a custom dataset.

## 👤 Author

**Dawit Tamirat**

Data Analyst | Aspiring Data Scientist

---

⭐ This project demonstrates practical skills in web scraping, data collection, data cleaning, and dataset preparation using Python.
