from flask import Flask, request, jsonify, send_from_directory
import requests
import base64
from dotenv import load_dotenv
import os
app = Flask(__name__)
load_dotenv()
GAK = os.environ.get('googleAPI')
GCE= os.environ.get('googleCustomEngine')
print(GAK, GCE)
######################## DO NOT TOUCH ######################## 
GOOGLE_API_KEY = GAK
CX = GCE
VISION_API_KEY = GAK
######################## DO NOT TOUCH ######################## 


def analyze_image(image_url):
    try:
        # 이미지 다운로드
        response = requests.get(image_url)
        image_content = response.content
        base64_image = base64.b64encode(image_content).decode('utf-8')

        # Google Cloud Vision API URL
        vision_url = f'https://vision.googleapis.com/v1/images:annotate?key={VISION_API_KEY}'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "requests": [
                {
                    "image": {
                        "content": base64_image
                    },
                    "features": [
                        {"type": "SAFE_SEARCH_DETECTION"}
                    ]
                }
            ]
        }
        response = requests.post(vision_url, headers=headers, json=data)
        result = response.json()

        # 응답 구조 디버깅
        print("Google Vision API 응답:", result)

        # Safe Search Detection 결과 확인
        if 'responses' in result and len(result['responses']) > 0:
            safe_search = result['responses'][0].get('safeSearchAnnotation', {})
            adult_score = safe_search.get('adult', '')
            racy_score = safe_search.get('racy', '')

            if adult_score in ['LIKELY', 'VERY_LIKELY', 'POSSIBLE'] or racy_score in ['LIKELY', 'VERY_LIKELY', 'POSSIBLE']:
                return 'AGE_VERIFICATION_REQUIRED'
            else:
                return 'SAFE'
        else:
            print('유효하지 않은 응답 구조:', result)
            return 'UNKNOWN'
    except Exception as e:
        print(f'이미지 분석 중 오류 발생: {e}')
        return 'ERROR'

@app.route('/search', methods=['POST'])
def search_images():
    data = request.get_json()
    query = data.get('query')
    num_results = data.get('num_results', 10)  # 가져올 결과 수
    results_per_page = 10  # 페이지당 최대 결과 수

    if not query:
        return jsonify({'error': '쿼리가 필요합니다'}), 400

    image_links = []
    try:
        # 페이지네이션을 사용해 이미지 검색
        for start_index in range(1, num_results + 1, results_per_page):
            search_url = (
                f'https://www.googleapis.com/customsearch/v1'
                f'?q={query}&key={GOOGLE_API_KEY}&cx={CX}&searchType=image'
                f'&start={start_index}&num={results_per_page}&gl=jp'
            )
            response = requests.get(search_url)
            response.raise_for_status()
            search_data = response.json()

            # 검색 데이터 오류 확인
            if 'items' not in search_data:
                break

            # 이미지 분석 및 필터링
            for item in search_data.get('items', []):
                img_url = item.get('link')
                page_url = item.get('image', {}).get('contextLink', '')
                status = analyze_image(img_url)
                if status == 'AGE_VERIFICATION_REQUIRED':
                    image_links.append({'url': img_url, 'pageUrl': page_url, 'status': 'AGE_VERIFICATION_REQUIRED'})
                elif status == 'SAFE':
                    # SAFE 상태인 이미지를 포함시키지 않으려면 이 부분을 주석 처리하세요
                    pass

            # 더 이상 결과가 없으면 종료
            if 'nextPage' not in search_data.get('queries', {}):
                break

        return jsonify({'images': image_links})

    except requests.RequestException as e:
        print(f'오류 발생: {e}')
        return jsonify({'error': '이미지 검색 중 오류가 발생했습니다.'}), 500

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/aggressive')
def ag():
    return send_from_directory('service', 'aggressive.html')

if __name__ == '__main__':
    app.run(debug=False)