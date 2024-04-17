import discord
import discord.ext
from discord import app_commands 
from discord import ui
import datetime
import os
import src.functions.checks as checks
import src.functions.embed_creator as embeds
import src.functions.auto_messages as auto_messages
from dotenv import load_dotenv
import json

# ---------------------- Variables ---------------------- #
load_dotenv()

file_pg_recpie_new = discord.File('pg_new.png')
file_pg_recpie_upgrade = discord.File('pg_upgrade.png')
file_pg_rp_magic = discord.File('PowerGems_magic_pack.zip')
file_pg_rp_normal = discord.File('Powergems_Pack.zip')
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
allowed_mentions = discord.AllowedMentions(roles = True)

# ---------------------- GUIs ---------------------- #
class WikiSelect(discord.ui.Select):
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
class WikiSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(WikiSelect())

class ResourceSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Resource Pack"),
            discord.SelectOption(label="Recipes")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        print(self.values)
        roles = [role.name for role in interaction.user.roles]
        if self.values == ['Resource Pack']:
                await interaction.response.send_message("Select the plugin that you would like the resource pack for:", view=ResourcePackSelectView(),ephemeral=True)
        elif self.values == ['Recipes']:
                await interaction.response.send_message("Select the plugin that you would like to view the recipes for:", view=RecpieSelectView(),ephemeral=True)
class ResourceSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(ResourceSelect())


class ResourcePackSelect(discord.ui.Select):
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
            name = "PowerGems"
            file_objects = [file_pg_rp_normal, file_pg_rp_magic]
        elif self.values == ['OrePowers']:
            name = "OrePowers"
            return await interaction.response.send_message(content="OrePowers does not have a resource pack. Try selecting another Plugin.", view=ResourcePackSelectView(),ephemeral=True)
            file_objects = []
        elif self.values == ['Valocraft']:
            name = "Valocraft"
            return await interaction.response.send_message(content="Valocraft does not have a resource pack. Try selecting another Plugin.", view=ResourcePackSelectView(),ephemeral=True)
            file_objects = []
        elif self.values == ['ParkourProject']:
            name = "ParkourProject"
            return await interaction.response.send_message(content="ParkourProject does not have a resource pack. Try selecting another Plugin.", view=ResourcePackSelectView(),ephemeral=True)
            file_objects = []
        else:
            return
        roles = [role.name for role in interaction.user.roles]
        if await checks.check_roles(roles) == True:
            await interaction.response.send_message(content=f"Here is the resourcespacks for {name}, select one of the following and install it", view=None, files=file_objects,ephemeral=False)
        else:
            await interaction.response.send_message(f"Here are the resourcepacks for {name}, select one of the following and install it, this message will delete it self after 30 seconds", view=None,  Files=file_objects, delete_after=30,ephemeral=True)

class ResourcePackSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(ResourcePackSelect())

class RecpieSelect(discord.ui.Select):
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
            name = "PowerGems"
            await interaction.response.send_message(content="Select one of the following recpies:", view=PowergemsRecpieSelectView(), ephemeral=True)
            return
        elif self.values == ['OrePowers']:
            name = "OrePowers"
            return await interaction.response.send_message(content="OrePowers does not have a recpies. Try selecting another Plugin.", view=RecpieSelectView(),ephemeral=True)
        elif self.values == ['Valocraft']:
            name = "Valocraft"
            return await interaction.response.send_message(content="Valocraft does not have a recpies. Try selecting another Plugin.", view=RecpieSelectView(),ephemeral=True)
        elif self.values == ['ParkourProject']:
            name = "ParkourProject"
            return await interaction.response.send_message(content="ParkourProject does not have any recpies. Try selecting another Plugin.", view=RecpieSelectView(),ephemeral=True)
        else:
            return

class RecpieSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(RecpieSelect())

class PowergemsRecpieSelect(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="New-Gem"),
            discord.SelectOption(label="Upgrade")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        print(self.values)
        if self.values == ['New-Gem']:
            name = "New Gem"
            file_objects = [file_pg_recpie_new]
        elif self.values == ['Upgrade']:
            name = "Upgrade"
            file_objects = [file_pg_recpie_upgrade]
        else:
            return await interaction.response.send_message(content="Failure, contact LunarcatOwO", ephemeral=True)
        roles = [role.name for role in interaction.user.roles]
        if await checks.check_roles(roles) == True:
            await interaction.response.send_message(content=f"Here is the recpie for {name}", view=PowergemsRecpieSelectView(), files=file_objects)
        else:
            await interaction.response.send_message(f"Here are the recpie for {name}, this message will delete it self after 30 seconds", view=PowergemsRecpieSelectView(),  files=file_objects,delete_after=30)
class PowergemsRecpieSelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(PowergemsRecpieSelect())

class UpdateModal(ui.Modal, title='Information Required'):
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

#---------------------- Commands ----------------------#

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

@tree.command(name='unsupported', description='Sends a message in the current channel, to tell the user to change their server verison/kind')
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
    embed = await embeds.resourcepack_embed(resouce_pack, m_resouce_pack)
    if await checks.check_roles(roles) == True:
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return


@tree.command(name='update', description='Send a message to the current channel for updating a plugin')
async def update(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        await interaction.response.send_modal(UpdateModal())
        return
    else:
        await interaction.response.send_message("You do not have the permission to trigger this command", ephemeral=True)
        return 

@tree.command(name='rp', description='Sends the resourcepack into current channel')
async def rp(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    embed = await embeds.resourcepack_embed(resouce_pack, m_resouce_pack)
    if await checks.check_roles(roles) == True:
        await interaction.response.send_message(embed=embed)
        return
    else:
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return
@tree.command(name='wiki',description='Get the wiki for the plugins')
async def wiki(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    if await checks.check_roles(roles) == True:
        view = WikiSelectView()
        await interaction.response.send_message("Please select the wiki", view=view)
        return
    else:
        view = WikiSelectView()
        await interaction.response.send_message("Please select the wiki", view=view, ephemeral=True)
        return

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

@tree.command(name='r', description='sends the selected resource to the current channel')
async def r(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    await interaction.response.send_message("Select the resource you would like", view=ResourceSelectView(), ephemeral=True)
    return

@tree.command(name='resources', description='sends the selected resource to the current channel')
async def resources(interaction: discord.Interaction):
    roles = [role.name for role in interaction.user.roles]
    await interaction.response.send_message("Select the resource you would like", view=ResourceSelectView(), ephemeral=True)
    return

# ---------------------- Autocompletes ---------------------- #

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
    await auto_messages.join_thread(thread)
    

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
        
@client.event
async def on_member_join(member):
    await auto_messages.welcome(member)


client.run(TOKEN)
