from discord.ext import commands
import discord

class High_school(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Change' , aliases=['找零'])
    async def Change(self, ctx, purchase_amount: int, payment_amount: int):
        """找零錢計算"""
        change = payment_amount - purchase_amount
        if change <= 0:
            await ctx.send("付款金額不足或正好，無需找零。")
            return

        coins = [500, 100, 10, 1]
        change_count = {}
        #chatgpt 找零錢
        for coin in coins:
            if change >= coin:
                count = change // coin
                change_count[coin] = count
                change -= count * coin

        result = f"應找:{payment_amount - purchase_amount}元\n"
        for coin, count in change_count.items():
            result += f"{coin}元x {count}\n"

        await ctx.send(result.strip())

    @commands.command(name='Leapyear' , aliases=['閏年判斷'])
    async def Leapyear(self, ctx, year: int):
        """閏年判斷"""
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            await ctx.send(f"{year}年是閏年。")
        else:
            await ctx.send(f"{year}年不是閏年。")

    @commands.command(name='bmi' , aliases=['身體質量指數'])
    async def bmi(self, ctx, weight: float, height: float):
        """身體質量指數（BMI）計算"""
        height_meters = height / 100
        bmi_value = weight / (height_meters ** 2)
        bmi_category = ""

        if bmi_value < 18.5:
            bmi_category = "體重過輕"
        elif bmi_value < 24:
            bmi_category = "理想"
        elif bmi_value < 27:
            bmi_category = "過重"
        elif bmi_value < 30:
            bmi_category = "輕度肥胖"
        elif bmi_value < 35:
            bmi_category = "中度肥胖"
        else:
            bmi_category = "重度肥胖"

        await ctx.send(f"BMI: {bmi_value:.2f}\n屬於範圍: {bmi_category}")

    @commands.command(name='XX' , aliases=['一元二次方程解'])
    async def XX(self, ctx, a: float, b: float, c: float):
        """一元二次方程解"""
        if a == 0:
            await ctx.send("這不是一元二次方程。")
            return

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            await ctx.send(f"二解: x1 = {x1}, x2 = {x2}")
        elif discriminant == 0:
            x = -b / (2*a)
            await ctx.send(f"重根: x = {x}")
        else:
            await ctx.send("無實解。")

    @commands.command(name='T' , aliases=['溫度轉換'])
    async def T(self, ctx, temperature: float, scale: str):
        """溫度轉換"""
        if scale.upper() == 'C':
            converted_temp = temperature * 9/5 + 32
            await ctx.send(f"{temperature}°C 轉換為華氏溫度為 {converted_temp}°F")
        elif scale.upper() == 'F':
            converted_temp = (temperature - 32) * 5/9
            await ctx.send(f"{temperature}°F 轉換為攝氏溫度為 {converted_temp}°C")
        else:
            await ctx.send("請提供正確的溫度轉換代號：C 或 F。")
    @commands.command(name='triangle', aliases=['三角形'])
    async def triangle(self, ctx, l1: float, l2: float, l3: float):
        """判斷給定的三個邊長是否能形成三角形，並確定三角形的類型"""
        if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
            if l1 == l2 == l3:
                triangle_type = "正三角形"
            elif l1 == l2 or l2 == l3 or l1 == l3:
                triangle_type = "等腰三角形"
            else:
                triangle_type = "普通三角形"

            # 使用餘弦定理計算角度類型
            a2, b2, c2 = l1**2, l2**2, l3**2
            angles = [a2 + b2 - c2, a2 + c2 - b2, b2 + c2 - a2]
            angle_types = []
            for angle in angles:
                if angle == 0:
                    angle_types.append("直角")
                elif angle > 0:
                    angle_types.append("銳角")
                else:
                    angle_types.append("鈍角")

            if "鈍角" in angle_types:
                angle_type = "鈍角三角形"
            elif "直角" in angle_types:
                angle_type = "直角三角形"
            else:
                angle_type = "銳角三角形"

            await ctx.send(f"邊長 {l1}, {l2}, {l3} 可以形成一個 {triangle_type} 並且是一個 {angle_type}")
        else:
            await ctx.send(f"邊長 {l1}, {l2}, {l3} 不能形成三角形")
    @commands.command(name='dna', aliases=['去氧核酸配對'])
    async def dna(self, ctx, sequence: str):
        """輸入一段含氮鹼基序列，輸出 DNA 中的配對序列"""
        base_pairs_dna = {
            "A": "T",
            "T": "A",
            "C": "G",
            "G": "C"
        }

        try:
            sequence = sequence.upper()# 確保整個序列都是大寫
            paired_sequence = ''.join(base_pairs_dna[base] for base in sequence)
            await ctx.send(f"輸入的 DNA 含氮鹼基序列: {sequence}\n配對序列: {paired_sequence}")
        except KeyError:
            await ctx.send("無效的 DNA 含氮鹼基序列")

    @commands.command(name='rna', aliases=['核酸配對'])
    async def rna(self, ctx, sequence: str):
        """輸入一段含氮鹼基序列，輸出 RNA 中的配對序列"""
        base_pairs_rna = {
            "A": "U",
            "T": "A",
            "C": "G",
            "G": "C"
        }

        try:
            sequence = sequence.upper()# 確保整個序列都是大寫
            paired_sequence = ''.join(base_pairs_rna[base] for base in sequence)
            await ctx.send(f"輸入的 RNA 含氮鹼基序列: {sequence}\n配對序列: {paired_sequence}")
        except KeyError:
            await ctx.send("無效的 RNA 含氮鹼基序列")
    def rna_to_protein(self, rna_sequence):
        codon_table = {
            'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
            'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
            'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
            'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
            'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
            'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
            'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
            'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
            'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'Stop', 'UAG': 'Stop',
            'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
            'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
            'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
            'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'Stop', 'UGG': 'Trp',
            'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
            'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
            'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
        }
        protein_sequence = []
        start_found = False
        for i in range(0, len(rna_sequence), 3):
            codon = rna_sequence[i:i+3]
            if codon == 'AUG':
                start_found = True
            if start_found:
                if codon in codon_table:
                    amino_acid = codon_table[codon]
                    if amino_acid == 'Stop':
                        break
                    protein_sequence.append(amino_acid)
        return '-'.join(protein_sequence)

    @commands.command(name='translate_to_protein', aliases=['轉蛋白質']) 
    async def translate_to_protein(self, ctx, sequence: str):
        """輸入一段含氮鹼基序列，輸出對應的蛋白質序列"""
        protein = self.rna_to_protein(sequence.upper()) # 確保整個序列都是大寫
        await ctx.send(protein)

    def arithmetic_series(self, a, d, n):
        return [a + i * d for i in range(n)]

    def geometric_series(self, a, r, n):
        return [a * (r ** i) for i in range(n)]

    @commands.command(name='arithmetic', aliases=['等差級數'])
    async def arithmetic(self, ctx, a: int, d: int, n: int):
        series = self.arithmetic_series(a, d, n)
        await ctx.send(f"等差級數: {series}")

    @commands.command(name='geometric', aliases=['等比級數'])
    async def geometric(self, ctx, a: int, r: int, n: int):
        series = self.geometric_series(a, r, n)
        await ctx.send(f"等比級數: {series}")

    def calculate_remaining_assets(self, marital_assets, marital_debts, inherited_assets, gifted_assets, alimony):
        remaining_assets = marital_assets - marital_debts - inherited_assets - gifted_assets - alimony
        return max(remaining_assets, 0)

    def calculate_distribution(self, assets1, assets2):
        if assets1 > assets2:
            return (assets1 - assets2) / 2
        else:
            return (assets2 - assets1) / 2

    @commands.command(name='離婚')
    async def calculate_assets(self, ctx, marital_assets1: float, marital_debts1: float, inherited_assets1: float, gifted_assets1: float, alimony1: float, marital_assets2: float, marital_debts2: float, inherited_assets2: float, gifted_assets2: float, alimony2: float):
        remaining_assets1 = self.calculate_remaining_assets(marital_assets1, marital_debts1, inherited_assets1, gifted_assets1, alimony1)
        remaining_assets2 = self.calculate_remaining_assets(marital_assets2, marital_debts2, inherited_assets2, gifted_assets2, alimony2)
        distribution_amount = self.calculate_distribution(remaining_assets1, remaining_assets2)

        if remaining_assets1 > remaining_assets2:
            await ctx.send(f"配偶1的剩餘財產為 {remaining_assets1}。配偶2的剩餘財產為 {remaining_assets2}。配偶2應向配偶1請求分配 {distribution_amount} 的剩餘財產。")
        else:
            await ctx.send(f"配偶1的剩餘財產為 {remaining_assets1}。配偶2的剩餘財產為 {remaining_assets2}。配偶1應向配偶2請求分配 {distribution_amount} 的剩餘財產。")

    @commands.command(name='遺產')
    async def send_image(self, ctx):
        # 直接发送图片链接
        image_url = 'https://www.canva.com/design/DAGKCxnKU6I/3zG5k_aiLgQcj2zKn3UXBQ/edit?utm_content=DAGKCxnKU6I&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'
        await ctx.send(image_url)
async def setup(bot):
    await bot.add_cog(High_school(bot))