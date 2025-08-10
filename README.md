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

##📂 Project Structure


Madesh project/
│── app.py
│── config.py
│── requirements.txt
│── history.db
│── static/
│    └── style.css
│── templates/
│    └── *.html
│── utils/
│    └── *.py
│── README.md

##📄 License
MIT License




##venv selection
python3 -m venv venv
source venv/bin/activate

##3. Install dependencies
pip install -r requirements.txt

##4. Run in development (HTTP)
python app.py

##Visit:
http://127.0.0.1:5000


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

MADHANRAJ V
MADESHWARAN M
LOKESHWARAN B
MADHAN E
