# Jungle Jive

Jungle Jive is a bot used in my friends and I's personal discord server. It checks to see if a song was already posted in our 'Jungle Jive' channel. Using the command jj.history, it will scan all links in the specified channel and put them into a sqlite database. If a song link is then posted that has already been posted, it will send a message that has the original author, date posted, and a jump link to view the original post. If a song that has not been posted before is posted, it will add it to the database with the the relevant data.

If you would like to use this, all you need to change is the channel id in the music.py and add in your api key.

Run create_db.py to create the database and then run the command jj.history to populate the database with links in the channel of your choosing.



 
