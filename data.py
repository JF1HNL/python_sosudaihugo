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
    self.player = {'1':a, '2':b}

  def card_dict_to_str(self, content_, type_):
    return_str = ''
    l = self.__dict__[content_]
    for i in l:
      return_str += str(i[type_])
    return return_str

a = game(player(0), player(0))
b = game(player(0), player(0))