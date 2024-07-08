import discord
import random
from discord.ext import commands

class Hehe(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.system_channel  
        if channel is not None:
            await channel.send("偷偷告訴你:用!後可輸入指令")
    @commands.command(name='網站', aliases=['website'])
    async def 網站(self, ctx:commands.Context):
        await ctx.send("提供nhentai:XXXXXX(6),紳士漫畫:XXXXX(5),pixiv:XXXXXXXX(8),禁漫天堂:XXXXXX (6)")

    @commands.command(name='N站', aliases=['nhentai'])
    async def N站(self, ctx, a: int):
        await ctx.send(f"https://nhentai.net/g/{a}")

    @commands.command(name='紳士漫畫', aliases=['wnacg.com'])
    async def 紳士漫畫(self, ctx, a: int):    
        await ctx.send(f"https://www.wnacg.com/photos-index-aid-{a}")

    @commands.command(name='P站', aliases=['pixiv'])
    async def P站(self, ctx, a: int):
        await ctx.send(f"https://www.pixiv.net/en/artworks/{a}") 
    @commands.command(name='禁漫天堂', aliases=['18comic'])
    async def 禁漫天堂(self, ctx, a: int):
        await ctx.send(f"https://18comic.vip/album/{a}")
    @commands.command(name='random', aliases=['隨機'])   
    async def random(self, ctx, a: int):
        if a > 0:
            random_re = random.randint(1, 10**a - 1)
            formatted_number = "{:0{}d}".format(random_re, a)
            await ctx.send(formatted_number)
        else:
            await ctx.send("請輸入大於零的數字位數")     

async def setup(bot):
    await bot.add_cog(Hehe(bot))