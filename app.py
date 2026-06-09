import requests
import sys
import json

url = "http://localhost:11434/api/generate"

def generate(prompt: str):
    payload = {
        "model": "qwen3:4b",
        "prompt": prompt,
        "stream": False
    }
    try:
        resp = requests.post(url, json=payload, timeout=120)
    except Exception as e:
        print(f"Request failed: {e}")
        return None

    try:
        data = resp.json()
    except ValueError:
        print("Response was not JSON:\n", resp.text)
        return None

    # Preferred field
    if isinstance(data, dict) and "response" in data:
        return data["response"]

    # Fallback: try common shapes
    if isinstance(data, dict) and "choices" in data:
        # Ollama/other LLMs sometimes return choices with text
        choices = data.get("choices")
        if isinstance(choices, list) and choices:
            first = choices[0]
            if isinstance(first, dict):
                return first.get("text") or first.get("message") or json.dumps(first)
    # Last resort: return pretty JSON
    return json.dumps(data, indent=2)


def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = input("Enter your question: ")

    print("\nSending prompt to local Ollama API...\n")
    result = generate(prompt)

    print("\nModel Response:\n")
    print(result)


if __name__ == '__main__':
    main()
