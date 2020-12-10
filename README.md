
### Overview

#### Code

[Matrix Factorization](matrix_factorization.md)

[Word2Vec](word2vec.md)

#### Data

**Scrapped Data**
Follow the instructions below to scrape the data

**Spotify Million Playlist**
The dataset can be accessed [here](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)




### Installation

#### Setup
Create virtual environment, activate it, and install dependencies:

*From inside the repo directory:*
```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

*Note: You can deactivate the virtual environment:* `deactivate`

Create dataset directoriess:

```
mkdir -p datasets/spotify
mkdir datasets/spotify2018
```

#### Authentication

In order to use the Spotify API we need to provide it with credentials. Navigate to 
[My Dashboard](https://developer.spotify.com/dashboard/applications) and create a new app. After creating the app,
you should see `Client ID` and `Client Secret`.

Save these credentials so that the crawler can use them. Replace `{Client ID}` and `{Client Secret}` with your newly 
created credentials.
```
echo "export SPOTIPY_CLIENT_ID={Client ID}" >> .auth
echo "export SPOTIPY_CLIENT_SECRET={Client Secret}" >> .auth
```

Now your `.auth` file should now look something like this:

```
export SPOTIPY_CLIENT_ID=an1XGYYM87XKEaFlyow9lv5nyJpo7Xri
export SPOTIPY_CLIENT_SECRET=Tgjg6yp93VqfqZXBUlUXtB2gcbdufMTW
```



You should now be all set to run: `./run_scraper.sh`.
