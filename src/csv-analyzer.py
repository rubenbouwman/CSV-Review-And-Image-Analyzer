from pandas import *

# Reading CSV file
data = read_csv("CSV Files/Bol-product-reviews.csv") # Path to your CSV File

# converting column data to list
# Change the string within [] to the collumn name containing the reviews
reviews = data['score'].tolist()
