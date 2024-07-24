NihongoLikeSubtitleGenerator
このリポジトリには、デスクトップにAIを使用して字幕を生成し、表示するPythonスクリプトが含まれています。このプロジェクトは、さまざまなライブラリを活用してその機能を実現しています。

機能
画面内容認識: AIビジョンシステムを使用して画面からテキストを認識し抽出します。
字幕生成: 認識されたテキストからOpenAIのAPIを使用して字幕を生成します。
Tkinter GUI表示: 生成された字幕をTkinterウィンドウに表示します。
要件
Python 3.7+

以下のパッケージをインストールする必要があります（requirements.txt参照）:

plaintext
コードをコピーする
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
インストール
Anacondaを使用した環境構築
Anacondaをインストールし、仮想環境を作成します:

sh
コードをコピーする
conda create -n subtitles_env python=3.8
conda activate subtitles_env
リポジトリをクローンします:

sh
コードをコピーする
git clone https://github.com/samezi-but/NihongoLikeSubtitleGenerator.git
cd NihongoLikeSubtitleGenerator
必要なPythonパッケージをインストールします:

sh
コードをコピーする
pip install -r requirements.txt
OpenAI APIキーをプロジェクトのルートディレクトリにあるapikey.txtというファイルに追加します。

設定
OpenAI APIキーをapikey.txtファイルに保存してください。
スクリプトは15秒ごとに画面内容をキャプチャします。この間隔はperiodic_capture関数で調整可能です。
使い方
メインスクリプトを実行します:

sh
コードをコピーする
python main.py
Tkinterウィンドウが表示されます。スクリプトは定期的に画面内容をキャプチャし、テキストを認識し、字幕を生成し、ウィンドウに表示します。

注意
本スクリプトは、Tkinterの画面キャプチャ機能の都合上、Windows環境でのみ動作します。
ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
