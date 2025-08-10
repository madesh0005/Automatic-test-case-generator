from flask import Flask, render_template, request, send_file
from test_case_generator import nlp_parser, rules_engine, test_case_writer
import os
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        requirements_text = ""
        
        # Option 1: Text area input
        if request.form.get("requirements"):
            requirements_text = request.form["requirements"]

        # Option 2: File upload
        uploaded_file = request.files.get("requirements_file")
        if uploaded_file and uploaded_file.filename:
            requirements_text = uploaded_file.read().decode("utf-8")

        if not requirements_text.strip():
            return render_template("index.html", error="Please enter or upload requirements.")

        # Process requirements
        test_cases = []
        counter = 1
        for line in requirements_text.split("\n"):
            line = line.strip()
            if not line:
                continue
            parsed_actions = nlp_parser.parse_requirements(line)
            for action, inputs in parsed_actions:
                expected_output = rules_engine.RulesEngine.get_expected_output(action, inputs)
                test_cases.append([f"TC{counter}", action, ", ".join(inputs), expected_output])
                counter += 1

        # Save to CSV in a temporary location
        output_path = os.path.join(tempfile.gettempdir(), "test_cases.csv")
        test_case_writer.write_test_cases(test_cases, output_path)

        return render_template("results.html", test_cases=test_cases, csv_path="download")

    return render_template("index.html")

@app.route("/download")
def download_csv():
    temp_path = os.path.join(tempfile.gettempdir(), "test_cases.csv")
    if os.path.exists(temp_path):
        return send_file(temp_path, as_attachment=True, download_name="test_cases.csv")
    return "No CSV file found", 404

if __name__ == "__main__":
    app.run(debug=True)
