

# DigitalArtMaker

Streamlit と ChatGPT API を用いて、ユーザー入力に基づいたデジタルアート (p5.js など) を生成する Web アプリです。

## 特長

- **インタラクティブアート生成**: ユーザーが入力したキーワードをもとに、ChatGPT API が p5.js のコードを自動生成
- **ストリーミング表示**: Streamlit により Web インターフェイスを構築
- **様々なアイデアに対応**: 入力キーワードやプロンプトを工夫することで、多種多様なアートを生成可能

## 実行例

アプリを起動した際の画面キャプチャ例です。

<img src="https://github.com/user-attachments/assets/d7e787e8-46e6-4454-b361-6d71fe37eb5a" width="400" alt="screenshot1" />
<img src="https://github.com/user-attachments/assets/3d6880f4-6e77-4698-be33-bdbf9345b70e" width="400" alt="screenshot2" />
<img src="https://github.com/user-attachments/assets/c5d6aad8-c337-45a0-ac69-cbbc9e10f485" width="400" alt="screenshot3" />

## 使い方

1.**OpenAI APIキーの用意**  
   [OpenAIの管理画面](https://platform.openai.com/account/api-keys)から APIキーを取得し、環境変数や設定ファイル にセットしてください。
   
2.**環境構築**  
必要なパッケージ (streamlit, openai ) をインストールします。

3.**アプリの起動**
```
streamlit run app.py
```
のようにしてアプリを起動します。

4.**アート生成**

画面が表示されたら、テキストボックスに任意のキーワード(例: 花火, 海, スペース)などを入力し、「生成する」ボタンをクリックしてください。
ChatGPT API が自動生成した p5.js コードによるインタラクティブアートが描画されます。
