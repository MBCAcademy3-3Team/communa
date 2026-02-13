# 이 파일은 Vercel이 실행할 '가짜' 시작점입니다.
# 진짜 코드는 LMS 폴더 안에 있는 app.py를 불러와서 실행합니다.

import sys
import os

# 현재 폴더(flaskLMS)를 파이썬 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# LMS 폴더 안에 있는 app.py에서 'app' 객체를 가져옴
from LMS.app import app

# (중요) Vercel은 이 'app' 변수를 찾아서 서버를 킵니다.