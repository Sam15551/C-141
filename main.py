from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
allmovies = movies_data[["original_title","poster_link","release_date","runtime","weighted_rating"]]

# variables to store data
liked_movies = [],
disliked_movies = [],
unwatched_movies = []

# method to fetch data from database
def assign_val():
  m_data = {
    "original_title":allmovies.iloc[0,0],
    "poster_link":allmovies.iloc[0,1],
    "release_date":allmovies.iloc[0,2] or "N/A",
    "runtime":allmovies.iloc[0,3],
    "weighted_rating":allmovies.iloc[0,4]/2
  }
  return m_data

# /movies api
@app.route("/movies")

def get_movies():
  movie_data = assign_val()
  return jsonify({
    "data":movie_data,
    "status":"success"
  })

# /like api
@app.route("/like",methods = ["POST"])

def like():
  global allmovies
  movie_data = assign_val()
  liked_movies.append(movie_data)
  allmovies.drop([0],inplace = True)
  allmovies = allmovies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })


# /dislike api
@app.route("/dislike",methods = ["POST"])

def disliked_movie():
  global allmovies
  movie_data = assign_val()
  disliked_movies.append(movie_data)
  allmovies.drop([0],inplace = True)
  allmovies = allmovies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })



# /did_not_watch api
@app.route("/did_not_watch",methods = ["POST"])

def did_not_watch_movie():
  global allmovies
  movie_data = assign_val()
  unwatched_movies.append(movie_data)
  allmovies.drop([0],inplace = True)
  allmovies = allmovies.reset_index(drop = True)
  return jsonify({
    "status":"success"
  })

if __name__ == "__main__":
  app.run()