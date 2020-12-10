### Code Overview

#### Scraped Spotify Data

[Cleaning the Data](cleaning_scraped.ipynb)
This notebook will take in data from `datasets/spotify/spotify_scraped_dataset.csv` and then output the cleaned data 
to `datasets/spotify/spotify_cleanded_dataset.csv`

[Pre-processing the Data](preprocess_scraped.ipynb)
This notebook will take in data from `datasets/spotify/spotify_cleaned_dataset.csv` and then output two different 
files. Song information is saved to `datasets/spotify/songs.csv`, the list of playlists is saved to 
`datasets/spotify/playlists.npy`.

[Training & Recommending](recommender_scraped.ipynb)
This notebook will take in data from `datasets/spotify/songs.csv` and `datasets/spotify/playlists.npy`. Then, you can
train the model and start recommending songs!


#### Spotify Million Playlist Data

[Cleaning the Data](preprocess_spotify2018.ipynb)
This notebook will take in data from `datasets/spotify2018/spotify_million_playlist_dataset.zip` and then output two 
different files. Song information is saved to `datasets/spotify2018/songs.csv`, the list of playlists is saved to 
`datasets/spotify2018/playlists.npy`.

[Training & Recommending](recommender_spotify2018.ipynb)
This notebook will take in data from `datasets/spotify/songs.csv` and `datasets/spotify/playlists.npy`. Then, you can
train the model and start recommending songs!



