# coding: UTF-8
# token情報やチャンネルidなどの定数を別のファイルにおく
import const
# 関数関係
import prime
import function
# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = const.token

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
  channel = client.get_channel(const.channel_id['bot_control'])
  # 起動したらターミナルにログイン通知が表示される
  print('...ready')
  await channel.send('server-start!')
  await function.new_game(client)

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
  return
  def role_class(e):
    return message.guild.get_role(const.role_id[e])
  for member in message.guild.members:
    if not member.bot:
      print(member)
      await member.add_roles(role_class("kankyaku"))
      await member.remove_roles(role_class('player-a-1'))
      await member.remove_roles(role_class('player-a-2'))
      await member.remove_roles(role_class('player-b-1'))
      await member.remove_roles(role_class('player-b-2'))
  return
  # メッセージ送信者がBotだった場合は無視する
  if message.author.bot:
    return
  # 「/neko」と発言したら「にゃーん」が返る処理
  if message.content == '/neko':
    await message.channel.send('にゃーん')
  await message.channel.send(prime.primarity_test(message.content))

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)