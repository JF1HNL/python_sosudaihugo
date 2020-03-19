import function
import data

async def bot_control(msg):
  print(f'channel.bot_control: msg={msg}')
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
    await msg.channel.send(f'{msg.author.mention} 役職の設定が終わりました。')
  if ary[0] == 'new_game':
    await function.new_game(msg.guild)
  if ary[0] == 'game_start':
    for i in range(11):
      data.a.draw('1')
      data.a.draw('2')
      data.b.draw('1')
      data.b.draw('2')
    await function.message_push(msg.guild, 'player-a-1', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('1')}")
    await function.message_push(msg.guild, 'player-a-2', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('2')}")
    await function.message_push(msg.guild, 'jikkyo-a', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.a.turn_message('jikkyo')}")
    await function.message_push(msg.guild, 'player-b-1', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.b.turn_message('1')}")
    await function.message_push(msg.guild, 'player-b-2', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.b.turn_message('2')}")
    await function.message_push(msg.guild, 'jikkyo-b', f"素数大富豪スタート！\nお互いに11枚引きました。\n\n{data.b.turn_message('jikkyo')}")
    await msg.channel.send(f'{msg.author.mention} ゲームスタートしました。')
    return
  print(f"{ary[0]}が見当たりません。")

async def player(msg, a_or_b, player_num_):
  print(f'channel.player: msg={msg}, a_or_b={a_or_b}, player_num_={player_num_}')
  class_data = data.a
  if a_or_b == 'b':
    class_data = data.b
  if class_data.turn != player_num_:
    return #あなたの番じゃないよ
  return_obj = class_data.player_input(player_num_, msg.content.upper())
  print(f"channel.player return_obj={return_obj}")
  if return_obj['type'] == 'turn_continue': # まだ自分のターンが続くとき
    await msg.channel.send(return_obj['text'])
    return
  if return_obj['type'] == 'turn_end': # 自分のターンが終わるとき,全体で公開されるとき
    text = return_obj['text']
    await function.message_push(msg.guild, 'player-' + a_or_b + '-1', f"{text}\n{class_data.turn_message('1')}")
    await function.message_push(msg.guild, 'player-' + a_or_b + '-2', f"{text}\n{class_data.turn_message('2')}")
    await function.message_push(msg.guild, 'jikkyo-' + a_or_b, f"{text}\n{class_data.turn_message('jikkyo')}")
    return
  if return_obj['type'] == 'winner':
    await function.message_push(msg.guild, f'player-{a_or_b}-{player_num_}', f"＿人人人人人人＿\n＞　YOU WIN!　＜\n￣Y^Y^Y^Y^Y^Y^￣\n{class_data.current_situation(0,0)}")
    await function.message_push(msg.guild, f'player-{a_or_b}-{data.teki_num(player_num_)}', f"YOU LOSE\n{class_data.current_situation(0,0)}")
    await function.message_push(msg.guild, 'jikkyo-' + a_or_b, f"＿人人人人人人人＿\n＞　ゲーム終了　＜\n￣Y^Y^Y^Y^Y^Y^Y^￣\nプレイヤー{player_num_}が勝利しました。\n{class_data.current_situation(0,0)}")
    player1 = msg.guild.get_member(int(class_data.player['1'].id))
    player2 = msg.guild.get_member(int(class_data.player['2'].id))
    print(f'channel.player winner player1={player1}')
    print(f'channel.player winner player2={player2}')
    await function.role_change(player1, 'kankyaku')
    await function.role_change(player2, 'kankyaku')
    await function.message_push(msg.guild, 'bot_control', '役職設定終了しました。')
    return
  print(f"channel.player return_dict error : dict={return_obj}")

# reutrn_obj = {'type', 'text'}