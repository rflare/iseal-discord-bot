// MIT License

// Copyright (c) 2024 LunarcatOwO

// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

import {
  Client,
  GatewayIntentBits,
  REST,
  Routes,
  EmbedBuilder,
  ModalBuilder,
  TextInputBuilder,
  ActionRowBuilder,
} from "discord.js";
import { config } from "dotenv";
// Loading the environment variables
config();
const TOKEN = process.env.TOKEN;
const CLIENT_ID = process.env.CLIENT_ID;
const TRIGGER_ROLES = process.env.TRIGGER_ROLES;
const commands = [
  {
    name: "help",
    description: "Get help on how to use the bot",
  },
  {
    name: "resourcepack",
    description: "Get a link to download the resource pack",
  },
  {
    name: "rp",
    description: "Get a link to download the resource pack",
  },
  {
    name: "rules",
    description: "Get the server's rules",
  },
  {
    name: "config",
    description: "Get how to access the config file",
  },
  {
    name: "wiki",
    description: "Get the wiki link",
    options: [
      {
        name: "powergems",
        description: "Get the wiki link for powergems",
        type: 1,
      },
      {
        name: "orepowers",
        description:
          "Get the wiki link for orepowers (wiki coming if the plugin reaches 2k downloads)",
        type: 1,
      },
      {
        name: "valocraft",
        description:
          "Get the wiki link for valocraft (wiki coming if the plugin reaches 2k downloads)",
        type: 1,
      },
      {
        name: "parkourproject",
        description:
          "Get the wiki link for parkourproject (wiki coming if the plugin reaches 2k downloads)",
        type: 1,
      },
    ],
  },
  {
    name: "download",
    description: "Get the latest download link",
  },
  {
    name: "update",
    description: "Sends out a message for plugin updates (ADMIN ONLY)",
  },
  {
    name: "format",
    description: "Get how to format your bug reports or suggestions",
    options: [
      {
        name: "bug",
        description: "Get how to format your bug reports",
        type: 1,
      },
      {
        name: "suggestion",
        description: "Get how to format your suggestions",
        type: 1,
      },
    ],
  },
  {
    name: "botgithub",
    description:
      "Get the github link to the bot's code to report issues and give suggestions!",
  },
];

const rest = new REST({ version: "10" }).setToken(TOKEN);

try {
  console.log("Started refreshing application (/) commands.");

  // Wrap the code in an async function
  (async () => {
    await rest.put(Routes.applicationCommands(CLIENT_ID), { body: commands });
  })();

  console.log("Successfully reloaded application (/) commands.");
} catch (error) {
  console.error(error);
}

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.DirectMessages,
    GatewayIntentBits.GuildMembers,
  ],
  allowedMentions: { parse: ["users", "roles", "everyone"] },
});

