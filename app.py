from flask import Flask, render_template
import time
from datetime import datetime, timedelta

app = Flask(__name__)

# تسجيل وقت بدء التشغيل
start_time = datetime.now()

@app.route('/')
def home():
    # حساب مدة التشغيل
    uptime = datetime.now() - start_time
    seconds = int(uptime.total_seconds())
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return render_template('index.html', days=days, hours=hours, minutes=minutes, seconds=seconds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=False)
