import re

class RulesEngine:
    """
    Uses a template-based mapping to determine expected output from an action.
    Falls back to a generic response if no direct mapping is found.
    """
    ACTION_TEMPLATES = {
        "login": "User is successfully logged in",
        "authenticate": "User gains access to the system",
        "reset": "Password reset confirmation sent",
        "recover": "Account recovery instructions sent",
        "search": "Relevant results are displayed",
        "upload": "File is successfully uploaded",
        "download": "File is downloaded successfully",
        "update": "Record is updated successfully",
        "delete": "Record is removed successfully",
        "generate": "Report is generated successfully"
    }

    @staticmethod
    def get_expected_output(action, input_data):
        action_lower = action.lower()

        # Exact match in template
        for key in RulesEngine.ACTION_TEMPLATES:
            if re.search(rf"\b{key}\b", action_lower):
                return RulesEngine.ACTION_TEMPLATES[key]

        # Fallback for unknown actions
        inputs_formatted = ", ".join(input_data) if input_data else "required data"
        return f"System processes the request to {action} using {inputs_formatted}"
