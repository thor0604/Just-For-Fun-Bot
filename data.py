"""stores data such as possible user inputs and API keys"""

TOKEN = {TOKEN} # replace here

HI = (
    'hello',
    'hi',
    'hey',
    'ello',
    'bonjour'
)

HELP = (
    "`Say hi to the bot!`\n"
    "`!help: to get help menu`\n"
    "`!inspire: to get inspired`\n"
    "`!roll: to roll a dice`\n"
    "`!image[query]: replace [query] with a phrase to search for an image`\n"
    "`!weatherLabege: to get weather forecast for Labège`\n"
    "`!weatherGrenoble: to get weather forecast for Grenoble`\n"
    "`!startgame: to start a cumber comparison game`\n"
    "`/add [music]: to add music into queue`\n"
    "`/play: to play music in voice channel`\n"
    "`/pause: to pause music`\n"
    "`/queue: to see list of songs in queue`\n"
    "`/skip: to skip the current song`\n"
    "`/clear: to clear the queue`\n"
    "`/leave: to leave voice channel`\n"
)

API_KEY_WEATHER = {API_KEY_WEATHER} # replace here
API_GOOGLE = {API_GOOGLE} # replace here
CX_GOOGLE_IMAGE = {CX_GOOGLE_IMAGE} # replace here

# add more cities here
CITY_DATA = {
    'Labege': {
        'lat' : 43.53432096887032,
        'lon' : 1.5177019830925111
    },
    'Grenoble': {
        'lat' : 45.183230638352256,
        'lon' : 5.7562940921331345
    }
}