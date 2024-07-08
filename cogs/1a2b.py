import discord
from discord.ext import commands
import random

class OneA2BGame:
    def __init__(self, num_digits):
        # 初始化遊戲，設置所需的數字位數和生成秘密數字
        self.num_digits = num_digits
        self.secret = self.generate_secret()
        self.attempts = 0

    def generate_secret(self):
        # 生成一個隨機的秘密數字序列
        digits = list(range(10))
        random.shuffle(digits)
        return digits[:self.num_digits]

    def guess(self, user_guess):
        # 猜測處理，返回A和B的數量
        self.attempts += 1
        a = sum(1 for i in range(self.num_digits) if user_guess[i] == self.secret[i])
        b = sum(1 for i in range(self.num_digits) for j in range(self.num_digits) if i != j and user_guess[i] == self.secret[j])
        return a, b

    def reset(self):
        # 重置遊戲，生成新的秘密數字並重置嘗試次數
        self.secret = self.generate_secret()
        self.attempts = 0

class OneA2B(commands.Cog):
    def __init__(self, bot):
        # 初始化Cog並設置bot和遊戲字典
        self.bot = bot
        self.games = {}

    @commands.command(name='start1a2b')
    async def start_game(self, ctx, num_digits: int = 4):
        # 開始一個新的1A2B遊戲，指定數字位數
        if num_digits < 1 or num_digits > 10:
            await ctx.send(f"{ctx.author.mention} Please enter a valid number of digits (1-10).")
            return
        self.games[ctx.author.id] = OneA2BGame(num_digits)
        await ctx.send(f"{ctx.author.mention} The game 1A2B with {num_digits} digits has started! Guess a {num_digits}-digit number.")

    @commands.command(name='guess1a2b')
    async def make_guess(self, ctx, guess: str):
        # 處理用戶的猜測並返回A和B的數量
        if ctx.author.id not in self.games:
            await ctx.send(f"{ctx.author.mention} You need to start a game first with !start1a2b <num_digits>.")
            return

        game = self.games[ctx.author.id]
        if len(guess) != game.num_digits or not guess.isdigit():
            await ctx.send(f"{ctx.author.mention} Please enter a valid {game.num_digits}-digit number.")
            return

        user_guess = [int(digit) for digit in guess]
        a, b = game.guess(user_guess)

        if a == game.num_digits:
            await ctx.send(f"{ctx.author.mention} Congratulations! You've guessed the correct number {guess} in {game.attempts} attempts.")
            del self.games[ctx.author.id]
        else:
            await ctx.send(f"{ctx.author.mention} {a}A{b}B. Try again!")

    @commands.command(name='reset1a2b')
    async def reset_game(self, ctx):
        # 重置當前用戶的遊戲
        if ctx.author.id in self.games:
            self.games[ctx.author.id].reset()
            await ctx.send(f"{ctx.author.mention} The game has been reset. Guess a new {self.games[ctx.author.id].num_digits}-digit number.")
        else:
            await ctx.send(f"{ctx.author.mention} You have not started a game yet.")

async def setup(bot):
    # 註冊這個Cog到bot中
    await bot.add_cog(OneA2B(bot))