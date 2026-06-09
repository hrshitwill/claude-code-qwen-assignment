Quick test for Ollama + qwen3:4b

Requirements
- Ollama running locally and listening on http://localhost:11434
- qwen3:4b pulled into Ollama (`ollama pull qwen3:4b`)
- Python 3 and `requests` package

Run
1. Start Ollama server (if using brew services: `brew services start ollama`)
2. Run the script:
   python3 app.py

Example
> What is Generative AI?

The script will print the model's response or the full JSON returned by the local API.
# claude-code-qwen-assignment
