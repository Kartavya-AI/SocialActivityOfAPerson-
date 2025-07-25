from flask import Flask, request, jsonify
import warnings
import os
from datetime import datetime
from src.social_activity_of_a_person.crew import SocialActivityOfAPerson

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

app = Flask(__name__)

@app.route("/analyze-social-activity", methods=["POST"])
def analyze_social_activity():
    data = request.get_json() or {}

    inputs = {
        'person': data.get('person', 'Om Anand'),
        'company': data.get('company', 'IIT bhilai'),
        'location': data.get('location', 'Bihar'),
        'current_year': str(datetime.now().year)
    }

    try:
        SocialActivityOfAPerson().crew().kickoff(inputs=inputs)

        output_file = "life_story.md"
        if not os.path.exists(output_file):
            return jsonify({
                "status": "error",
                "message": f"Expected output file '{output_file}' not found."
            }), 500

        with open(output_file, "r", encoding="utf-8") as f:
            report = f.read()

        return jsonify({
            "status": "success",
            "report": report
        }), 200

    except Exception as e:
        import traceback
        return jsonify({
            "status": "error",
            "message": str(e),
            "trace": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
