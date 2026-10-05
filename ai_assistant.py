import requests
import os

from dotenv import load_dotenv

load_dotenv()


OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2"
)


def ask_ai(prompt):

    system_prompt = """
You are an AI academic assistant for a second-year B.Tech CSE student.

The student has college from 9:00 AM to 4:00 PM.

The student has a daily coding-test window from 8:00 PM to 10:00 PM.
A coding test takes 45 minutes.

Help the student improve:

1. Academic subjects
2. Programming
3. Data Structures and Algorithms
4. Technical skills
5. Communication
6. Teamwork
7. Problem solving
8. Interview preparation
9. Resume and GitHub skills
10. Future career skills

Give realistic advice that can fit around college hours.

Do not schedule study during college hours.
"""

    final_prompt = system_prompt + "\n\nStudent request:\n" + prompt

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": final_prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "I could not generate a response."
        )

    except requests.exceptions.ConnectionError:

        return (
            "⚠️ Ollama is not running.\n\n"
            "Start Ollama and try again."
        )

    except Exception as error:

        return f"⚠️ AI error: {error}"