import random
import discord
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
import time
import os

TOKEN = 'OTA3NjUzMDIyNTkzNzM2Nzk0.YYqTvw.1eFnPNuBMmLAigtxE7B7jRLDMDU'
bot = commands.Bot(command_prefix='!')


vip_mas_ember = ["QdAAcC","-XlocQ","F0KQ6F","BPz4ZM","VZLE3Y","Ml93_0","p9C2AR"]
vip_mas_obelisk = ["S6P_iz","Von9Uz","odO5Yn","OlSjZo","0gBH9q","X3b1RS","2jURsc"]
vip_mas_nimbus = ["AP-dY-","B4-Gvn","rKwyTw","JZYjZK","qDP3Ci","qDP3Ci","s5Zlpt"]
vip_mas_haze = ["eAU_zU","w3SG4i","isw9uB","IOmtF9","fqyaB3","wz5QbA"]
vip_mas_dunes = ["ZD_UuU","_Y90ry","ElStSF","HHSghl","UJYwOB","mgyAza","Otl7nA"]
vip_mas_newember = ["x6cWf3","AzCcy3","EKZvGa","32Z0zQ","1kjoS9","9JOtJP"]
vip_mas_training = ["ymDU96","WOym8X","NsrqJ3","fLRvqz","U8GVca","yDi-XV","jVCKZv"]
vip_mas_storm = ["dwolt0","VDbF-n","bXAXuy","32Z0zQ","1kjoS9","9JOtJP"]
vip_mas_forestofembers = ["x6cWf3","AzCcy3","EKZvGa","32Z0zQ","1kjoS9","9JOtJP"]
vip_mas_tempestvillage = ["x6cWf3","AzCcy3","EKZvGa","32Z0zQ","1kjoS9","9JOtJP"]
vip_mas_greatnarumakibridge = ["x6cWf3","AzCcy3","EKZvGa","32Z0zQ","1kjoS9","9JOtJP"]
vip_mas_shindaivalley = ["x6cWf3","AzCcy3","EKZvGa","32Z0zQ","1kjoS9","9JOtJP"]




def cooldown(rate, per_sec=0, per_min=0, per_hour=0, type=commands.BucketType.default):
    return commands.cooldown(rate, per_sec + 60 * per_min + 3600 * per_hour, type)