async function getLatestReleaseAsset(owner, repo) {
  try {
    const response = await fetch(
      `https://api.github.com/repos/${owner}/${repo}/releases/latest`
    );
    const release = await response.json();
    const asset = release.assets[0]; // Assuming you want the first asset
    const downloadUrl = asset.browser_download_url;
    console.log(downloadUrl);
    return downloadUrl;
  } catch (error) {
    console.error("Error fetching release data:", error);
    console.log("Giving user Default spigot download link...");
    let downloadUrl;
    if (repo === "Powergems") {
      downloadUrl =
        "https://spigotmc.org/resources/1-19-4-1-20-x-powergems.108943/";
    } else if (repo == "OrePowers") {
      downloadUrl = "https://www.spigotmc.org/resources/orepowers.113941/";
    } else if (repo == "Valocraft") {
      downloadUrl =
        "https://www.spigotmc.org/resources/1-19-4-1-20-x-valocraft.115131/";
    } else if (repo == "ParkourProject") {
      downloadUrl =
        "https://www.spigotmc.org/resources/1-20-x-1-19-4-parkourproject.115478/";
    }
    console.log(downloadUrl);
    return downloadUrl;
  }
}

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === "help") {
    help(interaction)
  }
  if (interaction.commandName === "resourcepack") {
    resourcepack(interaction)
  }
  if (interaction.commandName === "rp") {
    rp(interaction) 
  }
  if (interaction.commandName === "rules") {
    const embed = new EmbedBuilder()
      .setColor("#00ff00")
      .setTitle("Rules for the server")
      .setDescription("Read the following carefully!")
      .addFields(
        {
          name: "1️⃣ Spam!",
          value: "Please dont spam. Nobody likes it and you will get muted.",
        },
        {
          name: "2️⃣ Help us to help you!",
          value:
            'If you are reporting a bug/issue, please give plenty of information. Simply just saying "Help" isn\'t very useful.',
        },
        {
          name: "3️⃣ We have tickets!",
          value:
            "To get individual support, you can open a ticket in the <#1157666504461000714> channel.",
        },
        {
          name: "4️⃣ Patience",
          value:
            "When asking for help, please be patient. We will get to you as soon as possible, but we all have a life too. (I know, shocking)",
        },
        {
          name: "5️⃣ Tone.",
          value:
            "Keep a friendly tone and try not to swear, a little is allowed, but dont exagerate",
        }
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      await interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({ embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
  if (interaction.commandName === "config") {
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("How to access the config file")
      .setDescription(
        "Follow the following steps if you do not know how to access the config file"
      )
      .addFields(
        {
          name: "Step 1",
          value: "Go to your server's file manager",
          inline: true,
        },
        { name: "Step 2", value: "Open the `~/plugins` folder", inline: true },
        {
          name: "Step 3",
          value:
            "Open the folder with the plugin's name. example of the route: `~/plugins/PowerGems`",
          inline: true,
        },
        {
          name: "Step 4",
          value: "Open the `config.yml` file",
          inline: true,
        }
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      await interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({ embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
  if (interaction.commandName === "wiki") {
    const subcommand = interaction.options.getSubcommand();
    if (subcommand === "powergems") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("Link to PowerGems wiki")
        .setTimestamp()
        .setDescription(
          "[Click me](https://powergems.iseal.dev) for Powergems wiki"
        )
        .setFooter({
          text: "Made with ❤️ by LunarcatOwO",
          iconURL:
            "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
    if (subcommand === "orepowers") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("Link to OrePowers wiki")
        .setDescription("Coming soon (if the plugin hits 2k downloads)")
        .setTimestamp()
        .setFooter({
          text: "Made with ❤️ by LunarcatOwO",
          iconURL:
            "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
    if (subcommand === "valocraft") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("Link to Valocraft wiki")
        .setDescription("Coming soon (if the plugin hits 2k downloads)")
        .setTimestamp()
        .setFooter({
          text: "Made with ❤️ by LunarcatOwO",
          iconURL:
            "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
    if (subcommand === "parkourproject") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("Link to ParkourProject wiki")
        .setDescription("Coming soon (if the plugin hits 2k downloads)")
        .setTimestamp()
        .setFooter({
          text: "Made with ❤️ by LunarcatOwO",
          iconURL:
            "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
  }
  if (interaction.commandName === "download") {
    const PGdownloadLink = await getLatestReleaseAsset(
      "ISeal-plugin-developement",
      "PowerGems"
    );
    const OPdownloadLink = await getLatestReleaseAsset(
      "ISeal-plugin-developement",
      "OrePowers"
    );
    const VCdownloadLink = await getLatestReleaseAsset(
      "ISeal-plugin-developement",
      "Valocraft"
    );
    const PPdownloadLink = await getLatestReleaseAsset(
      "ISeal-plugin-developement",
      "ParkourProject"
    );
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("Download Link for the plugins!")
      .setDescription(
        `[Click me to download PowerGems](${PGdownloadLink})
[Click me to download OrePowers](${OPdownloadLink})
[Click me to download Valocraft](${VCdownloadLink})
[Click me to download ParkourProject](${PPdownloadLink})`
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      await interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({ embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
  if (interaction.commandName === "update") {
    const modal = new ModalBuilder()
      .setCustomId("updateModal")
      .setTitle("Update");
    const pluginIDinput = new TextInputBuilder()
      .setCustomId("pluginIDinput")
      .setLabel("What is the ID for the plugin")
      .setStyle(1)
      .setMaxLength(2)
      .setRequired(true);

    const updateInfoInput = new TextInputBuilder()
      .setCustomId("updateInfoInput")
      .setLabel("What changed?")
      .setStyle(2)
      .setRequired(true);
    const versionInfoInput = new TextInputBuilder()
      .setCustomId("versionInfoInput")
      .setLabel("Version of update")
      .setStyle(1)
      .setRequired(true);
    const secondActionRow = new ActionRowBuilder().addComponents(
      versionInfoInput
    );
    const firstActionRow = new ActionRowBuilder().addComponents(pluginIDinput);
    const thirdActionRow = new ActionRowBuilder().addComponents(
      updateInfoInput
    );

    modal.addComponents(firstActionRow, secondActionRow, thirdActionRow);
    if (!interaction.guild) {
      await interaction.reply({ content: "What are you thinking..." });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.showModal(modal);
    } else {
      await interaction.reply({
        content: "What are you trying to do...",
        ephemeral: true,
      });
    }
  }
  if (interaction.commandName === "format") {
    const subcommand = interaction.options.getSubcommand();
    if (subcommand === "bug") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("How to format your bug report")
        .setDescription(
          "Please follow the following format to format your bug report"
        )
        .addFields(
          {
            name: "General information",
            value: `Server software:
Server version:
Software build: (if applicable)
Plugins on the server`,
          },
          {
            name: "Plugin information",
            value: `Plugin:
Plugin version:
Errors in console: (if applicable, preferably using https://mclo.gs/)`,
          },
          {
            name: "Bug information:",
            value: `Expected result:
Actual result:
Things tried:`,
          }
        )
        .setTimestamp()
        .setFooter({
          text: "Made with ❤️ by LunarcatOwO",
          iconURL:
            "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
    if (subcommand === "suggestion") {
      const embed = new EmbedBuilder()
        .setColor("#0099ff")
        .setTitle("How to format your suggestion")
        .setDescription(
          "Please follow the following format to format your suggestion"
        )
        .addFields({
          name: "Information needed",
          value: `Plugin Name:
What to add:
How it is currently (If applicable):
Why it should be added:
Extra Notes (If applicable):`,
          inline: true,
        });
      if (!interaction.guild) {
        await interaction.reply({ embeds: [embed] });
        return;
      }
      const member =
        interaction.member ||
        (await interaction.guild.members.fetch(interaction.user.id));
      const roleNamesToCheck = TRIGGER_ROLES;
      const hasRole = member.roles.cache.some((role) =>
        roleNamesToCheck.includes(role.name)
      );
      if (hasRole) {
        await interaction.reply({ embeds: [embed] });
      } else {
        await interaction.reply({ embeds: [embed], ephemeral: true });
      }
    }
  }
  if (interaction.commandName === "botgithub") {
    if (!interaction.guild) {
      await interaction.reply({
        content: `Thank you for being intrested in the bot! 
[Github](https://github.com/LunarcatOwO/iseal-discord-bot)
[Support me!](https://ko-fi.com/lunarcatOwO)`,
        ephemeral: true,
      });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({
        content: `Thank you for being intrested in the bot! 
[Github](https://github.com/LunarcatOwO/iseal-discord-bot)
[Support me!](https://ko-fi.com/lunarcatOwO)`,
        ephemeral: true,
      });
    } else {
      await interaction.reply({
        content: `Thank you for being intrested in the bot! 
[Github](https://github.com/LunarcatOwO/iseal-discord-bot)
[Support me!](https://ko-fi.com/lunarcatOwO)`,
        ephemeral: true,
      });
    }
  }
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isModalSubmit()) return;

  if (interaction.customId === "updateModal") {
    if (!interaction.guild) {
      await interaction.reply({
        content: "How did you even trigger this message... ",
      });
      return;
    }
    const pluginID = interaction.fields.getTextInputValue("pluginIDinput");
    const version = interaction.fields.getTextInputValue("versionInfoInput");
    const updateInfo = interaction.fields.getTextInputValue("updateInfoInput");
    let pluginName;
    let roleid;
    if (pluginID === "pg") {
      pluginName = "PowerGems";
      roleid = "1158015875744551003";
    } else if (pluginID === "op") {
      pluginName = "OrePowers";
      roleid = "1185692151716270121";
    } else if (pluginID === "vc") {
      pluginName = "Valocraft";
      roleid = "1201124609060245555";
    } else if (pluginID === "pp") {
      pluginName = "ParkourProject";
      roleid = "1215399455835029504";
    }
    const embed = new EmbedBuilder()
      .setColor("#FFFF00")
      .setTitle(`${pluginName} has updated to version ${version}`)
      .setDescription(
        `**What changed:**
    ${updateInfo}`
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      await interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({ content: `<@&${roleid}>`, embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
});

client.on("threadCreate", async (thread) => {
  await thread.join();
  const embed = new EmbedBuilder()
    .setColor("#FFFF00")
    .setTitle("Hello!")
    .setDescription(
      "**I am a bot, I may not be able to assist you, but please be patient as someone will respond as soon as they can!**"
    )
    .setTimestamp()
    .setFooter({
      text: "Made with ❤️ by LunarcatOwO",
      iconURL:
        "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
    });
  await thread.send({ embeds: [embed] });
  await thread.send({ content: "<@905758994155589642> <@398908171357519872>" });
  await thread.lastMessage.delete();
});

client.on("messageCreate", async (message) => {
  if (message.mentions.has(client.user)) {
    await message.reply(
      "**I am a bot, cannot assist you! If you want to report a bug put it in https://discord.com/channels/1157645386480091156/1157659553345831012 if you have a suggestion put it in https://discord.com/channels/1157645386480091156/1157664317932584970 **"
    );
  }
  if (message.channel.type === "DM" && message.author.id !== client.user.id) {
    await message.reply(
      "**I am a bot, cannot assist you! If you want to report a bug put it in https://discord.com/channels/1157645386480091156/1157659553345831012 if you have a suggestion put it in https://discord.com/channels/1157645386480091156/1157664317932584970 **"
    );
  }
});

client.on("guildMemberAdd", async (member) => {
  try {
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("Welcome to the server!")
      .setDescription(
        "Welcome to the server! if you are looking for the resource pack then run /resourcepack or /resources and it will automatically help you with that. Again welcome to the server and if you have any questions then just ask!"
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    await member.user.send({ embed: [embed] });
  } catch (error) {
    console.error(`Could not send welcome DM to ${member.displayName}.`, error);
  }
});

client.login(TOKEN);

function help(interaction) {
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("**Commands**")
      .addFields(
        { name: "/help", value: "Shows this page", inline: true },
        {
          name: "/resourcepack",
          value: "Sends the resourcepack download links",
          inline: true,
        },
        { name: "/rules", value: "Get the server's rules", inline: true },
        {
          name: "/config",
          value: "Get how to access the config files for your plugins",
          inline: true,
        },
        {
          name: "/wiki <name>",
          value: "Get the wiki link for the plugin you want to know about",
          inline: true,
        },
        {
          name: "/download",
          value: "Get the latest download link for the plugins",
          inline: true,
        },
        {
          name: "/format <type>",
          value:
            "Get how to format your bug report or suggestions (for the plugins)",
          inline: true,
        },
        {
          name: "/botgithub",
          value:
            "Get the github link to the bot's code to report issues and give suggestions!",
        }
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (interaction.guild.members.fetch(interaction.user.id));

    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );

    if (hasRole) {
      interaction.reply({ embeds: [embed] });
    } else {
      interaction.reply({ embeds: [embed], ephemeral: true });
    }
}

function resourcepack(interaction)
{
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("Resource Pack")
      .setDescription(
        "[Click me to download the default resourcepack for PowerGems](https://cdn.discordapp.com/attachments/1157658269318402058/1193993804672421918/Powergems_Pack.zip?ex=662a00a2&is=6628af22&hm=ab75523cb14d11b57debef3faa3616e111e2f57d7a4674131d8d59740eeeba10&) /n [Click me to download the magic resource pack for PowerGems](https://cdn.discordapp.com/attachments/1157658269318402058/1194529976645582858/PowerGems_magic_pack.zip?ex=6629f9bb&is=6628a83b&hm=157d405d2f872ff9365371da79c110c793cb6e89178a84b3d508e4f65c9f7218&)"
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    const roleNamesToCheck = TRIGGER_ROLES;
    const member =
      interaction.member ||
      (interaction.guild.members.fetch(interaction.user.id));
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      interaction.reply({ embeds: [embed] });
    } else {
      interaction.reply({ embeds: [embed], ephemeral: true });
    }
}

function rp(interaction)
{
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("Resource Pack")
      .setDescription(
        `[Click me to download the default resourcepack for PowerGems](https://cdn.discordapp.com/attachments/1157658269318402058/1193993804672421918/Powergems_Pack.zip?ex=662a00a2&is=6628af22&hm=ab75523cb14d11b57debef3faa3616e111e2f57d7a4674131d8d59740eeeba10&) 
[Click me to download the magic resource pack for PowerGems](https://cdn.discordapp.com/attachments/1157658269318402058/1194529976645582858/PowerGems_magic_pack.zip?ex=6629f9bb&is=6628a83b&hm=157d405d2f872ff9365371da79c110c793cb6e89178a84b3d508e4f65c9f7218&)`
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by LunarcatOwO",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/96f2fabc5e89d3e89a71aeda12f81a47?size=1024&f=.png",
      });
    if (!interaction.guild) {
      interaction.reply({ embeds: [embed] });
      return;
    }
    const member =
      interaction.member ||
      (interaction.guild.members.fetch(interaction.user.id));
    const roleNamesToCheck = TRIGGER_ROLES;
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      interaction.reply({ embeds: [embed] });
    } else {
      interaction.reply({ embeds: [embed], ephemeral: true });
    }
}
