# mypkg
ロボットシステム学の課題２で作成したプログラムです。

## 概要
講義内で作成したプログラムを一部改造して作成しました。 
３つのノードで自然数のカウントアップ、奇数のカウントアップ、偶数のカウントアップを表示することが出来ます。

## 動作環境
- Raspberry Pi 4 Model B 
- Ubuntu 20.04 
- ROS (Melodic Morenia)
 
## 実行手順 
以下の手順で実行してください。 

### ターミナル１

- リポジトリをクローンする

`$ cd catkin_ws/src` 
`$ git clone ` 

- コンパイルする

`$ cd ..` 
`$ catkin_make`
`$ source ~/.bashrc`

- ROSを起動する 

`$ roscore` 

### ターミナル２ 

- ディレクトリを移動する 

`$ cd catkin_ws/src/mypkg/scripts` 

- 各ファイルの実行許可を設定する 

`$ chmod +x count.py` 
`$ chmod +x even.py`_*1
`$ chmod +x odd.py`_*1
*1 
