import discord
async def join_thread(thread):
    embed = discord.Embed(
        title=f"Hello!",
        description=f"**I am a bot, I may not be able to assist you, but please be patient as someone will respond as soon as they can!**",
        color=discord.Color.yellow().value,
    )
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    await thread.send(embed=embed) # This sends the embed to the thread
    await thread.send("<@905758994155589642> <@398908171357519872>", delete_after=1)
    return