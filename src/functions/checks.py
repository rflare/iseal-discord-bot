pgv = "1.19.4"
vv = "1.19.4"
opv = "1.19.4"
ppv = "1.19.4"



trigger_roles = ["Trusted", "ISeal"]




async def check_plugin(plugin_name, interaction):
        if plugin_name.lower() == "powergems" or plugin_name.lower() == "pg": 
            name = "PowerGems"
            link = "https://www.spigotmc.org/resources/108943/"
        elif plugin_name.lower() == "valocraft" or plugin_name.lower() == "v":
            name = "Valocraft"
            link = "https://www.spigotmc.org/resources/115131/"
        elif plugin_name.lower() == "orepowers" or plugin_name.lower() == "op":
            name = "OrePowers"
            link = "https://www.spigotmc.org/resources/113941/"
        elif plugin_name.lower() == "parkourproject" or plugin_name.lower() == "pp":
            name = "ParkourProject"
            link = "www.spigotmc.org/resources/115478/"
        else:
            await interaction.response.send_message(f"Failed to find the name of the plugin, please try again", ephemeral=True)
            return None, None
        return name, link

async def check_roles(roles):
    if any(role in roles for role in trigger_roles):
        return True
    else:
        return False


async def check_type(type, name, interaction):
        if type.lower() == 'm' or type.lower() == 'modded':
            title = '''UNSUPPORTED TYPE OF MINECRAFT!'''
            content = (f'**{name} and any plugin in this server does not support to be used as a mod as mods and servers are two different things! Please put {name} in a server running on a Minecraft server software that supports plugins (Suggested PaperMC)**')
        elif type.lower() == 'v' or type.lower() == 'version':
            if name == 'PowerGems':
                title = f'PowerGems does not support the version of minecraft you are on!'
                content = f'PowerGems does not support the version of minecraft you are on as that it is only compatible with versions {pgv} or above!'
            elif name == 'OrePowers':
                title = f'OrePowers does not support the version of minecraft you are on!'
                content = f'OrePowers does not support the version of minecraft you are on as that it is only compatible with versions {opv} or above!'
            elif name == 'Valocraft':
                title = f'Valocraft does not support the version of minecraft you are on!'
                content = f'Valocraft does not support the version of minecraft you are on as that it is only compatible with versions {vv} or above!'
            elif name == 'ParkourProject':
                title = f'ParkourProject does not support the version of minecraft you are on!'
                content = f'ParkourProject does not support the version of minecraft you are on as that it is only compatible with versions {ppv} or above!'
            else:
                await interaction.response.send_message(f"Failed to find the name of the plugin or the spsific kind/version you are looking for, please try again", ephemeral=True)
                return None, None
        return title, content

async def check_format(format_name, interaction):
        if format_name.lower() == "bug" or format_name.lower() == 'b':
            content = '''*General information*
Server software:
Server version:
Software build (if you don't know just dont add this):
Plugins on the server:

*Plugin information*
Plugin:
Plugin version:
Errors in the console (if any, preferably use paste.md-5.net): 

*Bug*
Expected result:
Actual result:
Things tried:

*also attach config.yml file*'''
        elif format_name.lower() == 'suggestion' or format_name.lower() == 's':
            content = '''**Plugin Name**:
What to add:
How it is currently (*Optional*):
Why should it be added:
Extra information:'''
        
        else:
            await interaction.response.send_message("Failed to find format, please try again", ephemeral=True)
            return None, None
        return content

async def check_plugin_ui(plugin_name, interaction):
        plugin_name = f"{plugin_name}"
        if plugin_name.lower() == "powergems" or plugin_name.lower() == "pg": 
            pname = "PowerGems"
            plink = "https://www.spigotmc.org/resources/108943/"
            role_id = 1158015875744551003
        elif plugin_name.lower() == "valocraft" or plugin_name.lower() == "v":
            pname = "Valocraft"
            plink = "https://www.spigotmc.org/resources/115131/"
            role_id = 1201124609060245555
        elif plugin_name.lower() == "orepowers" or plugin_name.lower() == "op":
            pname = "OrePowers"
            plink = "https://www.spigotmc.org/resources/113941/"
            role_id = 1185692151716270121
        elif plugin_name.lower() == "parkourproject" or plugin_name.lower() == "pp":
            pname = "ParkourProject"
            plink = "https://www.spigotmc.org/resources/115478/"
            role_id = 1215399455835029504
        else:
            interaction.response.send_message(f"Failed to find the name of the plugin, please try again", ephemeral=True)
        return pname, plink, role_id