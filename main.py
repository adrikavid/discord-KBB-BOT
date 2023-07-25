import discord
import requests
import tensorflow as tf
import tensorflow_hub as hub
from discord.ext import commands
import better_profanity

insult_list = ["abruti","niquer sa mère","nique ta mère","va te faire enculer","va te faire foutre","bande d’abrutis","bâtard","bête comme ses pieds","bouffon","bouffonne","bougnoul","bougnoule","branleur","bridé","fils de pute","fdp","sale chien","enculer","ta mère la pute","ta mere la pute", "trou du cul", "narco","négros","negro","négro","nigga","enculer de ta mère la pute","ta gueule fils de pute","ta gueule fdp","sont des putes", "des putes","vous etes des putes","vous êtes des putes","putes","connard","konnard","konnar","konar","batard", "bâtard","brtd","nique ta mere", "ntm","nique sa mere","va niquer ta mere","trou du cul","t'es un trou du cul","sale chien va","sale chien"]

API_KEY = "0103c140cac04dd10681748659b150ec"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

bot = commands.Bot(command_prefix="$", intents=discord.Intents().all())

# Chargement du modèle de détection des insultes
embed = hub.load("https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1")

@bot.event
async def on_ready():
    print(f"{bot.user.name} s'est connecté !")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    for insult in insult_list:
        if insult in message.content:
            await message.channel.send(f"{message.author.mention}, Fais gaffe à ce que tu dis enculer sinon jte ban def trou du cul")
            break

    await bot.process_commands(message)

@bot.command()
async def weather(ctx, *, city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        message = f"Tiens ta météo connard {city_name} : {weather_desc}, Température : {temp}°C, Humidité : {humidity}%, Vitesse du vent : {wind_speed} m/s"
    else:
        message = f"Wsh tu sais même pas écrire ta ville abruti ptdrrr chui mort - Met des tirets la prochaine fois idiot va "

    await ctx.send(message)

bot.run("MTEzMTU1NzY1MjY3ODMyNDM2NQ.GKuF80.tNRxZjjQOLpqVIpEiOA_1ENluBxG16YLHkNa0s")
