import function

async def bot_control(msg):
  ary = msg.content.split()
  if ary[0] == 'role_set':
    ary.remove('role_set')
    if not len(ary) == 4:
      await msg.channel.send(f'{msg.author.mention} memberが足りません。')
      return
    user_id = ary[0].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-a-1')
    user_id = ary[1].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-a-2')
    user_id = ary[2].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-b-1')
    user_id = ary[3].translate(str.maketrans({'<':'', '>': '', '@':'', '!':''}))
    member = msg.guild.get_member(int(user_id))
    await function.role_change(member, 'player-b-2')