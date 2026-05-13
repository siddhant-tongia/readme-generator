# README Generator CLI

## 📌 Project Title

**readme_gen.py** — An Automated README Generator Powered by LLMs

A lightweight command-line tool that analyzes your source code files and automatically generates a professional, well-structured README.md using a Large Language Model (LLM) via the OpenRouter API.

---

## 🔍 Problem It Solves

Writing documentation is one of the most overlooked yet essential parts of software development. Creating a quality README involves:

- **Time and effort** — Manually summarizing what your code does, how to install it, and how to run it is tedious.
- **Inconsistency** — Different projects end up with READMEs of varying quality, some incomplete or missing key sections.
- **Developer friction** — Many developers would rather write code than documentation, leading to neglected project pages.

This tool eliminates the manual effort by **automatically inferring project details from your source code** and producing a polished README in seconds.

---

## 🛠️ How It Solves It

The script follows a clean pipeline:

1. **Input** — Accepts one or more file paths as command-line arguments.
2. **Code Reading** — Reads the content of each file with UTF-8 encoding, ensuring broad compatibility.
3. **Prompt Construction** — Dynamically builds a detailed prompt that includes:
   - The full source code of all provided files (tagged with filenames).
   - Clear instructions specifying the desired README structure.
   - Guidance to handle multi-file projects as a single cohesive document.
4. **LLM Communication** — Sends the prompt to the **InclusionAI Ring 2.6-1T** model via the **OpenRouter** API (an OpenAI-compatible endpoint).
5. **Output** — Writes the LLM-generated response as `README.md` in the directory of the first provided file.

Key architectural decisions:
- **Nested helper functions** keep the logic encapsulated within `main()`, preventing namespace pollution.
- **Error handling** covers missing API keys, non-existent files, and API communication failures with descriptive messages.
- **`.env` integration** securely loads the API key without hardcoding secrets.

---

## 📦 Requirements / Installation

### Prerequisites
- **Python 3.8+**
- An **OpenRouter API key** (free tier available at [openrouter.ai](https://openrouter.ai))

### Setup

1. **Clone or download** this repository.

2. **Install dependencies:**
   ```bash
   pip install openai python-dotenv
   ```

3. **Create a `.env` file** in the same directory as the script and add your API key:
   ```env
   API_KEY=your_openrouter_api_key_here
   ```

---

## 🚀 How to Run It on Your Computer

### Basic Usage (Single File)
```bash
python readme_gen.py my_script.py
```
This generates a `README.md` in the same directory as `my_script.py`.

### Multi-File Usage (Entire Project)
```bash
python readme_gen.py main.py utils.py config.py
python readme_gen.py src/*.py
```
This produces **one combined README.md** covering the entire project, placed in the directory of the first file.

### What Happens Under the Hood
```
python readme_gen.py app.py helpers.py
    │
    ├── 1. Reads app.py + helpers.py
    ├── 2. Builds a detailed prompt describing the code
    ├── 3. Sends prompt to InclusionAI Ring 2.6-1T via OpenRouter
    └── 4. Saves the AI-generated README.md to your project folder
```

---

## 📚 Key Learnings

- **LLMs for documentation** — Large language models can effectively interpret code structure, dependencies, and intent to produce meaningful documentation.
- **OpenAI-compatible APIs** — Using `base_url` in the OpenAI Python client makes it simple to swap between OpenAI's own models and third-party providers like OpenRouter.
- **Prompt engineering matters** — The quality of the generated README heavily depends on the prompt's clarity, specificity, and context provided.
- **Multi-file awareness** — Tagging each file with `# FILE: filename` in the prompt helps the LLM understand project structure and write coherent documentation.
- **Environment-based secrets** — Using `python-dotenv` to load API keys from `.env` files is a simple yet effective security practice for local development.

---

## 🔮 Future Improvements

| Improvement | Description |
|---|---|
| **Model selection via CLI flag** | Allow users to specify which LLM to use (e.g., `--model claude-sonnet`) instead of hardcoding it. |
| **Recursive directory scanning** | Support passing a directory path and auto-discovering all source files within it. |
| **Configurable prompt templates** | Let users customize or extend the README sections through a config file. |
| **Markdown preview mode** | Add a `--dry-run` flag that prints the README to stdout without writing to disk. |
| **Append mode** | Detect an existing README.md and offer to append/update specific sections instead of overwriting. |
| **Rate limiting & retry logic** | Implement exponential backoff for handling API rate limits gracefully. |
| **Support for more languages** | Extend beyond Python — detect file types and adjust the prompt context for JavaScript, TypeScript, C++, etc. |
| **GitHub Actions / CI integration** | Auto-generate READMEs as part of a CI/CD pipeline on every commit. |
| **Dependency analysis** | Parse imports/requires to auto-generate a dedicated "Dependencies" section. |
| **Custom output path** | Add an optional `--output` flag to specify where the README.md should be saved. |

---

*Built with ❤️ to make documentation the least painful part of shipping code.*