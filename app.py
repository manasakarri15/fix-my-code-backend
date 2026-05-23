from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Fix My Code Backend Running!"

@app.route('/fix-code', methods=['POST'])
def fix_code():
    data = request.json
    code = data.get("code", "")

    fixed_code = code
    explanation = []

    lines = fixed_code.split('\n')

    for i in range(len(lines)):
        line = lines[i].strip()

        if (
            line.startswith("if ")
            or line.startswith("for ")
            or line.startswith("while ")
            or line.startswith("def ")
        ) and not line.endswith(":"):
            lines[i] += ":"
            explanation.append(f"Added missing colon in line {i+1}")

    fixed_code = "\n".join(lines)

    return jsonify({
        "original_code": code,
        "fixed_code": fixed_code,
        "explanation": explanation
    })

if __name__ == '__main__':
    app.run(debug=True)
