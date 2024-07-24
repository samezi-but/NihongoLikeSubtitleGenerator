# NihongoLikeSubtitleGenerator
[yes](main.png)
OpenAIのVisionとGPTシリーズを利用し、画面を流れるデスクトップ実況コメントを生成するツールです。
まだ不具合があるかも知れません。

## 使用ライブラリ

- Python 3.7+
- 以下のパッケージをインストールする必要があります（`requirements.txt`参照）:

```plaintext
  annotated-types==0.7.0
  anyio==4.4.0
  certifi==2024.7.4
  charset-normalizer==3.3.2
  colorama==0.4.6
  distro==1.9.0
  exceptiongroup==1.2.2
  h11==0.14.0
  httpcore==1.0.5
  httpx==0.27.0
  idna==3.7
  openai==1.37.0
  pillow==10.4.0
  pydantic==2.8.2
  pydantic_core==2.20.1
  requests==2.32.3
  sniffio==1.3.1
  tqdm==4.66.4
  typing_extensions==4.12.2
  urllib3==2.2.2
```

## インストール方法
Anacondaを使用した環境構築
Anacondaをインストールし、仮想環境を作成します:

```sh
conda create -n subtitles_env python=3.8
conda activate subtitles_env
```

リポジトリをクローンします:

```sh
git clone https://github.com/samezi-but/NihongoLikeSubtitleGenerator.git
cd NihongoLikeSubtitleGenerator
```

必要なPythonパッケージをインストールします:
```sh
pip install -r requirements.txt
```
# 注意！
apikey.txtというテキストファイルを作成してください。
OpenAI APIキーを入れること。でないと動きません。

## 設定
OpenAI APIキーをapikey.txtファイルに保存してください。
スクリプトは15秒ごとに画面内容をキャプチャします。この間隔はperiodic_capture関数で調整可能です。
## 使い方
メインスクリプトを実行します。

```sh
python main.py
```

## 注意
本スクリプトは、Tkinterの画面キャプチャ機能の都合上、Windows環境でのみ動作します。
