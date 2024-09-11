import discord
import json
import asyncio
import random
from colorama import Fore, Style, init
from termcolor import colored
import logging
import ctypes
import itertools
import os  


for logger_name in logging.root.manager.loggerDict:
    logging.getLogger(logger_name).disabled = True


init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("Discord Voice Channel Switcher - xz2r")

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

async def print_watermark():
    ascii_art = [
        "██╗  ██╗███████╗██████╗ ██████╗ ",
        "╚██╗██╔╝╚══███╔╝╚════██╗██╔══██╗",
        " ╚███╔╝   ███╔╝  █████╔╝██████╔╝",
        " ██╔██╗  ███╔╝  ██╔═══╝ ██╔══██╗",
        "██╔╝ ██╗███████╗███████╗██║  ██║",
        "╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝",
        "                                ",
        "                       Created by xz2r"
    ]
    
    color_cycle = itertools.cycle(colors) 

    print(f"{Style.BRIGHT}")
    for line in ascii_art:
        colored_line = "".join(colored(char, next(color_cycle)) for char in line) 
        print(colored_line)
        await asyncio.sleep(0.01) 
    print("Giriş yapılıyor...")

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
CATEGORY_ID = int(config['category_id'])

client = discord.Client()

async def setup():
    clear_console() 
    await print_watermark() 

@client.event
async def on_ready():
    print(f"{Fore.CYAN}Giriş yapıldı: {client.user} 🤖")
    client.loop.create_task(random_voice_channel_switcher())

async def random_voice_channel_switcher():
    print(f"{Fore.GREEN}Bot hazır ve çalışıyor! 🔄")
    
    voice_client = None
    while not client.is_closed():
        category = discord.utils.get(client.get_all_channels(), id=CATEGORY_ID, type=discord.ChannelType.category)
        
        if category:
            voice_channels = [channel for channel in category.voice_channels if len(channel.members) > 0]

            if voice_channels:
                random_channel = random.choice(voice_channels)
                
                if voice_client and voice_client.is_connected():
                    await voice_client.disconnect()
                    print(f"{Fore.YELLOW}Kanaldan ayrıldı: {voice_client.channel.name} 🚪")
                
                try:
                    voice_client = await random_channel.connect()
                    print(f"{Fore.GREEN}Kanala katıldı: {random_channel.name} 🎤")
                    
                    await asyncio.sleep(random.uniform(0, 5))
                
                except Exception as e:
                    print(f"{Fore.RED}Hata oluştu: {e} ❗")
            else:
                print(f"{Fore.YELLOW}Dolu ses kanalı bulunamadı. Bekleniyor... ⏳")

        else:
            print(f"{Fore.RED}Kategori bulunamadı: {CATEGORY_ID} ❗")
        
        await asyncio.sleep(random.uniform(0, 5))

asyncio.run(setup())

client.run(TOKEN)
