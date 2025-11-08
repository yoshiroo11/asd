from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# This will hold submitted stories in memory (for demo only)
stories = []

@app.route('/submit-story', methods=['POST'])
def submit_story():
    data = request.json
    name = data.get('name', 'Anonymous')
    story = data.get('story')
    color = data.get('color', '#000')
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if not story or story.strip() == "":
        return jsonify({'error': 'Story is required.'}), 400

    story_entry = {
        'name': name,
        'story': story,
        'color': color,
        'date': date
    }
    stories.append(story_entry)

    return jsonify({'message': 'Story received!', 'story': story_entry}), 200

if __name__ == '__main__':
    app.run(debug=True)
