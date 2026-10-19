from flask import Flask, render_template, request, redirect
import requests
import sqlite3

app = Flask(__name__) #creates a new web application

APIKey = "80e56bb69b5b76bdccb8df79f57f71dd"

def searchMovies(searchInput):
    url = "https://api.themoviedb.org/3/search/movie" #the URL for the movie database API
    parameters = {
        "api_key": APIKey,
        "query": searchInput 
    } # parameters for the request 
    response = requests.get(url, params=parameters) #sends a request to the API
    data = response.json() 
    return data["results"] #returns the results from the API response

def getDetails(movieId):
    url = f"https://api.themoviedb.org/3/movie/{movieId}" #the URL for the movie database API
    parameters = {"api_key": APIKey} # parameters for the request
    response = requests.get(url, params=parameters) #sends a request to the API
    return response.json()

@app.route("/", methods=["GET", "POST"]) #defines the route for the home page
def home():
    movieList = [] #creates an empty list to store the search results
    if request.method == "POST": 
        searchInput = request.form["movie"]
        movieList = searchMovies(searchInput) #calls the searchMovies function with the search input
    return render_template("index.html" , movies=movieList) #renders the index.html template with the search 

@app.route("/details/<int:movieId>") #defines the route for the details page
def moviePage(movieId):
    movie = getDetails(movieId) #calls the getDetails function with the movie ID
    return render_template("movie.html", movie=movie) #renders the details.html template with the movie details
    
if __name__ == "__main__": 
    app.run(debug=True) 