import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

load_dotenv()

# 1. 설정 초기화 (서버 켜질 때 한 번만 실행됨)
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)


def upload_file(file_obj, folder="uploads"):
    """
    파일을 Cloudinary에 업로드하고 URL을 반환하는 함수
    :param file_obj: request.files['file'] 객체
    :param folder: Cloudinary 내 저장할 폴더명 (기본값: communa)
    :return: 이미지 URL (실패 시 None)
    """
    if not file_obj:
        return None

    try:
        # 2. Cloudinary에 업로드
        upload_result = cloudinary.uploader.upload(
            file_obj,
            folder='uploads/' + folder,  # 클라우드 내 폴더명
            resource_type="auto"  # 이미지, 비디오 자동 감지
        )

        # 3. 업로드된 파일의 웹 주소(URL) 반환
        return upload_result.get('secure_url')

    except Exception as e:
        print(f"❌ 파일 업로드 실패: {e}")
        return None