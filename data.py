import random

class player:
  def __init__(self, id):
    self.id = id
    self.hand = []

class game:
  def __init__(self, a, b):
    self.turn = '1'
    self.field = []
    self.deck = [
      {'num':1,'char':'A'},{'num':1,'char':'A'},{'num':1,'char':'A'},{'num':1,'char':'A'},
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

  def card_dict_to_str(self, content_, type_, secret_):
    return_str = ''
    if content_ == '1':
      l = self.player[content_].hand
    elif content_ == '2':
      l = self.player[content_].hand
    else:
      l = self.__dict__[content_]
    for i in l:
      if secret_:
        return_str += '?'
      else:
        return_str += str(i[type_])
    return return_str

  def current_situation(self, one_secret, two_secret):
    player_1 = ''.join(list(map(lambda x: x['char'], self.player['1'].hand)))
    player_2 = ''.join(list(map(lambda x: x['char'], self.player['1'].hand)))
    field = ''.join(list(map(lambda x: x['char'], self.field)))
    if one_secret:
      player_1 = ''.join(list(map(lambda x: '?', self.player['1'].hand)))
    if two_secret:
      player_2 = ''.join(list(map(lambda x: '?', self.player['2'].hand)))
    return f"プレイヤー1:{player_1}\n場の状況:{field}\nプレイヤー2:{player_2}"

  def draw(self, player_num_):
    self.player[player_num_].hand.append(self.deck[0])
    self.deck.pop(0)
    self.player[player_num_].hand = sorted(self.player[player_num_].hand, key=lambda x : int(x['num']))


a = game(player(0), player(0))
b = game(player(0), player(0))