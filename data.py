import random
import const
import sympy

class player:
  def __init__(self, id):
    self.id = id
    self.hand = []

class game:
  def __init__(self, a, b):
    self.turn = '1'
    self.kakumei = False
    self.draw_flag = False
    self.field = []
    self.graveyard = []
    self.joker_memory = {'text': '', 'replace':[]}
    self.deck = [
      {'num':1,'char':'1'},{'num':1,'char':'1'},{'num':1,'char':'1'},{'num':1,'char':'1'},
      {'num':2,'char':'2'},{'num':2,'char':'2'},{'num':2,'char':'2'},{'num':2,'char':'2'},
      {'num':3,'char':'3'},{'num':3,'char':'3'},{'num':3,'char':'3'},{'num':3,'char':'3'},
      {'num':4,'char':'4'},{'num':4,'char':'4'},{'num':4,'char':'4'},{'num':4,'char':'4'},
      {'num':5,'char':'5'},{'num':5,'char':'5'},{'num':5,'char':'5'},{'num':5,'char':'5'},
      {'num':6,'char':'6'},{'num':6,'char':'6'},{'num':6,'char':'6'},{'num':6,'char':'6'},
      {'num':7,'char':'7'},{'num':7,'char':'7'},{'num':7,'char':'7'},{'num':7,'char':'7'},
      {'num':8,'char':'8'},{'num':8,'char':'8'},{'num':8,'char':'8'},{'num':8,'char':'8'},
      {'num':9,'char':'9'},{'num':9,'char':'9'},{'num':9,'char':'9'},{'num':9,'char':'9'},
      {'num':10,'char':'T'},{'num':10,'char':'T'},{'num':10,'char':'T'},{'num':10,'char':'T'},
      {'num':11,'char':'J'},{'num':11,'char':'J'},{'num':11,'char':'J'},{'num':11,'char':'J'},
      {'num':12,'char':'Q'},{'num':12,'char':'Q'},{'num':12,'char':'Q'},{'num':12,'char':'Q'},
      {'num':13,'char':'K'},{'num':13,'char':'K'},{'num':13,'char':'K'},{'num':13,'char':'K'},
      {'num':77,'char':'X'},{'num':77,'char':'X'}
    ]
    random.shuffle(self.deck)
    # self.deck = random.shuffle(self.deck)
    self.player = {'1':a, '2':b}

  def current_situation(self, one_secret, two_secret):
    player_1 = ', '.join(list(map(lambda x: x['char'], self.player['1'].hand)))
    player_2 = ', '.join(list(map(lambda x: x['char'], self.player['2'].hand)))
    field = ', '.join(list(map(lambda x: x['char'], self.field)))
    field_num = ''.join(list(map(lambda x: str(x['num']), self.field)))
    if one_secret:
      player_1 = ', '.join(list(map(lambda x: '?', self.player['1'].hand)))
    if two_secret:
      player_2 = ', '.join(list(map(lambda x: '?', self.player['2'].hand)))
    return f"```\nプレイヤー1:{player_1}\n場の状況:{field} ({field_num})\nプレイヤー2:{player_2}\n```"

  def draw(self, player_num_):
    self.player[player_num_].hand.append(self.deck[0])
    self.deck.pop(0)
    self.player[player_num_].hand = sorted(self.player[player_num_].hand, key=lambda x : int(x['num']))

  def hand_sort(self):
    sorted(self.player['1'].hand, key=lambda x : int(x['num']))
    sorted(self.player['2'].hand, key=lambda x : int(x['num']))

  def turn_message(self, player_num_):
    if player_num_ == 'jikkyo':
      return f'{self.current_situation(1, 1)}\n\nプレイヤー{self.turn}の番です。'
    if player_num_ == self.turn:
      return f"{self.current_situation(not player_num_ == '1', not player_num_ == '2')}\nあなたのターンです。\n素数はそのままアルファベットで記入\nx はジョーカーでスペースを開けてから、xの値を記入\nd はドロー\np はパス"
    else:
      return f"{self.current_situation(not player_num_ == '1', not player_num_ == '2')}\n相手のターンです。しばらくお待ちください。"

  def player_input(self, player_num_, text_):  # text_は大文字
    if text_ == 'D':
      if self.draw_flag:
        return "すでに一枚引きました！"
      self.draw(player_num_)
      self.draw_flag = True
      return f"一枚引きました。\n{self.current_situation(not player_num_ == '1', not player_num_ == '2')}\n素数はそのままアルファベットで記入\nx はジョーカーでスペースを開けてから、xの値を記入\np はパス"
    if text_ == 'P':
      self.graveyard.extend(self.field)
      self.field = []
      self.draw_flag = False
      self.turn = teki_num(player_num_)
      return 'パスしました。'
    if 'X' in text_: #ジョーカーを含んでいた時
      self.joker_memory['text'] = text_
      self.joker_memory['replace'] = []
      return 'ジョーカーが選択されたので、最初のジョーカーの代わりとなる数字を入力してください。'
    if self.joker_memory['text'] != '': # ジョーカーのあとの処理
      self.joker_memory['replace'].append(text_)
      if len(self.joker_memory['replace']) != self.joker_memory['text'].count('X'): # ジョーカー二枚つかってたとき
        return 'もう一枚のジョーカーの代わりとなる数字を入力してください'
      text_ = self.joker_memory['text']
      self.joker_memory['text'] = ''
    player_input_list = []
    for char in text_:
      if not char in list(map(lambda x : x['char'], self.player[player_num_].hand)):
        self.player[player_num_].hand.extend(player_input_list)
        self.hand_sort()
        return f'{char}が手札にありません！'
      elif char == 'X':
        self.player[player_num_].hand.pop( # 削除
          int(
            list(map(lambda x : x['char'], self.player[player_num_].hand)).index(char)
          )
        )
        player_input_list.append({'num': int(self.joker_memory['replace'].pop(0)), 'char': 'X'})
      else:
        player_input_list.append(
          self.player[player_num_].hand.pop(
            int(
              list(map(lambda x : x['char'], self.player[player_num_].hand)).index(char)
            )
          )
        )
    player_input_obj =  {'char':''.join(list(map(lambda x : x['char'], player_input_list))), 'num':''.join(list(map(lambda x : str(x['num']), player_input_list)))}
    if self.field != []:
      field_obj =  {'char':''.join(list(map(lambda x : x['char'], self.field))), 'num':''.join(list(map(lambda x : str(x['num']), self.field)))}
      if len(field_obj['char']) != len(player_input_obj['char']):
        self.player[player_num_].hand.extend(player_input_list)
        return 'フィールドの札の枚数と出した札の枚数が違います'
      if int(field_obj['num']) >= int(player_input_obj['num']) and not self.kakumei:
        self.player[player_num_].hand.extend(player_input_list)
        return 'フィールドの札の数のほうが大きいです'
      if int(field_obj['num']) <= int(player_input_obj['num']) and self.kakumei:
        self.player[player_num_].hand.extend(player_input_list)
        return 'ラマヌジャン革命中です。フィールドの札の数のほうが小さいです'
    self.draw_flag = False
    self.graveyard.extend(self.field)
    self.field = []
    self.turn = teki_num(player_num_)
    if sympy.isprime(int(player_input_obj['num'])) is True:
      self.field.extend(player_input_list)
      return f"{player_input_obj['num']}は素数です！相手にターンが渡ります。"
    if player_input_obj['num'] == '57':
      self.turn = teki_num(player_num_)
      self.graveyard.extend(player_input_list)
      return f"グロタンディーク素数切りです。場が流れプレイヤー{player_num_}の番です。"
    if player_input_obj['num'] == '1729':
      self.field.extend(player_input_list)
      return 'ラマヌジャン革命です。今後は値が小さい数を出してください。'
    else:
      self.player[player_num_].hand.extend(player_input_list)
      for i in player_input_list:
        self.draw(player_num_)
      return f"{player_input_obj['num']}は素数ではありません。ペナルティーが発生しました。相手にターンが渡ります。"

a = game(player(0), player(0))
b = game(player(0), player(0))

def teki_num(e):
  if e == '1':
    return '2'
  if e == '2':
    return '1'
  return 'error'