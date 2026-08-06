import os
from multiprocessing import freeze_support

import cohere
import pyttsx3
from dotenv import load_dotenv
from RealtimeSTT import AudioToTextRecorder


load_dotenv()

cohere_api_key = os.getenv("COHERE_API_KEY")

if not cohere_api_key:
    raise ValueError(
        "COHERE_API_KEY is missing. Add your Cohere API key to the .env file."
    )

co = cohere.ClientV2(api_key=cohere_api_key)


def generate_ai_response(user_text: str) -> str:
    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful voice assistant. "
                    "Reply briefly and clearly in the same language as the user."
                ),
            },
            {
                "role": "user",
                "content": user_text,
            },
        ],
    )

    return response.message.content[0].text.strip()


def speak(text: str) -> None:
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 165)
        engine.setProperty("volume", 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    except Exception as error:
        print(f"Text-to-Speech error: {error}")


def process_text(user_text: str) -> None:
    user_text = user_text.strip()

    if not user_text:
        return

    print(f"\nYou said: {user_text}")

    exit_words = {
        "exit",
        "quit",
        "stop",
        "خروج",
        "توقف",
        "إنهاء",
        "مع السلامة",
    }

    if user_text.lower() in exit_words:
        print("Assistant: مع السلامة")
        speak("مع السلامة")
        raise KeyboardInterrupt

    try:
        print("Generating response...")

        assistant_response = generate_ai_response(user_text)

        print(f"Assistant: {assistant_response}")
        speak(assistant_response)

    except Exception as error:
        print(f"Cohere error: {error}")


def main() -> None:
    print("=" * 50)
    print("Voice-to-Voice AI Assistant using Cohere")
    print("=" * 50)
    print("Speak into the microphone.")
    print("Say 'خروج' or press Ctrl + C to stop.")
    print()

    try:
        with AudioToTextRecorder(
            model="small",
            language="ar",
            spinner=False,
        ) as recorder:

            while True:
                print("Listening...")
                recorder.text(process_text)

    except KeyboardInterrupt:
        print("\nProgram stopped.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    freeze_support()
    main()