# -*- coding: utf-8 -*-

#Author: Godwin

import pandas as pd

df = pd.read_csv('movie_dataset.csv')

#Renaming colunm

df.columns = ['Rank', 'Title', 'Genre', 'Description', 'Director', 'Actors', 'Year', 'Runtime_minutes',
             'Rating', 'Votes', 'Revenue_millions', 'Metascore']

#Drop Rank column
df.drop(['Rank'], inplace=True, axis=1)

#Change Year to proper integer format
df['Year'] = df['Year'].astype(int) 

#Finding mean to replace empty sells in Revenue_millions column 
revenue_ave = df["Revenue_millions"].mean()
df["Revenue_millions"].fillna(revenue_ave, inplace=True)

#Finding mean to replace empty sells in Metascore column
metascore_ave = df["Metascore"].mean()
df["Metascore"].fillna(metascore_ave, inplace=True)

#Adding a new 'Rank' column that starts from 1
df['Rank'] = df.index + 1
#making this Rank the first column
df = df[['Rank'] + [col for col in df.columns if col != 'Rank']]

#Saving the cleaned data removing the panda index
df_clean = df.to_csv("movie_dataset_cleaned.csv", index=False)
print(df_clean)

#calling clean data to answer the questions.
df_clean = pd.read_csv("movie_dataset_cleaned.csv")



# Answers to the Project Quiz


# Question 1: What is the highest rated movie in the dataset?

highest_rated_movie = df_clean[df_clean['Rating'] == df_clean['Rating'].max()]
print("Highest Rated Movie:")
print(highest_rated_movie[['Title', 'Rating']])




# Question 2: What is the average revenue of all movies in the dataset?
average_revenue = df_clean['Revenue_millions'].mean()
print(f"Average Revenue of All Movies: ${average_revenue:.2f} million")


# Question 3: What is the average revenue of movies from 2015 to 2017 in the dataset?
movies_2015_to_2017 = df_clean[(df_clean['Year'] >= 2015) & (df_clean['Year'] <= 2017)]
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue_millions'].mean()
print(f"Average Revenue of Movies from 2015 to 2017: ${average_revenue_2015_to_2017:.2f} million")




# Question 4: How many movies were released in the year 2016?
movies_2016 = df_clean[df_clean['Year'] == 2016]
count_movies_2016 = movies_2016.shape[0]
print(f"Number of Movies Released in 2016: {count_movies_2016}")





# Question 5: How many movies were directed by Christopher Nolan?
nolan_movies = df_clean[df_clean['Director'] == 'Christopher Nolan']
count_nolan_movies = nolan_movies.shape[0]
print(f"Number of Movies Directed by Christopher Nolan: {count_nolan_movies}")




# Question 6: How many movies in the dataset have a rating of at least 8.0?
high_rated_movies = df_clean[df_clean['Rating'] >= 8.0]
count_high_rated_movies = high_rated_movies.shape[0]
print(f"Number of Movies with Rating of at least 8.0: {count_high_rated_movies}")



# Question 7: What is the median rating of movies directed by Christopher Nolan?
median_nolan_rating = nolan_movies['Rating'].median()
print(f"Median Rating of Movies Directed by Christopher Nolan: {median_nolan_rating}")





# Question 8: Find the year with the highest average rating.
avg_rating_by_year = df_clean.groupby('Year')['Rating'].mean()
year_highest_avg_rating = avg_rating_by_year.idxmax()
highest_avg_rating = avg_rating_by_year.max()
print(f"Year with the Highest Average Rating: {year_highest_avg_rating} with a rating of {highest_avg_rating:.2f}")




# Question 9: Percentage increase in number of movies made between 2006 and 2016
movies_2006 = df_clean[df_clean['Year'] == 2006].shape[0]
movies_2016 = df_clean[df_clean['Year'] == 2016].shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"Percentage Increase in Number of Movies Made between 2006 and 2016: {percentage_increase:.2f}%")




# Question 10: Find the most common actor in all the movies
all_actors = df_clean['Actors'].str.split(',').explode().str.strip()
most_common_actor = all_actors.value_counts().idxmax()
print(f"Most Common Actor: {most_common_actor}")



# Question 11: How many unique genres are there in the dataset?
unique_genres = df_clean['Genre'].str.split(',').explode().str.strip().nunique()
print(f"Number of Unique Genres: {unique_genres}")












