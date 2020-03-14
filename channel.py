import function
import data

async def bot_control(msg):
  ary = msg.content.split()
  if ary[0] == 'role_set':
    ary.remove('role_set')
    if len(ary) < 2:
      await msg.channel.send(f'{msg.author.mention} memberが足りません。')
      return
    user_id = ary[0].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-a-1')
    user_id = ary[1].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-a-2')
    if not len(ary) == 4:
      return
    user_id = ary[2].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-b-1')
    user_id = ary[3].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-b-2')
  if ary[0] == 'new_game':
    await function.new_game(msg.guild)
  if ary[0] == 'game_start':
    for i in range(11):
      data.a.draw('1')
      data.a.draw('2')
      data.b.draw('1')
      data.b.draw('2')
    #await function.message_push(msg.guild, 'player-a-1', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('1')}")
    #await function.message_push(msg.guild, 'player-a-2', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('2')}")
    #await function.message_push(msg.guild, 'jikkyo-a', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('jikkyo')}")
    await function.message_push(msg.guild, 'bot_control', f'素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.current_situation(0, 0)}')

async def playera1(msg):
  if data.a.turn != '1':
    return #あなたの番じゃないよ
  text =  data.a.player_input('1', msg.content.upper())
  await function.message_push(msg.guild, 'player-a-1', text)
  if '相手にターンが渡ります。' in text:
    await function.message_push(msg.guild, 'player-a-1', data.a.turn_message('1'))
    await function.message_push(msg.guild, 'player-a-2', data.a.turn_message('2'))
    await function.message_push(msg.guild, 'jikkyo-a', data.a.turn_message('jikkyo'))
  return

async def playera2(msg):
  if data.a.turn != '2':
    return #あなたの番じゃないよ
  text =  data.a.player_input('2', msg.content.upper())
  await function.message_push(msg.guild, 'player-a-2', text)
  if '相手にターンが渡ります。' in text:
    await function.message_push(msg.guild, 'player-a-1', data.a.turn_message('1'))
    await function.message_push(msg.guild, 'player-a-2', data.a.turn_message('2'))
    await function.message_push(msg.guild, 'jikkyo-a', data.a.turn_message('jikkyo'))
  return

async def playerb1(msg):
  if data.b.turn != '1':
    return #あなたの番じゃないよ
  text =  data.b.player_input('1', msg.content.upper())
  await function.message_push(msg.guild, 'player-b-1', text)
  if '相手にターンが渡ります。' in text:
    await function.message_push(msg.guild, 'player-b-1', data.b.turn_message('1'))
    await function.message_push(msg.guild, 'player-b-2', data.b.turn_message('2'))
    await function.message_push(msg.guild, 'jikkyo-b', data.b.turn_message('jikkyo'))
  return

async def playerb2(msg):
  if data.b.turn != '2':
    return #あなたの番じゃないよ
  text =  data.b.player_input('2', msg.content.upper())
  await function.message_push(msg.guild, 'player-b-2', text)
  if '相手にターンが渡ります。' in text:
    await function.message_push(msg.guild, 'player-b-1', data.b.turn_message('1'))
    await function.message_push(msg.guild, 'player-b-2', data.b.turn_message('2'))
    await function.message_push(msg.guild, 'jikkyo-b', data.b.turn_message('jikkyo'))
  return