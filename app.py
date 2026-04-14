import os
from flask import Flask, request, render_template_string, jsonify
import requests

app = Flask(__name__)

# ضع مفتاح الـ API حقك هنا (من OpenRouter)
API_KEY = "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"

HTML_CHAT = '''
<!DOCTYPE html>
<html dir="rtl">
<head>
    <title>Dola AI Chat</title>
    <style>
        body { font-family: sans-serif; background: #343541; color: white; display: flex; flex-direction: column; height: 100vh; margin: 0; }
        #chat-box { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; }
        .msg { margin: 10px 0; padding: 15px; border-radius: 10px; max-width: 80%; }
        .user { background: #444654; align-self: flex-end; }
        .bot { background: #10a37f; align-self: flex-start; }
        #input-area { padding: 20px; background: #40414f; display: flex; }
        input { flex: 1; padding: 12px; border: none; border-radius: 5px; outline: none; }
        button { padding: 10px 20px; background: #10a37f; color: white; border: none; margin-right: 10px; cursor: pointer; }
    </style>
</head>
<body>
    <div id="chat-box"></div>
    <div id="input-area">
        <input type="text" id="user-input" placeholder="اسألني أي شيء...">
        <button onclick="sendMessage()">إرسال</button>
    </div>

    <script>
        async function sendMessage() {
            let input = document.getElementById('user-input');
            let box = document.getElementById('chat-box');
            if(!input.value) return;

            box.innerHTML += `<div class="msg user">${input.value}</div>`;
            let text = input.value;
            input.value = '';

            let response = await fetch('/ask', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({prompt: text})
            });
            let data = await response.json();
            box.innerHTML += `<div class="msg bot">${data.answer}</div>`;
            box.scrollTop = box.scrollHeight;
        }
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_CHAT)

@app.route('/ask', methods=['POST'])
def ask():
    user_prompt = request.json.get('prompt')
    
    # طلب الرد من الذكاء الاصطناعي (استخدام موديل مجاني من OpenRouter)
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "google/gemma-2-9b-it:free", # هذا موديل مجاني
            "messages": [{"role": "user", "content": user_prompt}]
        }
    )
    answer = response.json()['choices'][0]['message']['content']
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 7860)))
