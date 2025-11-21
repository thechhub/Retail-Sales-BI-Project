# Retail-Sales-BI-Project

A complete end-to-end data analysis project using Python, SQL, and Power BI.
This project demonstrates real industry skills, including data cleaning, exploratory data analysis, business intelligence, statistical insights, and dashboard development.
The dataset contains 8,400+ rows of Walmart retail performance from 2012, including sales, profit, product categories, regions, discounts, and customer behavior.

🔥 Project Goals

This project aims to:

Analyze sales performance and profitability across products & regions
Identify trends, seasonality, and peak demand periods
Detect the most profitable product categories
Understand customer buying patterns
Build a business-ready dashboard for decision-making
Demonstrate real-world skills in Python, SQL, data cleaning, visualization, and BI tools

📁 Dataset

After converting from Excel, the dataset is stored as:

walmart_sales_2012.csv
Columns Included
Date / Time
Category
Product name / Product ID
Sales
Profit
Cost
Orders
Customers
Discount
Margin
Region / Location
...and more (A → Y columns in original file)

Data Format
File type: CSV UTF-8 (Comma delimited)
Rows: 8,400+
Timeframe: 2012

🧰 Tools & Technologies Used
Programming & Analysis
Python
Pandas
NumPy
Matplotlib / Seaborn
Jupyter Notebook
Database
SQL / SQLite (or MySQL/PostgreSQL depending on your setup)
Business Intelligence
Microsoft Power BI (free to use Power BI Desktop)
🛠 Project Workflow

1️⃣ Data Collection
Raw XLSX file converted to CSV UTF-8
Verified for encoding, formatting, and missing values

2️⃣ Data Cleaning (Python)
Handling missing values
Converting dates
Removing duplicates
Standardizing column names
Fixing data types (numeric columns, date columns, categorical columns)
Feature engineering (month, year, day, profit margin, etc.)

3️⃣ Exploratory Data Analysis (EDA)
Sales trends over time
Profit distribution
Category-wise performance
Regional insights
Customer-level analysis
Correlation heatmaps
Detecting outlier

4️⃣ SQL Analysis
Top-selling categories
Region-wise revenue
Monthly/quarterly breakdown
Most profitable products
High-discount vs low-discount performance

5️⃣ Visualization & BI Dashboard
Created using Power BI:
Sales trends
Profit by category
Regional performance
Discount impact on sales
Customer purchase behavior

📈 Key Insights (Example placeholders)
These will update once your analysis is done:
X% of total revenue came from Category A
Region South/West/East had the highest profit margin
Discounts increased sales by Y%, but reduced profit by Z%
The last quarter of 2012 showed the highest demand

📦 Project Structure
📁 walmart-sales-analysis
│
├── 📄 README.md
├── 📂 data
│   └── walmart_sales_2012.csv
│
├── 📂 notebooks
│   ├── 1_data_cleaning.ipynb
│   ├── 2_eda.ipynb
│   └── 3_sql_queries.ipynb
│
├── 📂 dashboards
│   └── powerbi_dashboard.pbix
│
└── 📂 src
    ├── cleaning.py
    ├── analysis.py
    └── visualization.py

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/thechhub/Retail-Sales-BI-Project
cd walmart-sales-analysis

2. Install Required Libraries
pip install -r requirements.txt

3. Run Jupyter Notebook
jupyter notebook

4. Open the Power BI Dashboard

Open powerbi_dashboard.pbix using Power BI Desktop.

🎯 Skills Demonstrated
Data cleaning (industry level)
Exploratory data analysis
SQL querying
Business intelligence dashboarding
Python automation scripts
Data storytelling and insight generation
Git & GitHub workflow

📬 Contact

If you would like to discuss this project or collaborate, feel free to reach out!
