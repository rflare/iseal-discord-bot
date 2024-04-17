import discord
async def join_thread(thread):
    embed = discord.Embed(
        title=f"Hello!",
        description=f"**I am a bot, I may not be able to assist you, but please be patient as someone will respond as soon as they can!**",
        color=discord.Color.yellow().value,
    )
    embed.set_footer(
        text="*This bot was made with love by LunarcatOwO*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    await thread.send(embed=embed) # This sends the embed to the thread
    await thread.send("<@905758994155589642> <@398908171357519872>", delete_after=1)
    return
async def welcome(member):
    await member.create_dm()
    embed = discord.Embed(
        title=f"Hello!",
        description=f"**Welcome to the server {member.mention}, if you are looking for the resource pack then run /resourcepack or /resources and it will automatically help you with that. Again welcome to the server and if you have any questions then just ask!**",
        color=discord.Color.yellow().value,
    )
    embed.set_footer(
        text="**Automated message, bot will not be able to respond to any messages** *This bot was made with love by LunarcatOwO*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    await member.dm_channel.send(embed=embed)
    return
