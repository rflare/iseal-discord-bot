import discord
import functions.checks as checks

# async def cembed(title,content):
#        embed = discord.Embed(title=title, description=content, color=discord.Color.blue().value)
#        return embed

async def rules_embed():    
    embed = discord.Embed(
            title=f"Please read the following rules 🙂",
            description='''1️⃣ **Spam!**
Please dont spam. Nobody likes it and you will get muted.
2️⃣ **Help us to help you!**
If you are reporting a bug/issue, please give plenty of information.
Simply just saying "Help" isn't very useful.
3️⃣ **We have tickets!**
To get individual support, you can open a ticket in the ⁠tickets channel.
4️⃣ **Patience**
When asking for help, please be patient.
I will get to you as soon as possible, but I have a life too. (I know, shocking)
5️⃣ **Tone.** 
Keep a friendly tone and try not to swear, a little is allowed, but dont exagerate''',
            color=discord.Color.blue().value,
        )
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    return embed

async def unspported_embed(plugin_name, interaction, type):
        name, link = await checks.check_plugin(plugin_name, interaction)
        title, content = await checks.check_type(type, name, interaction)
        embed = discord.Embed(
            title=title,
            description=content,
            color=discord.Color.red().value,
        )
        embed.set_footer(
            text="*This bot was made with love by Lunarcat_21*",
            icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
        )
        return embed

async def upgrade_embed(plugin_name, interaction):
        name, link = await checks.check_plugin(plugin_name, interaction)
        embed = discord.Embed(
            title=f"Your {name} is outdated!",
            description=f"Please update your {name} to the newest version",
            color=discord.Color.blue().value,
        )
        embed.add_field(name="Update Link:", value=link, inline=False),
        embed.set_footer(
            text="*This bot was made with love by Lunarcat_21*",
            icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
        )
        return embed

async def format_embed(format_name, interaction):
    content = await checks.check_format(format_name, interaction)
    embed = discord.Embed(
            title=f"Please Provide The Following",
            description=f"{content}",
            color=discord.Color.blue().value,
        )
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    return embed

async def resourcepack_embed(resouce_pack, m_resouce_pack):
    embed = discord.Embed(
            title=f"Hello! Read the following for the resource pack for PowerGems",
            description=f"**Here is the default resourcepack {resouce_pack}, and here is the magic version (not gems) {m_resouce_pack} for it**",
            color=discord.Color.yellow().value,
        )
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    return embed

async def update_embed(name, version, content, interaction):
                pname, plink, role_id = await checks.check_plugin_ui(name, interaction)
                embed = discord.Embed(
                    title=f"{pname} has been updated to {version}!",
                    description=f'''''',
                    color=discord.Color.yellow().value,
                )
                embed.add_field(name="Changes:", value=content, inline=False),
                embed.add_field(name="Update Link:", value=plink, inline=False),
                embed.set_footer(
                    text="*This bot was made with love by Lunarcat_21*",
                    icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
                )
                return embed, role_id

async def config_embed(plugin_name, interaction):
    name,link = await checks.check_plugin(plugin_name, interaction)
    embed = discord.Embed(
            title=f"How to access config.yml for {name}",
            description=f'''First open you're server's file manager
Next head to `~/Plugins/{name}/config.yml`
Then open that file and there should be all the configs for {name}!''',
            color=discord.Color.blue().value,
        )
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    return embed

async def faq_embed(interaction):
    embed = discord.Embed(
            title=f"Frequently Asked Question",
            description=f'''Hello! The questions you have asked are frequently asked questions, and the answers are in <#1219165112519233546>! Please visit there before asking questions next time!''')
    embed.set_footer(
        text="*This bot was made with love by Lunarcat_21*",
        icon_url="https://yt3.googleusercontent.com/XaSpc4tyf4zYIrd3BmMy0Bj9eKk3U5bCQsN3hKySMnQn8Og_xYzxXr4gqeQMOyKGf-AQh8ZZ=s176-c-k-c0x00ffffff-no-rj",
    )
    return embed