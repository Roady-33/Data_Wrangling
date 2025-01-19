import pandas as pd

films = pd.read_csv("C:/Users/ecgam/Documents/1. Minor HU/Tech/Week 3/Les 2/movie_plots.csv")

# Basic section ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# prints the first few rows of the table, and prints the information per column
print(films.head(), films.info())

# Prints out the number of movies per origin/ethnicity 
print (films["Origin/Ethnicity"].value_counts())

# Subsetting rows only containing Bollywood movies
print (films[films["Origin/Ethnicity"] == "Bollywood"])

# Subsetting rows only containing Turkish movies after 2000
print (films[(films["Origin/Ethnicity"] == "Turkish") & (films ["Release Year"] >= 2000)])

# Make a new df with only Title, Release Year, Origin/Ethnicity, Plot
films_new = films[["Title", "Release Year", "Origin/Ethnicity", "Plot"]]
print (films_new)

# Change column names to Title, Year, Origin and Plot (https://stackoverflow.com/questions/11346283/renaming-column-names-in-pandas) stackoverflow gebruikt
print (films_new.rename(columns={"Release Year": "Year", "Origin/Ethnicity": "Origin"}))

# Advanced part ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a new column "kimono" that is True if the Plot contains the word "kimono" and false if not (tip: find a suitable Pandas string method). 
# Tip: use Pandas .astype(int) to convert the resulting Boolean in 0 or 1.
films ["kimono"] = films["Plot"].str.contains("kimono", case=False).astype(int) # Chatgpt gebruikt voor de string method



