import streamlit as st
import openai
import os

# OpenAIのAPIキーを環境変数から読み込む
openai.api_key = os.getenv("OPENAIAPIKEY")

st.title("アートを生成")

# --- ユーザー入力欄 ---
user_input = st.text_input("アートのヒントとなる言葉を入力してください：",  placeholder="例: 花火"  )

# ボタンを押したら生成
if st.button("生成する"):
    if not user_input:
        st.warning("キーワードを入力してください。")
    else:
        # --- ChatGPT API を呼び出して p5.js コードを生成 ---

        prompt_for_chatgpt = f"""
        あなたは p5.js のエキスパートです。
        次のキーワードに関連する、デジタルアート(インタラクティブアートなど)を作る p5.js のスケッチコードを出力してください。
        キーワード: {user_input}

        条件:
         他のHTMLタグや説明文は出力に含めず、JavaScript のコードだけを出力してください。
         出力はコード本体のみとし、``` や説明文は含めないでください。
        """

        # 新API での呼び出し: openai.chat_completions.create(...)
        response = openai.chat.completions.create(
            model="gpt-4o",  # 実際に利用可能なモデルを指定
            messages=[
                {
                    "role": "system",
                    "content": "あなたは優秀なp5.jsの開発者です。"
                },
                {
                    "role": "user",
                    "content": prompt_for_chatgpt
                }
            ],
            temperature=0.7
        )

        # 生成されたスケッチコード（JavaScript部分のみ）
        # 新APIでは message["content"] のようにアクセス可能
        p5_code = response.choices[0].message.content

        # --- 生成されたコードを埋め込み ---
        html_code = f"""
        <html>
        <head>
          <script src="https://cdn.jsdelivr.net/npm/p5@1.4.2/lib/p5.js"></script>
        </head>
        <body>
          <script>
          {p5_code}
          </script>
        </body>
        </html>
        """

        # 画面に埋め込んで表示
        st.components.v1.html(html_code, height=600, scrolling=True)
