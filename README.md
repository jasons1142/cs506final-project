# cs506final-project

# Project Description
For my project, I will be using Spotify and its features to predict if a new song will chart.

# Goals
Predict if a song will chart based on the features Spotify allows its users to see

# Data Collection
For my project, I will need to collect the audio features of the song I am trying to determine if it will chart. So things like danceability, loudness, duration. Data about the song; genre, release date, artist, features. How well songs did on the charts; position, when it entered the charts, when it left the charts.

# Data Modeling
To model the data, I plan to use logistic regression. By using logistic regression I will be able to give features a score and a weight in determining if they chart. Once they are scored and weighted I can calculate a probability and use that probability as a metric of whether a song charts or not.

# Data Visualization
To visualize the data for my project, I plan to use multiple forms of visualizers. I plan to use histograms to show the audio features that show up in songs that do chart compared to songs that do not chart. I plan to use a correlation matrix to show where songs with similar traits and features tend to land on the charts. I also plan to keep track of streams and time on a graph to see the listens a song is getting while it is charting and while it is not charting. 

# Test
To test I plan to collect a number of songs that have charted to and songs that have not to determine what decides if a song will chart or not. I will then train a model to know the features and weights for determining what charts. Finally I will feed it new songs and its features to determine if that song will chart.
