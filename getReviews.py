#!/usr/bin/env python
# coding: utf-8

# In[68]:


import requests
import json
import pandas as pd


def getReviews(appid, savePath):

    """

    This function returns a list of user reviews from Steamworks website, convert the
    reviews into Pandas dataframe, then export to .csv file to the savePath

    """

    # Detailed reference for parameters setting, please visit:
    # https://partner.steamgames.com/doc/store/getreviews
    parameters = {"filter":"recent","language":"english", "num_per_page": 100}

    # the target url from which retrieve user reviews
    url = "http://store.steampowered.com/appreviews/" + appid + "?json=1"

    # make a request on api page given by Steamwork
    r = requests.get(url = url, params=parameters)

    # the list of reviews store in json format
    data = r.json()

    # retrieve the list of reviews
    reviews = data["reviews"]

    # convert the reviews from json to dataframe
    df = pd.DataFrame(reviews)

    # export df to .csv file
    df.to_csv(savePath)


if __name__ == "__main__":

    # each game on Steam has an unique ID
    # E.g. game PUBG id is 578080
    appid = input("Please enter the appID of game from Steam database\n")
    savePath = input("Please enter your file save path..e.g \"~/Documents/userReviews.csv\"\n")
    getReviews(appid, savePath)

