# moogDC
moogDC is a repository containing all my Discord Bots, it's purpose is primarily for Python training and personal development, but it's always nice to have some fun with it.

Most of these bots will probably be built with [Discord.py](https://github.com/Rapptz/discord.py), a Discord API wrapper for Python. I may develop bots in other languages in the future.
## NovaBot
NovaBot is a general purpose Discord Bot with many capabilities, named after a close friend, [NovaMortis#8088](https://www.twitch.tv/novamortis_). The original intent of the bot was to just post images of Hatsune Miku - the personification of the Vocaloid voicebank - in a humourous attempt at mocking his passion for her. However, from the development, more comical and satirical bot functions have been introduced. 

### Dependencies
* [Discord.py](https://github.com/Rapptz/discord.py)
* [python_dotenv](https://pypi.org/project/python-dotenv/)
* **OPTIONAL:** [nohup](https://linux.die.net/man/1/nohup)

### Installation
Install Discord.py using pip.
```
python3 -m pip install discord.py
```
Install python_dotenv using pip.
```
python3 -m pip install python_dotenv
```
Add your Discord Token to the DISCORD_TOKEN environment variable using either .env or your system environment variables.
```
EXPORT DISCORD_TOKEN="YOUR DISCORD TOKEN HERE"
```
Run the _app.py file in the moogDC/novaBot directory using nohup.
```
python3 moogDC/novaBot/_app.py
```
Alternatively, the script can be run using [nohup](https://linux.die.net/man/1/nohup) to run in the background.
```
nohup python3 moogDC/novaBot/_app.py &
```
Output from the script will be directed into the working directory under the filename **nohup.out**.