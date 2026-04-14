from flask import Flask, request, render_template_string
import os
import subprocess

app = Flask(__name__)

# واجهة التحكم البسيطة
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Bot Control Panel</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #f4f4f9; padding: 50px; }
        .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input { padding: 10px; width: 80%; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="card">
        <h2>إدارة استضافة البوتات</h2>
        <form method="POST">
            <input type="text" name="token" placeholder="أدخل توكن البوت (تليجرام أو ديسكورد)" required><br>
            <input type="text" name="admin_id" placeholder="الآيدي الخاص بك (اختياري)"><br>
            <button type="submit">تشغيل البوت الآن</button>
        </form>
        {% if msg %}<p style="color: blue;">{{ msg }}</p>{% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        token = request.form.get('token')
        # هنا تقدر تضيف المنطق الخاص بتشغيل البوت في الخلفية
        msg = f"تم استلام التوكن: {token[:10]}... وجاري التشغيل!"
    return render_template_string(HTML_TEMPLATE, msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
