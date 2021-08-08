from colored import fg, attr
from colorama import Fore, Style
from discord.ext import commands
import os, time, discord, datetime, subprocess, stdiomask, asyncio
class colors:

    red = fg('#ff004d8')
    reset = attr('reset')
    gray = fg('#ff4b00')

asci = """
                                             █████╗ ██████╗  ██████╗  ██████╗ 
                                            ██╔══██╗╚════██╗██╔═████╗██╔═████╗
                                            ╚█████╔╝ █████╔╝██║██╔██║██║██╔██║
                                            ██╔══██╗ ╚═══██╗████╔╝██║████╔╝██║
                                            ╚█████╔╝██████╔╝╚██████╔╝╚██████╔╝
                                             ╚════╝ ╚═════╝  ╚═════╝  ╚═════╝ 
                                       ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
                                        """.replace("█", f"{Fore.LIGHTBLACK_EX}█{colors.gray}")


def get_date_now(time_now):
    return time_now.strftime("%I:%M:%S")

os.system('cls & title 8300')

print(asci)
                                      
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Launching Group Leaver.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Running debug process..""")
time.sleep(1)
hwid = str(subprocess.check_output('wmic csproduct get uuid'), 'utf-8').split('\n')[1].strip()
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Debug{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Completed Debug task.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Machine uuid ({hwid}) is now being utilized.""")
time.sleep(1)
print(f"""{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}Info{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Passed checks, moving foward.""")
time.sleep(1)
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} Client version: 1.0.0 is up to date.")
time.sleep(1)
print(f"{colors.gray}[{colors.gray}{Fore.WHITE}{get_date_now(datetime.datetime.now())}{Fore.WHITE}{colors.gray}] {colors.gray}[{colors.gray}{Fore.WHITE}8300{Fore.WHITE}{colors.gray}] {Fore.LIGHTBLACK_EX} \"thank you for using 8300 Group Leaver for you're task\"")
token = input(f'·{Fore.LIGHTBLACK_EX}√{Fore.LIGHTBLACK_EX} {Fore.WHITE}[{Fore.LIGHTCYAN_EX}{Fore.LIGHTBLACK_EX}{Fore.LIGHTBLACK_EX}{Fore.WHITE}]{colors.gray} Client Token {Fore.WHITE}')
os.system('cls')
client = discord.Client()
prefix = "x"
command = "gl"
leaveMessage = "subscribe to 2ksyrus"

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == prefix + command:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count = count + 1
                        await channel.send(leaveMessage)
                        await channel.leave()
            await message.channel.send("``your left [" + str(count) + "] gc!``")
            await client.logout()
            exit(1)
if __name__ == '__main__':
    try:
        client.run(token, bot=False)
    except:
        os._exit(0)
