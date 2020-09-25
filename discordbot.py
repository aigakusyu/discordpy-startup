# インストールした discord.py を読み込む
import discord
import pandas as pd
import random
import codecs
siritori =""

url = 'https://raw.githubusercontent.com/aigakusyu/discordpy-startup/master/s_hyou.csv'
df = pd.read_csv(url, error_bad_lines=False)

with codecs.open('df', "r", "UTF-8", "ignore") as file:
    siritori = pd.read_table(file, delimiter=",")

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NzU1MjcyNTM4ODk1OTQxNjcy.X2A4XQ.aluPawj1JeQoFhU96-rEct8KhMg'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    def check(msg):
        return msg.author == message.author

    if message.content.startswith("/s start"):

        await message.channel.send("しりとりスタート！　しりとり")

        while True:

            wait_message = await client.wait_for("message", check=check)

            i = random.randint(0,100)

            await message.channel.send(siritori[wait_message.content[-1]][i])

            if wait_message.content[-1] == "ん":
                print("最後が「ん」だよ！！！！！！")
                break

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
