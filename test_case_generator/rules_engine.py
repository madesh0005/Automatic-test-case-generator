def generate_test_cases(sentences):
    test_cases = []
    for i, sentence in enumerate(sentences):
        sentence_lower = sentence.lower()

        if "log in" in sentence_lower or "login" in sentence_lower:
            test_cases.append({
                "ID": f"TC{i+1}",
                "Action": "Login",
                "Input": "Email and Password",
                "Expected Output": "Dashboard is displayed"
            })
        elif "error message" in sentence_lower:
            test_cases.append({
                "ID": f"TC{i+1}",
                "Action": "Invalid Login",
                "Input": "Wrong credentials",
                "Expected Output": "Error message is shown"
            })
        elif "reset" in sentence_lower and "password" in sentence_lower:
            test_cases.append({
                "ID": f"TC{i+1}",
                "Action": "Reset Password",
                "Input": "Email",
                "Expected Output": "Reset link sent to email"
            })
        elif "dashboard" in sentence_lower:
            test_cases.append({
                "ID": f"TC{i+1}",
                "Action": "Post-login",
                "Input": "Valid login",
                "Expected Output": "Dashboard appears"
            })
        else:
            test_cases.append({
                "ID": f"TC{i+1}",
                "Action": "Unknown",
                "Input": "N/A",
                "Expected Output": sentence
            })
    return test_cases
