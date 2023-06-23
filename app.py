from flask import Flask, render_template, request
import openai 
from youtube_transcript_api import YouTubeTranscriptApi
openai.api_key = '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'

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_link', methods=['POST'])
def process_link():
    
    link = request.form.get('link')
    srt = YouTubeTranscriptApi.get_transcript("SW14tOda_kI")
    print(srt)
    prompt = f"""
    ```{link}```
    """
    response = get_completion(prompt)
    print(response)

    return f'The link "{response} {srt}" has been processed.'


def get_completion(prompt, model='gpt-3.5-turbo'):
    messages = [{'role':'user', 'content': prompt}]
    response = openai.ChatCompletion.create(
    model = model,
    messages = messages,
    temperature = 0,)
    return response.choices[0].message['content']

if __name__ == '__main__':
    app.run(debug=True)
