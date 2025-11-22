#cleaning the file:
import pandas as pd
dataset = pd.read_csv("raw_data.csv")
dataset.info()
#check if there are missing values init
dataset.isnull().sum()
#chane the data type
dataset["Order Date"] = pd.to_datetime(dataset["Order Date"])
dataset["Ship Date"]  = pd.to_datetime(dataset["Ship Date"])
#usinhg median to fill out any missing values
dataset["Customer Age"] = dataset["Customer Age"].fillna(dataset["Customer Age"].median())
dataset["Product Base Margin"] = dataset["Product Base Margin"].fillna(dataset["Product Base Margin"].median())
#check agian if there are missing values init
dataset.isnull().sum()
#if all the entries have 0 then congrat there are no missing values
#Fixing the type mistake like upper or lower header
text_columns = [
    "City","Customer Name","Customer Segment","Order Priority",
    "Product Category","Product Sub-Category","Product Container",
    "Region","Ship Mode","State","Product Name"
]
for col in text_columns:
    dataset[col] = dataset[col].str.strip().str.title()
dataset["Zip Code"] = dataset["Zip Code"].astype(str)
dataset.info()
# Save cleaned data to a new CSV file
dataset.to_csv("data_cleaned.csv", index=False, encoding='utf-8')
