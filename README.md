# pythonで素数大富豪bot作るぞ！！！
## ファイル内容

- const.py  
  必要なid系だったりtokenだったりを入れている  
  （githubに乗せないので、直接僕まで）  
- app.py  
  メインのファイル  
- channel.py  
  送られてきたチャンネルごとによって処理を変える  
- player_data.py  
  プレイヤーの状態を残す  

## 使うコマンド
- bot_control  
  - new_game  
  情報や役職をリセットする
  - role_set @player-a-1 @player-a-2 @player-b-1 @player-b-2  
  役職を決める
- プレイヤー系
  - 状況確認
  現在の状況を確認をする