## Voice Assistant App

Welcome to the **Voice Assistant App**! This AI-powered application leverages cutting-edge technologies to assist users in performing various tasks through voice commands.

### Features

- **Play Songs**: Request your favorite songs, and the assistant will play them for you using VLC Media Player.
- **Recite Poems**: Enjoy beautiful poems recited by the assistant.
- **Write Messages**: Dictate messages, and the assistant will write them for you.
- **Voice Recognition**: Uses advanced speech-to-text technology to process user commands.
- **Natural Language Processing (NLP)**: Understands and interprets user requests effectively.
- **AI-Powered Chat**: Integrated with LangChain to enhance conversational abilities.

### Technologies Used

- **Python**: Core programming language.
- **SpeechRecognition**: Converts voice commands into text.
- **LangChain**: Powers advanced AI-driven conversational abilities.
- **OpenAI API**: Enables intelligent response generation.
- **VLC Media Player**: Handles music playback via the `python-vlc` library.
- **Pyttsx3**: Converts text to speech for responses.
- **Flask (Optional)**: If used, enables API-based interaction.
- **OS & subprocess modules**: Used for handling system commands and external processes.

### Installation

To get started with the Voice Assistant App, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/voice-assistant.git
    ```

2. Navigate to the project directory:
    ```sh
    cd voice-assistant
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Usage

To run the voice assistant, execute the following command:
```sh
python main.py
```

### How It Works (Internal Flow)

1. **User Input**: The assistant listens to voice commands via the microphone.
2. **Speech-to-Text**: `SpeechRecognition` converts spoken words into text.
3. **Processing Command**:
   - If it’s a song request, `python-vlc` plays the song using VLC Media Player.
   - If it’s a query, `LangChain` processes it with AI capabilities.
   - If it's a text-related request, `Pyttsx3` converts the response to speech.
4. **Response Generation**: The assistant replies via text-to-speech or executes the requested action.
5. **Execution**: The appropriate module handles the command (e.g., playing music, responding to queries, or writing text).

### Contributing

We welcome contributions! If you encounter any issues or have suggestions for improvements, feel free to submit issues or pull requests on our GitHub repository.

### Contact

For any inquiries or support, please contact [vinayiet435@gmail.com](mailto:vinayiet435@gmail.com).

Thank you for using the **Voice Assistant App**! 🎤🤖