@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipember(ctx):  # создаем асинхронную фунцию бота
    var_mas_ember = random.choice(vip_mas_ember)
    index_for_del_ember = vip_mas_ember.index(var_mas_ember)
    vip_mas_ember.pop(index_for_del_ember)

    var_mas_ember2 = random.choice(vip_mas_ember)
    index_for_del_ember = vip_mas_ember.index(var_mas_ember2)
    vip_mas_ember.pop(index_for_del_ember)
    
    embed = discord.Embed(title="Ваша випка для деревни ember", description=f'{var_mas_ember}\n {var_mas_ember2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipobelisk(ctx):  # создаем асинхронную фунцию бота
    vaw_mas_ember = random.choice(vip_mas_obelisk)
    index_for_del_obelisk = vip_mas_obelisk.index(vaw_mas_ember)
    vip_mas_obelisk.pop(index_for_del_obelisk)

    vaw_mas_ember2 = random.choice(vip_mas_obelisk)
    index_for_del_obelisk = vip_mas_obelisk.index(vaw_mas_ember2)
    vip_mas_obelisk.pop(index_for_del_obelisk)
    
    embed = discord.Embed(title="Ваша випка для деревни obelisk", description=f'{vaw_mas_ember}\n {vaw_mas_ember2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipnimbus(ctx):  # создаем асинхронную фунцию бота
    vai_mas_ember = random.choice(vip_mas_nimbus)
    index_for_del_nimbus = vip_mas_nimbus.index(vai_mas_ember)
    vip_mas_nimbus.pop(index_for_del_nimbus)

    vai_mas_ember2 = random.choice(vip_mas_nimbus)
    index_for_del_nimbus = vip_mas_nimbus.index(vai_mas_ember2)
    vip_mas_nimbus.pop(index_for_del_nimbus)

    embed = discord.Embed(title="Ваша випка для деревни nimbus", description=f'{vai_mas_ember}\n {vai_mas_ember2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)


@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def viphaze(ctx):  # создаем асинхронную фунцию бота
    vak_mas_haze = random.choice(vip_mas_nimbus)
    index_for_del_haze = vip_mas_nimbus.index(vak_mas_haze)
    vip_mas_nimbus.pop(index_for_del_haze)

    vak_mas_haze2 = random.choice(vip_mas_nimbus)
    index_for_del_haze = vip_mas_nimbus.index(vak_mas_haze2)
    vip_mas_nimbus.pop(index_for_del_haze)

    embed = discord.Embed(title="Ваша випка для деревни haze", description=f'{vak_mas_haze}\n {vak_mas_haze2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipdunes(ctx):  # создаем асинхронную фунцию бота
    vak_mas_dunes = random.choice(vip_mas_nimbus)
    index_for_del_dunes = vip_mas_nimbus.index(vak_mas_dunes)
    vip_mas_nimbus.pop(index_for_del_dunes)

    vak_mas_dunes2 = random.choice(vip_mas_nimbus)
    index_for_del_dunes = vip_mas_nimbus.index(vak_mas_dunes2)
    vip_mas_nimbus.pop(index_for_del_dunes)

    embed = discord.Embed(title="Ваша випка для деревни dunes", description=f'{vak_mas_dunes}\n {vak_mas_dunes2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipnewember(ctx):  # создаем асинхронную фунцию бота
    vak_mas_newember = random.choice(vip_mas_newember)
    index_for_del_newember = vip_mas_newember.index(vak_mas_newember)
    vip_mas_newember.pop(index_for_del_newember)

    vak_mas_newember2 = random.choice(vip_mas_newember)
    index_for_del_newember = vip_mas_newember.index(vak_mas_newember2)
    vip_mas_newember.pop(index_for_del_newember)

    embed = discord.Embed(title="Ваша випка для деревни newembe", description=f'{vak_mas_newember}\n {vak_mas_newember2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def viptraining(ctx):  # создаем асинхронную фунцию бота
    vak_mas_training = random.choice(vip_mas_training)
    index_for_del_training = vip_mas_training.index(vak_mas_training)
    vip_mas_training.pop(index_for_del_training)

    vak_mas_training2 = random.choice(vip_mas_training)
    index_for_del_training = vip_mas_training.index(vak_mas_training2)
    vip_mas_training.pop(index_for_del_training)

    embed = discord.Embed(title="Ваша випка для деревни training", description=f'{vak_mas_training}\n {vak_mas_training2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipstorm(ctx):  # создаем асинхронную фунцию бота
    vak_mas_storm = random.choice(vip_mas_storm)
    index_for_del_storm = vip_mas_storm.index(vak_mas_storm)
    vip_mas_storm.pop(index_for_del_storm)
    
    vak_mas_storm2 = random.choice(vip_mas_storm)
    index_for_del_storm = vip_mas_storm.index(vak_mas_storm2)
    vip_mas_storm.pop(index_for_del_storm)

    embed = discord.Embed(title="Ваша випка для деревни storm", description=f'{vak_mas_storm}\n {vak_mas_storm2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipforestofembers(ctx):  # создаем асинхронную фунцию бота
    vak_mas_forestofembers = random.choice(vip_mas_forestofembers)
    index_for_del_forestofembers = vip_mas_forestofembers.index(vak_mas_forestofembers)
    vip_mas_forestofembers.pop(index_for_del_forestofembers)

    vak_mas_forestofembers2 = random.choice(vip_mas_forestofembers)
    index_for_del_forestofembers = vip_mas_forestofembers.index(vak_mas_forestofembers2)
    vip_mas_forestofembers.pop(index_for_del_forestofembers)

    embed = discord.Embed(title="Ваша випка для деревни forestofembers", description=f'{vak_mas_forestofembers}\n {vak_mas_forestofembers2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def viptempestvillage(ctx):  # создаем асинхронную фунцию бота
    vak_mas_tempestvillage = random.choice(vip_mas_tempestvillage)
    index_for_del_tempestvillage = vip_mas_tempestvillage.index(vak_mas_tempestvillage)
    vip_mas_tempestvillage.pop(index_for_del_tempestvillage)

    vak_mas_tempestvillage2 = random.choice(vip_mas_tempestvillage)
    index_for_del_tempestvillage = vip_mas_tempestvillage.index(vak_mas_tempestvillage2)
    vip_mas_tempestvillage.pop(index_for_del_tempestvillage)

    embed = discord.Embed(title="Ваша випка для деревни tempestvillage", description=f'{vak_mas_tempestvillage}\n {vak_mas_tempestvillage2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipgreatnarumakibridge(ctx):  # создаем асинхронную фунцию бота
    vak_mas_greatnarumakibridge = random.choice(vip_mas_greatnarumakibridge)
    index_for_del_greatnarumakibridge = vip_mas_greatnarumakibridge.index(vak_mas_greatnarumakibridge)
    vip_mas_greatnarumakibridge.pop(index_for_del_greatnarumakibridge)

    vak_mas_greatnarumakibridge2 = random.choice(vip_mas_greatnarumakibridge)
    index_for_del_greatnarumakibridge = vip_mas_greatnarumakibridge.index(vak_mas_greatnarumakibridge2)
    vip_mas_greatnarumakibridge.pop(index_for_del_greatnarumakibridge)

    embed = discord.Embed(title="Ваша випка для деревни tempestvillage", description=f'{vak_mas_greatnarumakibridge}\n {vak_mas_greatnarumakibridge2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)  # разрешаем передавать агрументы
@cooldown(1, per_hour=62, type=commands.BucketType.user)
@commands.has_role('Vip')
async def vipshindaivalley(ctx):  # создаем асинхронную фунцию бота
    vak_mas_shindaivalley = random.choice(vip_mas_shindaivalley)
    index_for_del_shindaivalley = vip_mas_shindaivalley.index(vak_mas_shindaivalley)
    vip_mas_shindaivalley.pop(index_for_del_shindaivalley)

    vak_mas_shindaivalley2 = random.choice(vip_mas_shindaivalley)
    index_for_del_shindaivalley = vip_mas_shindaivalley.index(vak_mas_shindaivalley2)
    vip_mas_shindaivalley.pop(index_for_del_shindaivalley)

    embed = discord.Embed(title="Ваша випка для деревни shindaivalley", description=f'{vak_mas_shindaivalley}\n {vak_mas_shindaivalley2}' ,color=discord.Colour.dark_red())
    await ctx.send(embed=embed)





@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def helps(ctx):  # создаем асинхронную фунцию бота
        embed = discord.Embed(title="Доступные Команды", description="!vipember\n !vipobelisk\n !vipnimbus\n !viphaze\n !vipdunes\n !vipnewember\n !viptraining\n !vipstorm\n !vipforestofembers\n !viptempestvillage\n !vipgreatnarumakibridge\n !vipshindaivalley\n", color=discord.Colour.dark_red())
        await ctx.send(embed=embed)



@vipember.error
async def error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        message = discord.Embed(title="Ошибка", description="Прежде чем использовать это, вы должны подождать <t:{}:R>".format(int(time.time() + error.retry_after)), color=discord.Colour.dark_red())
        await ctx.send(embed=message)



@bot.event
async def on_ready():
    print("bot is started")

bot.run(TOKEN)