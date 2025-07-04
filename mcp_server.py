from flask import Flask, request, jsonify
from educhain import Educhain
from dotenv import load_dotenv
import logging
import os

load_dotenv()

app = Flask(__name__)
generator = Educhain()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/generate_mcqs', methods=['POST'])
def generate_mcqs_endpoint():
    try:
        data = request.json
        topic = data.get('topic', '')
        count = int(data.get('count', 5))

        mcqs = generator.generate_mcqs(topic=topic, count=count)  # ✅ CORRECTED

        return jsonify({"data": mcqs})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/generate_lesson_plan', methods=['POST'])
def generate_lesson_plan_endpoint():
    try:
        data = request.json
        subject = data.get('subject', '')

        lesson_plan = generator.generate_lesson_plan(topic=subject)  # ✅ CORRECTED

        return jsonify({"data": lesson_plan})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/generate_flashcards', methods=['POST'])
def generate_flashcards_endpoint():
    try:
        data = request.json
        topic = data.get('topic', '')
        count = int(data.get('count', 10))

        if not topic:
            return jsonify({"error": "Topic is required"}), 400

        flashcards = generator.generate_flashcards(topic=topic, count=count)  # ✅ Already correct
        return jsonify({"status": "success", "data": flashcards})
    except Exception as e:
        logger.error(f"Error in flashcard generation: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
