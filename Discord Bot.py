"""
Discord Bot
Taylor N
"""
# Importing the modules
import discord
import random
from discord.ext import commands
from discord.utils import get
import datetime

# Intents allows commands to function with the "." as the command prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = '.', intents = intents)


# A defined function that picks a random picture from my folder and returns it to the original function
def pickPicture():
    num = random.randrange(0, 20)
    img = 'C:/Users/Taylor/Desktop/pics/' + str(num + 1) + '.png'
    return img


# The startup function just so I know that the bot is online and ready to go
def startup():
    @bot.event
    async def on_ready():
        print("Bot is online")
    return


# Multiple arrays of words that are used in arguments for following functions
# PolarQ stands for Polar questions, only returns "yes" or "no"
polarQ = ["is", "isn't", "isnt", "should", "shouldn't", "shouldnt", "do", "don't", "dont", "does", "doesn't",
          "doesnt", "can", "can't", "cant", "did", "didn't", "didnt", "will", "won't", "wont", "was",
          "wasn't", "wasnt"]
what = ["what", "what's", "whats"]
deion = ["deion's", "deions", "deion"]
burp = ["soda", "pop", "pepper", "burp", "rick", "morty"]
pic = ["deion", "daevon", "noied", "dÆvon", "boi", "neon"]
choice = ["rock", "paper", "scissors"]
# list of chosen user IDs of people in my discord server
# The Ids are hidden to keep privacy
people = [123456789101112131, 123456789101112131, 123456789101112131, 123456789101112131, 123456789101112131,
          123456789101112131, 123456789101112131, 123456789101112131, 123456789101112131, 123456789101112131,
          123456789101112131, 123456789101112131]


# The function that reads a user message and checks if any word in that message is in any of the above arrays
def WordsAreInList(list1, list2, specialList):
    check = any(item in list1 for item in list2)
    if not specialList:
        return check
    else:
        check2 = all(item in list1 for item in specialList)
        return check and check2


# Command that removes the "RandomAdmin" role from anyone that has it
@bot.command(pass_context=True)
async def removeRole(ctx):
    guild2 = ctx.message.guild
    roleRandomAdmin = guild2.get_role("Discord Role ID")  # Discord Role ID goes there, hidden for privacy
    RandomAdminM = roleRandomAdmin.members[0]
    print(RandomAdminM)
    await RandomAdminM.remove_roles(roleRandomAdmin)


"""
Command that checks to see if the current time is in between 6:00pm and 11:59pm Sunday then continues to remove the
RandomAdmin role and randomly chooses someone from the previously mentioned "people" list and assigns them with the 
randomAdmin role
"""


@bot.command(pass_context=True)
@commands.has_role("Role ID that can perform this command")  # Discord ID of a role that can use command
async def RandomAdmin(ctx):
    # Gets the current day and hour
    now = datetime.datetime.now()
    today = now.strftime("%A")
    hour = int(now.strftime("%H"))
    if today == 'Sunday':
        if 18 <= hour < 24:
            # Removes the role from the first person in the list created by the RandomAdmin role
            guild2 = ctx.message.guild
            roleRandomAdmin = guild2.get_role("RandomAdmin Role ID number")  # Discord RandomAdmin role ID number
            RandomAdminM = roleRandomAdmin.members[0]
            RandomAdminM_Num = RandomAdminM.id
            mention2 = '<@' + str(RandomAdminM_Num) + '>'
            await RandomAdminM.remove_roles(roleRandomAdmin)
            # Gives random person the RandomAdmin role
            guild = ctx.guild
            RandomAdmin = random.choice(people)
            role = get(guild.roles, id="RandomAdmin Role ID number")
            user = guild.get_member(RandomAdmin)
            mention = '<@' + str(RandomAdmin)+'>'
            await user.add_roles(role)
            await ctx.send(mention2 + " is no longer the RandomAdmin")
            await ctx.send(mention + " is the RandomAdmin of the Week")
            return
        else:
            print("Someone tried to run the command in the wrong hour range")
            return
    else:
        print("Someone tried to run the command, but it is not Sunday")
        return


