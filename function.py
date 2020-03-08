# coding: UTF-8
import const

async def new_game(client):
  channel = client.get_channel(const.channel_id['bot_control'])
  for member in channel.guild.members:
    if not member.bot:
      print(member)
      await role_change(member, "kankyaku")
  await channel.send('役職の初期化がおわりました。')
      

async def role_change(member, role_name):
  def role_class(i):
    return member.guild.get_role(const.role_id[i])
  ctrl_channel = member.guild.get_channel(const.channel_id['bot_control'])
  await member.remove_roles(role_class("kankyaku"))
  await member.remove_roles(role_class('player-a-1'))
  await member.remove_roles(role_class('player-a-2'))
  await member.remove_roles(role_class('player-b-1'))
  await member.remove_roles(role_class('player-b-2'))
  await member.add_roles(role_class(role_name))
  await ctrl_channel.send(member.mention + f':役職を{role_name}に変更しました！')