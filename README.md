# Discordで素数大富豪をするぞ！
## ファイル内容

- [const.py](./const_.py)  
  必要なid系だったりtokenだったりを入れている  
  （GitHubに乗せないので、直接僕まで）  
  （GitHubにはダミーファイルとしてconst_.pyを乗せています。）
- [app.py](./app.py)  
  メインのファイル  
  ここには最低限必要なことを記入して、ほかのファイルにある関数を呼び出している。
- [channel.py](./channel.py)  
  送られてきたチャンネルごとによって処理を変える  
  チャンネルの分類ができたらここで分岐をかけている。
- [data.py](./data.py)  
  ゲームごとのデータやプレイヤーのデータ、プレイヤーの行動や素数判定などをクラスを使って整理して書いてある。
- [function.py](./function.py)  
  役職関係に関する関数がここに記入してある
- [delete.py](./delete.py)  
  投稿をけすためのpythonファイル。サーバーを起動した状態でチャンネルに投稿すると内容を全て消します。

## 使うコマンド
- #bot_control  
  - role_set {a or b} {@player-1} {@player-2}    
  メンションした人を指定した対戦のプレイヤーにメンションの順で設定します。
  - game_start {a or b}  
  指定した対戦のプレイヤーに手札を配り、ゲームをスタートさせる
  - game_reset {a or b}  
  指定した対戦のプレイヤーを観客に戻し、内容をリセットさせます
  - role_reset  
  参加しているメンバーを全て観客に変えます。
- #プレイヤー
  - d  
  ドロー  
  これは一ターンに一度だけ
  - p  
  パス
  - x  
  ジョーカー 
  これを出すときは内容を数字で答えてください。
  - g
  合成数だし