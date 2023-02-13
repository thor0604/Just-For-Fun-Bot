# Bot Just For Fun
This bot contains several random functions. I've developed this bot to learn how APIs and asynchonise programming works. This bot is strictly for personal use only and several improvements can be made.

## Instruction
1. Download all files 
2. Create a discord bot from Discord Developper site.
3. Replace all the data in *data.py* such as TOKEN and API_KEYS.
4. Include this bot in server using the invitation link generated when creating bot.
5. Execute *main.py*
6. Enjoy!

## Functions
a. Greetings 
As a start, I've learnt how to set up a very simple bot that greets user everytime a user says *hello*.

b. Roll a dice
Secondly, this simple function uses python random module to generate an integer between 1 and 6. 
Type *!roll* to use this function.

c. Inspirational quotes
Third, I learnt to get data using a simple API request from Zenquotes. One does not need an API key to use this API.
User can get a random quote by typing *!inspire* in a text channel.

d. Weather forecast
Third, I tried to develop my own commands to get the weather forecast from OpenWeather API. 
From here, I've learnt to manipulate JSON file format and use try and error method to find the exact data I want in the JSON data received. By default, there are two cities which are Grenoble and Labège. One can add more cities by adding its longtitude and latitude in *data.py* then mimic the functions in *responses.py*. One has to create an account with OpenWeather to get an API key and stores it in *data.py*.
Type *!weatherGrenoble* for example to get the forecast for the city of Grenoble

d. Image finder
Forth, I've integrated an image finder to this bot by using BIG QUERY API from Google. One has to create an account with Google and store his API key in *data.py* to use this function. This function returns an image in user's discord channel.
Type *!image [query]* to upload an image to discord text channel

e. Number Comparison game
Fifth, I tried to integrate a simple game into this bot. I remembered one of the first games I've developed is the number comparison game. An integer(target) is generated randomly from 1 to 100 and user has to guess the number. At each guess, the bot will tell the user whether the number is greater than or smaller than or equals to the target.
Type *!startgame* to play this game!

f. Music
Finally, since most of the music bot has been banned on Discord, I told myself to develop one myself to apply everything I've learnt. It wasn't easy and there're many things that can be improved. But here's what it looks like:) 
User can add any songs they want in queue by typing */add [query]* and this bot uses Youtubev3 API from Google to search the video online. Similarly, one has to create an account with Google in order to generate an API key which has to be include in *data.py*. This key can be similar to the one used in image finder. It then returns a list of results and we will be taking the first in the list.
User can then play the songs in queue with */play* command. The bot will then download the music from the url and convert it into discord readable format using ffmpeg. By default, I've named it *audio.mp3* and it will be replaced each and everytime a new song is downloaded. Check out othe functions using *!help* command.

## To be improved
- This bot contains global variables that stores data such as list of songs on queue and game target which is not ideal if it's deployed in several discord servers.