# Events that the bot is always looking for
def events():
    @bot.event
    async def on_message(message):  # on_message() is a function that looks at every single message that goes through the text chat
        channel = message.channel
        if message.author == bot.user:  # This is here so the bot doesn't respond to itself
            return

        # Rock, Paper, Scissors
        # looks at the message and looks to see if any word from the "rps" array are present along with the required word "rps"
        if WordsAreInList(message.content.lower().split(), choice, ["rps"]):
            x = random.randrange(0, 9)
            if x == 1:
                xx = random.randrange(0, 3)
                if xx == 0:
                    await message.channel.send("You have bested the bot")
                    return
                if xx == 1:
                    await message.channel.send("This has literally never happened.. I lost")
                    return
                if xx == 3:
                    await message.channel.send("*sigh* I've made a severe and continuous lapse of my judgement")
                    return
            # The game is designed for the player to lose most of the time
            elif x != 1:
                await message.channel.send("Nope, You lost")
                y = random.randrange(0, 5)
                if y == 1:
                    await message.channel.send("Get fucked, Pussy")
                    return
                else:
                    return

        # Random is here just to prevent the bot from talking all of the time, now it's only 1/3 of the time
        rand = random.randrange(0, 3)
        """
        Checks the message and looks to see if any word from the "PolarQ" array are present and if so sends a random
        response of "yes", "no", or "Mayhaps". This is the exact way that the next 2 events work.
        """
        if rand == 1:
            if WordsAreInList(message.content.lower().split(), polarQ, []):
                randomNum = random.randrange(0, 3)
                if randomNum == 0:
                    await message.channel.send("Yes")
                elif randomNum == 1:
                    await message.channel.send("No")
                else:
                    await message.channel.send("Mayhaps")

            if WordsAreInList(message.content.lower().split(), what, ["up"]):
                await message.channel.send("The opposite of down")

            if WordsAreInList(message.content.lower().split(), burp, []):
                await message.channel.send("*burp* Morty")

            """
            This event only triggers if the word "dp" is in the message so we don't need the array. 
            The bot sends the "*burp* morty" text along with a picture from my folder.
            This is similar to how the last 3 events work
            """

            if message.content.lower().find("dp") != -1:
                await message.channel.send("*burp* Morty")
                await channel.send(file=discord.File('C:/Users/Taylor/Desktop/pics/dp.jpg'))

            if message.content.lower().find("you know what they say") != -1:
                await message.channel.send("All toasters toast toast")
                await channel.send(file=discord.File('C:/Users/Taylor/Desktop/pics/toast.jpg'))

            if message.content.lower().find("help") != -1:
                await message.channel.send("1) Have you tried turning it off and back on again?")
                await message.channel.send("2) Did you check?")
                await message.channel.send("3) When's the last time you checked?")
                await message.channel.send("4) Have you tried turning it off and back on again? Again?")

            if WordsAreInList(message.content.lower().split(), pic, []):
                await channel.send(file=discord.File(pickPicture()))

        """
        After every message is sent it is assigned 2 random numbers. The 1 out of 50 "randA" and the 1 out of 500,
        "randB". If "randA" is equal to 1, it'll send a reply in the chat "Wow, this is rare". If "randB" is equal to 1,
        it'll reply with "This is really rare!". And if both "randA" and "randB" are 1, then it'll reply with "The
        previous message had only a .02% of happening".
        """
        if message.content.lower() != -1:
            randA = random.randrange(0, 50)
            randB = random.randrange(0, 500)
            if randA == 1:
                await message.channel.send("Wow, this is rare")
            if randB == 1:
                await message.channel.send("This is really rare!")
            if randA == 1 and randB == 1:
                await message.channel.send("The previous message had only a .02% of happening")

        # This is required for the bot to read commands along with events
        await bot.process_commands(message)


# The entrance to the program
if __name__ == "__main__":
    startup()
    events()

# A bot key, mine is hidden for privacy
bot.run('Your Bot Tokken')
