import openai
import json

def generate_subtitles(screen_text, api_key):
    client = openai.OpenAI(api_key=api_key)
    
    parameters = {
        'engine': 'gpt-4o',
        'max_tokens': 1024,
        'temperature': 0.35,
        'stop': None
    }

    if screen_text == None:
        print("Error: Failed to recognize screen content.")
        return None
    message_count = 50

    response = client.chat.completions.create(
        model=parameters['engine'],
        messages=[
            {"role": "system", "content": "Make feel casual middle volume and short shout text. Generate subtitles for the screen content in Japanese language. It is one line of text. Be like niconico douga. be like brainless."},
            {"role": "user", "content": "This is recognized screen result. Make live commentary in Japanese. make "+ str(message_count) +" messages and differents comment, export for strict JSON style. Insert meanless meme word. Style use this [{'"'comment'"': '"'XXXX'"'},{'"'comment'"': '"'YYYY'"'}]You should limited answer JSON format text only.  If text show Japanese subtitle, read this.:"+screen_text}
        ],
        max_tokens=parameters['max_tokens'],
        temperature=parameters['temperature'],
        stop=parameters['stop']
    )
    print(response.choices[0].message.content)
    content = response.choices[0].message.content.replace("'",'"')
    try:
        subtitles = json.loads(content.strip("```").strip("json"))
    except json.JSONDecodeError as e:
        print(f"JSONDecodeError: {e}")
        return None
    print("JSON parsed successfully.")
    return subtitles