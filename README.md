# cs506final-project

# YouTube Link
https://www.youtube.com/watch?v=y2IRj6gmKVw

# Midterm Report

  I created preliminary visualizations to understand relationships between Spotify streaming data and Billboard chart performance. The correlation heatmap shows that Spotify Streams and Popularity are negatively correlated with Billboard Peak Position, meaning songs with higher streams tend to chart higher. The plot showing the relationship between streams and peak position on the Billboard chart also shows that songs with higher streams tend to do better on the charts.
  I cleaned and processed the data by standardizing column names, converting date fields, and merging Spotify and Billboard data. My Spotify dataset had a large number of metrics, so I narrowed down the ones I used to metrics like Spotify streams, Spotify popularity, TikTok views, and YouTube views. My Billboard dataset had songs dating back all the way to 1958, so I used the year in the chart_week metric to only have songs that charted in 2024. I then merged the dataset by song title and artist name to create a dataset with things like Spotify Streams and YouTube views of a song linked to the song’s peak position on the Billboard charts.
	I created a correlation heatmap to visualize the relationships between Spotify metrics and Billboard Peak Position. I then used a linear regression model to quantify how each Spotify feature influences chart position and evaluate predictive performance. Model performance was assessed using R² and Mean Absolute Error. 
  My preliminary results show that there is a strong correlation between having higher Spotify streams and lower Billboard position (which is good because you are at the top of the charts). Things like high Spotify popularity and high YouTube Views also tend to indicate better performance on the charts. The linear regression model achieved an R² of 0.41 and a mean absolute error of 16, indicating that streams explain about 41% of the variance in peak chart position. Although not the best as this project progresses, I will add more metrics to better predict song placement.

