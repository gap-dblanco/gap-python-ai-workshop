# File: /src/controllers/dev/analysis_controller.py
import json
import os

from jinja2 import Environment, FileSystemLoader
from sqlalchemy.orm.session import Session

# Set up Jinja2 environment
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "../../templates")
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

class AnalysisController:

    def run(self, session: Session):
        """
        Render the analysis JSON data as an HTML page.
        """
        # Load the JSON data
        ai_file = os.path.join(os.path.dirname(__file__), "../../../ai_code_analysis.json")
        with open(ai_file, "r") as file:
            json_data = json.loads(file.read())

        # Render the template with the JSON data
        template = env.get_template("analysis.html")
        return template.render(data=json_data)
