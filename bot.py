import hikari
import lightbulb
import random
import os

bot = lightbulb.BotApp(token=os.environ["DISCORD_TOKEN"],
                       default_enabled_guilds=(972244644043837461, 892063974944821309, 896115278872715265))


@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started')


@bot.command
@lightbulb.command('boris', 'See an excellent gif/image of boris')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def boris(ctx):
    pass


@boris.child
@lightbulb.command('borisgif', 'See a gif of Boris looking his best')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def borisimage(ctx):
    bimage = open('boris').read().splitlines()
    myboris = random.choice(bimage)
    await ctx.respond(myboris)


@bot.command
@lightbulb.option('user', 'who you want to say happy Birthday to', type=str)
@lightbulb.command('happybirthday', 'happybirthday!')
@lightbulb.implements(lightbulb.SlashCommand)
async def birthday(ctx):
    await ctx.respond(ctx.options.user + ' Happy Birthday!')


@bot.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option('updateping', 'who you wish to ping for this update', type=str)
@lightbulb.option('update1', 'what is in the update', type=str)
@lightbulb.command('update', 'update')
@lightbulb.implements(lightbulb.SlashCommand)
async def update(ctx):
    await ctx.respond(ctx.options.update1)


@bot.command
@lightbulb.option('user', 'The user you wish to insult', type=str)
@lightbulb.command('insult', 'Insults someone')
@lightbulb.implements(lightbulb.SlashCommand)
async def insult(ctx):
    lines = open('a').read().splitlines()
    myline = random.choice(lines)
    await ctx.respond(ctx.options.user + myline)


@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')


@bot.command
@lightbulb.command('group', 'this is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def my_group(ctx):
    pass


@my_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')


bot.run()
