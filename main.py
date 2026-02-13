import sys
import os

# 현재 위치를 경로에 추가 (LMS 폴더를 찾기 위해)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# LMS 폴더 안의 진짜 app.py에서 app 객체를 가져옴
from LMS.app import app