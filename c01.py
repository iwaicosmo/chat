from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# 環境変数からAPIキーを取得
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    user_message = request.form['message']
    response = openai.Completion.create(
      engine="gpt-4",  # または使用する最新のエンジン名
      prompt=user_message,
      temperature=0.7,
      max_tokens=150,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0.6,
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)
