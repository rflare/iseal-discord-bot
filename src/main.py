import discord
import discord.ext
from discord import app_commands 
from discord import ui
import datetime
import os
import src.functions.checks as checks
import src.functions.embed_creator as embeds
import src.functions.threads as threads
from dotenv import load_dotenv

load_dotenv()

owners = [905758994155589642,398908171357519872]
plugins =  ['PowerGems', 'OrePowers','Valocraft', 'ParkourProject']

TOKEN = os.getenv('DISCORD_TOKEN')

resouce_pack = "https://cdn.discordapp.com/attachments/1157658269318402058/1193993804672421918/Powergems_Pack.zip?ex=65e61b62&is=65d3a662&hm=bdbf0cb227153b960c702d07ba3e6ba14fb562f6f4d16941a52e4934fdbe1000&"
resouce_pack_location = 'https://canary.discord.com/channels/1157645386480091156/1157658269318402058/1193993805012140103'
m_resouce_pack = "https://cdn.discordapp.com/attachments/1157658269318402058/1194529976645582858/PowerGems_magic_pack.zip?ex=65e80ebb&is=65d599bb&hm=64738d3ea8e369d425a53a06c34103a923db83a88902cebfb5e455ee5badc9b8&"


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync() #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ISeal's Server"))
        print(f"We have logged in as {self.user}.")


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name='rules', description='Sends the rules in the current channel', )
async def rules(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.rules_embed()
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@tree.command(name='unsupported', description='Sends a message in the current channel, to tell the user to change their server verison/kind', )
async def unsupported(interaction: discord.Interaction, plugin_name:str, type:str):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.unspported_embed(plugin_name, interaction, type)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@tree.command(name='upgrade', description='Sends a message in the current channel to tell user to update their plugin', )
async def upgrade(interaction: discord.Interaction, plugin_name:str):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.upgrade_embed(plugin_name, interaction)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@tree.command(name='format', description='Send a message to the current channel for the user to fix their format', )
async def format(interaction: discord.Interaction, format_name:str):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.format_embed(format_name, interaction)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@tree.command(name='resourcepack', description='Send the resource pack link to the current channel (PowerGems)')
async def resourcepack(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.resourcepack_embed(resouce_pack, m_resouce_pack)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return


@tree.command(name='update', description='Send a message to the current channel for updating a plugin')
async def update(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        allowed_mentions = discord.AllowedMentions(roles = True)
        class Questionnaire(ui.Modal, title='Information Required'):
            name = ui.TextInput(label='Name of plugin')
            version = ui.TextInput(label='Version of update')
            content = ui.TextInput(label='Content of update', style=discord.TextStyle.paragraph)
            async def on_submit(self, interaction: discord.Interaction):
                embed, role_id = await embeds.update_embed(self.name, self.version, self.content, interaction)
                role = interaction.guild.get_role(role_id)
                if role_id == 0:
                    await interaction.response.send_message(content="Failed to find plugin name (required to ping memebers) please try again", ephemeral=True)
                    return
                else:
                    await interaction.response.send_message(content=f"||{role.mention}||", embed=embed, allowed_mentions=allowed_mentions)
                    return
        await interaction.response.send_modal(Questionnaire())
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return 

@tree.command(name='rp', description='Sends the resourcepack into current channel')
async def rp(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.resourcepack_embed(resouce_pack, m_resouce_pack)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

# @tree.command(name='embed', description='Creates a custom embeded message')
# async def update(interaction: discord.Interaction):
#     roles = [role.name for role in interaction.user.roles]
#     if await checks.check_roles(roles) == True:
#         class Questionnaire(ui.Modal, title='Information Required'):
#             title = ui.TextInput(label='Title')
#             content = ui.TextInput(label='Description', style=discord.TextStyle.paragraph)
#             async def on_submit(self, interaction: discord.Interaction):
#                 embed = await embeds.cembed
#                 await interaction.response.send_message(embed=embed)
#                 return
#         await interaction.response.send_modal(Questionnaire())
#         return
#     else:
#         await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
#         return 



@tree.command(name='wiki',description='Get the wiki for the plugins')
async def wiki(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        view = SelectView()
        await interaction.response.send_message("Please select the wiki", view=view)
        return
    else:
        view = SelectView()
        await interaction.response.send_message("Please select the wiki", view=view, ephemeral=True)
        return
class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="PowerGems"),
            discord.SelectOption(label="OrePowers"),
            discord.SelectOption(label="Valocraft"),
            discord.SelectOption(label="ParkourProject")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        print(self.values)
        if self.values == ['PowerGems']:
            link = "https://powergems.iseal.dev"
            name = "PowerGems"
        elif self.values == ['OrePowers']:
            # link = "https://orepowers.iseal.dev"
            link = "Unavailable"
            name = "OrePowers"
        elif self.values == ['Valocraft']:
            # link = "https://valocraft.iseal.dev"
            link = "Unavailable"
            name = "Valocraft"
        elif self.values == ['ParkourProject']:
            # link = "https://parkourproject.iseal.dev"
            link = "Unavailable"
            name = "ParkourProject"
        else:
            return
        roles = [role.name for role in interaction.user.roles]
        if await checks.check_roles(roles) == True:
            await interaction.response.edit_message(content=f"Here is the wiki link to {name}: {link}", view=None)
        else:
            await interaction.response.send_message(f"Here is the wiki link to {name}: {link}", ephemeral=True)
class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@tree.command(name="config", description="Send how to access the config file")
async def config(interaction: discord.Interaction, plugin_name:str):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.config_embed(plugin_name, interaction)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@tree.command(name='faq' , description='Send the FAQ in the current channel')
async def faq(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        embed = await embeds.faq_embed(interaction)
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return

@config.autocomplete('plugin_name')
async def config_id_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> 'list[app_commands.Choice[str]]':
    names = plugins
    return [
        app_commands.Choice(name=names, value=names)
        for names in names if current.lower() in names.lower()
    ]

@unsupported.autocomplete('plugin_name')
async def unsupported_id_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> 'list[app_commands.Choice[str]]':
    names = plugins
    return [
        app_commands.Choice(name=names, value=names)
        for names in names if current.lower() in names.lower()
    ]

@unsupported.autocomplete('type')
async def unsupported_id_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> 'list[app_commands.Choice[str]]':
    names = ['version', 'modded']
    return [
        app_commands.Choice(name=names, value=names)
        for names in names if current.lower() in names.lower()
    ]

@upgrade.autocomplete('plugin_name')
async def upgrade_id_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> 'list[app_commands.Choice[str]]':
    names = plugins
    return [
        app_commands.Choice(name=names, value=names)
        for names in names if current.lower() in names.lower()
    ]

@format.autocomplete('format_name')
async def format_id_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> 'list[app_commands.Choice[str]]':
    names = ['bug', 'suggestion']
    return [
        app_commands.Choice(name=names, value=names)
        for names in names if current.lower() in names.lower()
    ]

@client.event
async def on_thread_join(thread):
    await threads.join_thread(thread)
    

@client.event
async def on_message(message): # This event triggers when a message is sent anywhere
    if client.user.mentioned_in(message):
        await message.reply(f"**I am a bot, can not assist you! If you want to report a bug put it in https://discord.com/channels/1157645386480091156/1157659553345831012 if you have a suggestion put it in https://discord.com/channels/1157645386480091156/1157664317932584970 **")
    if isinstance(message.channel, discord.DMChannel):
        if message.author == client.user:
            return
        await message.reply(f"**I am a bot, can not assist you! If you want to report a bug put it in https://discord.com/channels/1157645386480091156/1157659553345831012 if you have a suggestion put it in https://discord.com/channels/1157645386480091156/1157664317932584970 **")
    if isinstance(message.channel, discord.Thread): # If the message is in a thread, we check if the bot is in it
        if not any(member.id == client.user.id for member in message.channel.members): # If the bot is not in the thread, we join it
            await message.channel.join()
            return

client.run(TOKEN)