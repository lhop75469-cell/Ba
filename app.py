import os
import subprocess
from flask import Flask, request, render_template_string

app = Flask(__name__)

# واجهة التحكم
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html dir="rtl">
<head>
    <title>لوحة تحكم البوتات</title>
    <style>
        body { font-family: sans-serif; text-align: center; background: #f4f4f9; padding: 50px; }
        .card { background: white; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 350px; }
        input { padding: 12px; width: 90%; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; text-align: center; }
        button { padding: 12px 25px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; width: 95%; }
        .status { margin-top: 15px; color: #007bff; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h2>إدارة استضافة البوتات</h2>
        <form method="POST">
            <input type="text" name="token" placeholder="أدخل توكن البوت هنا" required>
            <input type="text" name="admin_id" placeholder="الآيدي الخاص بك (اختياري)">
            <button type="submit">تشغيل البوت الآن 🚀</button>
        </form>
        {% if msg %}<div class="status">{{ msg }}</div>{% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
    if request.method == 'POST':
        token = request.form.get('token')
        admin_id = request.form.get('admin_id')
        
        # تشغيل ملف البوت الأساسي مع إرسال التوكن كمتغير بيئة
        try:
            subprocess.Popen(["python", "bot_template.py", token, admin_id])
            msg = "✅ تم تشغيل البوت بنجاح! اذهب لتجربته الآن."
        except Exception as e:
            msg = f"❌ حدث خطأ أثناء التشغيل: {str(e)}"
            
    return render_template_string(HTML_TEMPLATE, msg=msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port)
