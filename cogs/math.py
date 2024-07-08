from discord.ext import commands
import discord
import random

class Math(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='roll_dice', aliases=['擲骰'])
    async def roll_dice(self, ctx):
        """擲骰子遊戲指令"""
        roll_result = random.randint(1, 6)
        await ctx.send(f"你擲出了: {roll_result}")

    @commands.command(name='add', aliases=['加'])
    async def add(self, ctx, num1: int, num2: int):
        """加法指令"""
        result = num1 + num2
        await ctx.send(f"{num1} + {num2} = {result}")

    @commands.command(name='subtract', aliases=['減'])
    async def subtract(self, ctx, num1: int, num2: int):
        """減法指令"""
        result = num1 - num2
        await ctx.send(f"{num1} - {num2} = {result}")

    @commands.command(name='multiply', aliases=['乘'])
    async def multiply(self, ctx, num1: int, num2: int):
        """乘法指令"""
        result = num1 * num2
        await ctx.send(f"{num1} * {num2} = {result}")

    @commands.command(name='divide', aliases=['除'])
    async def divide(self, ctx, num1: float, num2: float):
        """除法指令"""
        if num2 == 0:
            await ctx.send("無法除以零！")
        else:
            result = num1 / num2
            await ctx.send(f"{num1} / {num2} = {result}")

    def fibonacci(self, n):
        """計算費波納契數列的第 n 個數字"""
        if n == 1 or n == 2 :
            return 1
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)

    @commands.command(name='f_number', aliases=['費氏數列'])
    async def f_number(self, ctx, num: int):
        """顯示費波納契數列的第 num 項"""
        if num <= 0:
            await ctx.send("請輸入正整數！")
        else:
            fib_sequence = self.fibonacci(num)
            await ctx.send(f"費波納契數列的第 {num} 項是: {fib_sequence}")

    def gcd(self, a, b):
        """計算最大公因數 GCD"""
        if a == 0 or b == 0:
            return 0
        else:    
            rem = a % b
            if rem == 0:
                return b
            else:
                return self.gcd(b, rem)

    @commands.command(name='gcd', aliases=['最大公因數'])
    async def gcd_command(self, ctx, num1: int, num2: int):
        """計算最大公因數 GCD"""
        result = self.gcd(num1, num2)
        await ctx.send(f"{num1} 和 {num2} 的最大公因數是: {result}")

    @commands.command(name='lcm', aliases=['最小公倍數'])
    async def lcm(self, ctx, num1: int, num2: int):
        """計算最小公倍數 LCM"""
        gcd_value = self.gcd(num1, num2)
        lcm_value = abs(num1 * num2) // gcd_value
        await ctx.send(f"{num1} 和 {num2} 的最小公倍數是: {lcm_value}")

    def factorial(self, n):
        """計算階乘"""
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    @commands.command(name='P' , aliases=['排列'])
    async def P(self, ctx, n: int, r: int):
        """計算排列數 P(n, r)"""
        if n < r or n < 0 or r < 0 :
            await ctx.send("n必須大於等於r且n,r>=0")
        else:
            result = self.factorial(n) // self.factorial(n - r)
            await ctx.send(f"P({n},取{r}) = {result}")

    @commands.command(name='C' , aliases=['組合'])
    async def C(self, ctx, n: int, r: int):
        """計算組合數 C(n, r)"""
        if n < r or n < 0 or r < 0:
            await ctx.send("n必須大於等於r且n,r>=0")
        else:
            result = self.factorial(n) // (self.factorial(r) * self.factorial(n - r))
            await ctx.send(f"C({n},取{r}) = {result}")
    def snum(self, n):
        """計算數列"""
        return n*(n+1)/2
    @commands.command(name='s1number' , aliases=['數列1'])
    async def s1number(self, ctx, num1: int):
        """計算數列1"""
        if num1 < 0:
            await ctx.send("n必須大於等於0")
        else:
            result = self.snum(num1)
            await ctx.send(f"{num1}s1數列(1+2+...n)總和= {result}")
    @commands.command(name='s2number' , aliases=['數列2'])
    async def s2number(self, ctx, num2: int):
        """計算數列2"""
        if num2 < 0:
            await ctx.send("n必須大於等於0")
        else:
            result = self.snum(num2)*(2*num2+1)/3
            await ctx.send(f"{num2}s1數列(1**2+2**2+...n**2)總和= {result}")
    @commands.command(name='s3number' , aliases=['數列3'])
    async def s3number(self, ctx, num3: int):
        """計算數列3"""
        if num3 < 0:
            await ctx.send("n必須大於等於0")
        else:
            result = self.snum(num3)**2
            await ctx.send(f"{num3}s1數列(1**3+2**3+...n**3)總和= {result}")

async def setup(bot):
    await bot.add_cog(Math(bot))