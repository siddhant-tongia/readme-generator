import sys
import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

if len(sys.argv) < 2:
    print("Usage: python readme_gen.py <file_path>")
    sys.exit(1)
def main():
    size = len(sys.argv)
    combined_code = ""

    def read_file(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content 
        
    first_file_path = sys.argv[1]

    if not os.getenv("API_KEY"):
        print("API_KEY not found in .env file")
        sys.exit(1)

    for i in range (1,size):
        file_path = sys.argv[i]

        if not (os.path.exists(file_path)):
            print("Error: File not found — check the path and try again")
            sys.exit(1)
        combined_code += f"\n\n# FILE: {os.path.basename(file_path)}\n"
        combined_code += read_file(file_path)

    def build_prompt(combined_code):
        return f'''Here is my code:{combined_code}.
        Generate a professional README with these sections:
        1. Project Title & what it does
        2. Problem it solves
        3. How it solves it
        4. Requirements / Installation
        5. How to run it on your computer
        6. Key Learnings
        7. Future improvements
        Format-Use proper Markdown with # headings and bullet points.
        Context-Infer the project details from the code itself.
        Important Note-If multiple files are provided, generate one combined README for the whole project.'''

    prompt=build_prompt(combined_code)

    print("Generating README, please wait...")

    def generate_readme(prompt):
        try:
            client = OpenAI(
            api_key=os.getenv("API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            )
            response = client.chat.completions.create(
                model="inclusionai/ring-2.6-1t:free",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating README: {e}")
            sys.exit(1)

    readme = generate_readme(prompt)

    def make_readme(readme, file_path):
        folder = os.path.dirname(os.path.abspath(file_path))
        save_path = os.path.join(folder, "README.md")
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(readme)
        print(f"README.md saved at: {save_path}")
        
    make_readme(readme,first_file_path)

if __name__=="__main__":
    main()