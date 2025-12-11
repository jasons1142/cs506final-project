# cs506final-project

# YouTube Link
https://www.youtube.com/watch?v=y2IRj6gmKVw

# Midterm Report

  I created preliminary visualizations to understand relationships between Spotify streaming data and Billboard chart performance. The correlation heatmap shows that Spotify Streams and Popularity are negatively correlated with Billboard Peak Position, meaning songs with higher streams tend to chart higher. The plot showing the relationship between streams and peak position on the Billboard chart also shows that songs with higher streams tend to do better on the charts.
  I cleaned and processed the data by standardizing column names, converting date fields, and merging Spotify and Billboard data. My Spotify dataset had a large number of metrics, so I narrowed down the ones I used to metrics like Spotify streams, Spotify popularity, TikTok views, and YouTube views. My Billboard dataset had songs dating back all the way to 1958, so I used the year in the chart_week metric to only have songs that charted in 2024. I then merged the dataset by song title and artist name to create a dataset with things like Spotify Streams and YouTube views of a song linked to the song’s peak position on the Billboard charts.
	I created a correlation heatmap to visualize the relationships between Spotify metrics and Billboard Peak Position. I then used a linear regression model to quantify how each Spotify feature influences chart position and evaluate predictive performance. Model performance was assessed using R² and Mean Absolute Error. 
  My preliminary results show that there is a strong correlation between having higher Spotify streams and lower Billboard position (which is good because you are at the top of the charts). Things like high Spotify popularity and high YouTube Views also tend to indicate better performance on the charts. The linear regression model achieved an R² of 0.41 and a mean absolute error of 16, indicating that streams explain about 41% of the variance in peak chart position. Although not the best as this project progresses, I will add more metrics to better predict song placement.

# How To Build and Run Code
## Clone the Repository
git clone git@github.com:jasons1142/cs506final-project.git  
cd notebooks  
open 01_data_cleaning.ipynb  

## Set up the Project
make

## Run the Notebook
make run

## Run test
make test

## Clean Outputs
make clean

# Data Visualization 
<img width="1092" height="857" alt="image" src="https://github.com/user-attachments/assets/f99d9232-7ff2-4a84-9398-485b4192640f" />
<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/0aa96fb5-5b00-4ba4-87a9-188a0a3e57fc" />
<img width="571" height="455" alt="image" src="https://github.com/user-attachments/assets/cc16aee2-6bcd-4bdc-8387-544f474f2fbe" />
<img width="581" height="455" alt="image" src="https://github.com/user-attachments/assets/d38c365d-3ae8-4776-b4dd-619921548f29" />

Here I have data showing the correlations between some of the features I used and how well it performs on the charts.


# Final Report
For my final project, I used a 2024 dataset of songs and created a model to try and predict how well songs would perform based on streaming numbers of songs in 2024 and how high they charted. For my data processing, I downloaded the datasets and started by trying to make them consistent. To do this, I got rid of things like spaces, capitalization, and punctuation. I also renamed some of the features of the datasets to be consistent with one another, changing the artist and song name in both datasets to be artist and track. Finally, I picked a group of specific features and the year 2024 in my datasets and combined them into one dataset for training and testing.
For my data modeling, my goal was to take 2024 song data and determine what makes a song either be top10, top50, top100, or not chart. I would then pick a random month in 2024 for predicting whether the song would chart based on the data of all the songs for that month. In modeling, I made sure to exclude the month I chose, which was May, to avoid bias. For my first two models, I tried linear and logistic regression, which performed poorly. I believe Linear and Logistic Regression failed for me because all my metrics are hard to use linearly or in a binary manner, meaning the models would never perform well. The model I had the most success with was RandomForest, but even it struggled initially. When I was just trying to classify things evenly, it struggled with the disproportionate amount of songs that did not chart at all. To fix this, I ran the RF twice, once for songs that do not chart at all and again for songs that did chart. Doing this helped the model to better predict songs that did not chart vs songs that were either top100, top50, or top10.

#Results
Two-Stage Model: May 2024 Prediction Results

              precision    recall  f1-score   support

    LowChart       0.80      0.99      0.88       146
       Top10       0.82      0.53      0.64        17
      Top100       0.38      0.23      0.29        13
       Top50       1.00      0.25      0.40        32

    accuracy                           0.79       208
   macro avg       0.75      0.50      0.55       208
weighted avg       0.80      0.79      0.75       208


