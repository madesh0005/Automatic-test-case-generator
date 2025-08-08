# 🧪 Automated Test Case Generator for Software QA (Group 12)

This project automatically generates **test cases** from **natural language software requirements** using **NLP (Natural Language Processing)** and **rule-based logic**.

---
## 🚀 Features

- Accepts plain English requirements (e.g., "Login with email and password")
- Uses NLP to extract actions and inputs
- Applies rules to generate expected outputs
- Saves test cases in CSV format
- Easy to extend with more rules

---

## 📁 Project Structure

automated-test-case-generator/
│
├── main.py # Main controller script
├── sample_requirements.txt # Input: natural language requirements
├── requirements.txt # Python dependencies
│
├── test_case_generator/
│ ├── init.py
│ ├── nlp_parser.py # Extracts action and input from text
│ ├── rules_engine.py # Maps action to expected output
│ └── test_case_writer.py # Writes test cases to CSV
│
└── output/
└── test_cases.csv # Output: auto-generated test cases



##Install dependencies:

pip install -r requirements.txt
python3 -m spacy download en_core_web_sm

##Run the project:
python3 main.py

##Example Input (sample_requirements.txt)
Login with email and password
Reset password using email
Search product by name


## Example Output (output/test_cases.csv)
ID	Action	  Input	            Expected Output
TC1	Login	    email, password	  Dashboard is displayed
TC2	Reset	    email	Password    reset link sent
TC3	Search	  product name	    Product results shown

👥 Authors

MADHANRAJ V (TEAM LEAD)
MADESHWARAN M
LOKESHWARAN B
MADHAN E
