# local-chat-messenger
ローカルシステムで動作するシンプルなチャットメッセンジャー

## 概要
欲しいデータの種類を入力することでダミーデータをテキストで取得できるアプリです。  
サーバーとクライアントをソケットで繋ぎ、対話形式でダミーデータを取得します。

## 環境構築
### clone
```
$ git clone git@github.com:fate7bardiche/local-chat-messenger.git
$ cd local-chat-messenger
```

### Poetryの準備(Poetryがインストールされていない場合のみ)
[Poetry Introduction](https://python-poetry.org/docs/#installing-with-the-official-installer)
```
$ curl -sSL https://install.python-poetry.org | python3 -
$ poetry --version
> Poetry (version 2.0.1)
```

### パッケージのインストール
```
$ poetry install
```

### 実行
サーバー側とクライアント側は、別のタブで実行してください。
```
# サーバー側
$ poetry run python server.py
```
```
# クライアント側
$ poetry run python client.py
```

## 使い方
欲しいデータをクライアント側から入力します。
- アプリ実行画面のキャプチャ
![スクリーンショット 2025-01-16 16 22 42](https://github.com/user-attachments/assets/36c28804-44a0-4aac-89ac-e239e4987bfc)