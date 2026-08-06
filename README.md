# 🎙️ Voice-to-Voice AI Assistant

A Python-based voice assistant that listens to the user's speech, converts it into text using **RealtimeSTT**, sends the request to **Cohere AI**, then converts the AI response back into speech using **RealtimeTTS**.

## Features

- 🎤 Real-time speech recognition
- 🤖 AI-generated responses using Cohere
- 🔊 Text-to-Speech output
- ⚡ Continuous voice conversation
- 🐍 Built with Python

## Technologies Used

- Python 3.11
- RealtimeSTT
- RealtimeTTS
- Cohere API
- Faster-Whisper
- PyAudio

## Screenshot

The screenshot below shows the assistant running successfully in Visual Studio Code.

![Voice AI Assistant](photoFor(1).jpg)

## How to Run

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Cohere API key:

```env
COHERE_API_KEY=your_api_key_here
```

5. Run the application:

```bash
python main.py
```

## Notes

- Do not upload your `.env` file.
- Do not upload the `venv` folder.
- A microphone is required for voice input.
