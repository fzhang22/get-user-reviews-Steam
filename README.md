## get-user-reviews-Steam
Get user reviews of certain game from Steam using Steamwork. The reviews will be converted into dataframe and exported .csv file to the save path

---

Make sure to install the following packages to run the file:

|packages needed |
|--------------- |
|    requests    |
|    json        |
|    pandas      |

---

Running the Python file, in terminal: `cd filepath` where filepath is the location where you store the .py file. 
E.g `cd "~/Documents/Python/`  then run .py file:   `Python getReviews.py` 

You'll be asked to enter appID of game, each game has its unique appID in Steam databse. For example, appid of game DOTA2 is `570`. Find appID on https://steamdb.info/apps/

Next, you'll be asked to enter the savepath storing exported .csv file. For example, savePath could be `~/Documents/reviews/userReviews.csv`

After sucessfully excuting the file, yourname.csv file will be exported onto save path
