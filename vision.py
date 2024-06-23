import requests
from PIL import ImageGrab
import base64

def load_api_key(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print(f"Error: API key file '{file_path}' not found.")
        return None
    
# スクリーンショットを取得し、ファイルに保存する関数
def take_screenshot(file_path):
    screenshot = ImageGrab.grab()
    screenshot.save(file_path, 'JPEG')

# Vision API を呼び出して画像を分析する関数
def analyze_image(file_path):
    # 仮のAPIエンドポイントとAPIキー
    api_endpoint = "https://api.openai.com/v1/chat/completions"
    api_key = load_api_key('apikey.txt')

    with open(file_path, 'rb') as img_file:
        image_code =base64.b64encode(img_file.read()).decode('utf-8')
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                "role": "user",
                "content": [
                    {
                    "type": "text",
                    "text": "This is PC desktop screenshot. Don't exlain tab count. explain in this image more detail. 1line, no markdown"
                    },
                    {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_code}"
                    }
                    }
                ]
                }
            ],
            "max_tokens": 2048
        }
        response = requests.post(api_endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}")
        return None

def recognize_screen_content_detail():
    screenshot_file = "screenshot.jpg"
    
    # スクリーンショットの取得と保存
    take_screenshot(screenshot_file)
    
    # スクリーンショットの分析
    analysis_result = analyze_image(screenshot_file)

    # 結果の出力
    if analysis_result:
        print("Analysis Result: ", analysis_result['choices'][0]['message']['content'])
        return analysis_result['choices'][0]['message']['content']
    else:
        return None