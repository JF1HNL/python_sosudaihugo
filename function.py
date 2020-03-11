# coding: UTF-8
import const
import data

async def new_game(guild):
  data.a = data.game(data.player(0), data.player(0))
  data.b = data.game(data.player(0), data.player(0))
  channel = guild.get_channel(const.channel_id['bot_control'])
  for member in guild.members:
    if not member.bot:
      print(member)
      await role_change(member, "kankyaku")
  await channel.send('役職の初期化がおわりました。')

async def role_change(member, role_name):
  def role_class(i):
    return member.guild.get_role(const.role[i]['id'])
  role_ja = const.role[role_name]['ja']
  ctrl_channel = member.guild.get_channel(const.channel_id['bot_control'])
  role_name_list = role_name.split('-')
  if role_name_list[0] == 'player':
    data_dict = data.__dict__
    data_dict[role_name_list[1]].player[role_name_list[2]].id = member.id
  await member.remove_roles(role_class("kankyaku"))
  await member.remove_roles(role_class('player-a-1'))
  await member.remove_roles(role_class('player-a-2'))
  await member.remove_roles(role_class('player-b-1'))
  await member.remove_roles(role_class('player-b-2'))
  await member.add_roles(role_class(role_name))
  await ctrl_channel.send(f'{member.mention}:役職を{role_ja}に変更しました！')