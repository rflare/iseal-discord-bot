// MIT License

// Copyright (c) 2024 Lunarcat

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
} from "discord.js";
import { config } from "dotenv";

// Loading the environment variables
config();
const TOKEN = process.env.TOKEN;
const CLIENT_ID = process.env.CLIENT_ID;

const commands = [
  {
    name: "help",
    description: "Get help on how to use the bot",
  },
  {
    name: "resourcepack",
    description: "Get a link to download the resource pack",
  },
];

const rest = new REST({ version: "10" }).setToken(TOKEN);

try {
  console.log("Started refreshing application (/) commands.");

  await rest.put(Routes.applicationCommands(CLIENT_ID), { body: commands });

  console.log("Successfully reloaded application (/) commands.");
} catch (error) {
  console.error(error);
}

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
  ],
});

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === "help") {
    const embed = new EmbedBuilder()
      .setColor("#ffe600")
      .setTitle("**Commands**")
      .addFields(
        { name: "Command 1", value: "Description for command 1" },
        { name: "Command 2", value: "Description for command 2", inline: true },
        { name: "Command 3", value: "Description for command 3", inline: true }
      )
      .setTimestamp()
      .setFooter({
        text: "Made with ❤️ by lunarcatowo",
        iconURL:
          "https://cdn.discordapp.com/avatars/905758994155589642/c6784ea84cd89d2ec67688b97f04c922?size=1024&f=.png",
      });
    const member =
      interaction.member ||
      (await interaction.guild.members.fetch(interaction.user.id));

    const roleNamesToCheck = ["ISeal", "Community Manager"];
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );

    if (hasRole) {
      await interaction.reply({ embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
  if (interaction.commandName === "resourcepack") {
    const embed = new EmbedBuilder()
      .setColor("#0099ff")
      .setTitle("Resource Pack")
      .setDescription(
        "[Click me to download the default resource pack](https://cdn.discordapp.com/attachments/1157658269318402058/1193993804672421918/Powergems_Pack.zip?ex=662a00a2&is=6628af22&hm=ab75523cb14d11b57debef3faa3616e111e2f57d7a4674131d8d59740eeeba10&) /n [Click me to download the magic resource pack](https://cdn.discordapp.com/attachments/1157658269318402058/1194529976645582858/PowerGems_magic_pack.zip?ex=6629f9bb&is=6628a83b&hm=157d405d2f872ff9365371da79c110c793cb6e89178a84b3d508e4f65c9f7218&)"
      );
    const roleNamesToCheck = ["ISeal", "Community Manager"];
    const hasRole = member.roles.cache.some((role) =>
      roleNamesToCheck.includes(role.name)
    );
    if (hasRole) {
      await interaction.reply({ embeds: [embed] });
    } else {
      await interaction.reply({ embeds: [embed], ephemeral: true });
    }
  }
});

client.login(TOKEN);
