import sys
import os

# 현재 폴더 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 진짜 Flask 앱 가져오기
from LMS.app import app, socketio

# Vercel용 변수

if __name__ == '__main__':
    socketio.run(
        app,
        host='0.0.0.0',
        port=int(os.getenv('FLASK_APP_PORT', 5000)),
        debug=True,
        allow_unsafe_werkzeug=True
    )