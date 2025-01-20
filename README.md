# Discord Bot Online

This repository contains a Python-based Discord bot designed to enhance your server's functionality.

## Features

- **Modular Design**: Functions are organized into cogs for better management and extensibility.
- **Easy to Use**: Simplified setup process for quick deployment.
- **Customizable**: Adjust settings and commands to fit your needs.

## Installation

Follow these steps to get started:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Iamsvito/discord-bot-online.git
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Bot Token**:
   Add your Discord bot token to an environment variable or configuration file as per the bot's instructions.

## Usage

To run the bot, execute the following command in your terminal:
```bash
python main.py
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request with your improvements or bug fixes.

## License

This project currently does not specify a license. Please contact the repository owner for usage terms.

---

For more information, visit the [GitHub Repository](https://github.com/Iamsvito/discord-bot-online).

## 指令使用說名:
+ == 空格<br>
def == 分類用<br>
格式:!指令(替代方案)+你輸入的值-->輸出值<br>
範例:(!add 2 2-->4) or (!加 2 2-->4)<br>
def Hehe():
	!網站(website)-->提供的網站以及番號位數<br>
	!N站(nhentai)+番號-->該網站網址<br>
	!紳士漫畫(wnacg.com)+番號-->該網站網址<br>
	!P站(pixiv)+番號-->該網站網址<br>
	!禁漫天堂(18comic)+番號-->該網站網址<br>
	!random(隨機)+位數-->幾位數的隨機番號<br>
def math():
	!roll_dice(擲骰)-->隨機數字(1~6)<br>
	!add(加)+數字1+數字2-->數字1+數字2<br>
	!subtract(減)+數字1+數字2-->數字1-數字2<br>
	!multiply(乘)+數字1+數字2-->數字1*數字2<br>
	!divide(除)+數字1+數字2-->數字1/數字2<br>
	!f_number(費氏數列)+num-->費波納契數列的第 num 項<br>
	!gcd(最大公因數)+數字1+數字2-->數字1 和 數字2 的最大公因數<br>
	!lcm(最小公倍數)+數字1+數字2-->數字1 和 數字2 的最小公倍數<br>
	!P(排列)+n+r-->P(n, r)<br>
	!C(組合)+n+r-->C(n, r)<br>
	!s1number(數列1)+n-->(1+2+...n)總和<br>
	!s2number(數列2)+n-->(1**2+2**2+...n)總和<br>
	!s3number(數列3)+n-->(1**3+2**3+...n**3)總和<br>
def high_school():
	!Change(找零)+購買金額+付的金額-->找500, 100, 10, 1元的紙鈔數量<br>
	!Leapyear(閏年判斷)+西元年-->是否為閏年<br>
	!bmi(身體質量指數)+weight(kg)+height(cm)-->BMI屬於範圍<br>
	!XX(一元二次方程解)+a+b+c-->ax**2 + bx + c = 0的解<br>
	!T(溫度轉換)+n+C(F)-->n°C(°F) 轉換為華氏溫度為n°F(°C)<br>
	!triangle(三角形)+a+b+c-->判斷給定的三個邊長是否能形成三角形，並確定三角形的類型<br>
	!dna(去氧核酸配對)+一段含氮鹼基序列--> DNA 中的配對序列<br>
	!rna(核酸配對)+一段含氮鹼基序列--> RNA 中的配對序列<br>
def 1a2b():
	!start1a2b+指定數字位數 (1-10)-->開始一個新的1A2B遊戲(可指定數字位數)<br>
	!guess1a2b+用戶的猜測的數字-->返回A和B的數量<br>
	!reset1a2b-->重置當前用戶的遊戲<br>
