# LangChain GPT VoiceAssistant for MacOS

A Personal Assistant for Linux, MacOS and Windows

LangchainGPT converts your audio input to text using OpenAI's Whisper. Then, it uses a LangChain Agent to choose a set of actions, including generating AppleScript (for desktop automation) and JavaScript (for browser automation) commands from your prompt using OpenAI's GPT-3 ("text-davinci-003"), and then executing the resulting script. It then uses Google Text-To-Speech (GTTS) to convert text to audio.

## Features

* **Voice Recognition**: Listens to user's voice commands and transcribes them to text.
* **LangChain Chaining:** 'Chunks' user input into a new question which can be solved with tools and agents.
* **AI Commands**: Uses LLM to segment voice commands into separate prompts, which then get executed by agent.py
* **Text-to-Speech**: Converts the assistant's text responses into voice and speaks them out.
* **Reminders**: Create reminders in the reminders app
* **To-do-list**: Create to do lists in the notes app
* **Internet Statistics**: Check internet speed and ping
* **Internet History**: Check previous internet results
* **Weather**: Get several weather metrics in chosen city

## Usage

1. Download Repository folder or git clone https://github.com/Tristan296/LangchainGPT
2. run `python setup.py install` in terminal
3. In `.env` file add your OPENAI api key: `OPENAI_API_KEY=your_key_here` 
4. Open terminal and run `python3 main.py`
5. Choose from the available prompts or talk to ChatGPT

## Additional Features:

### OpenWeatherMap API:
- Create an openweather acccount and generate an api key
- in `.env` add api key to:
- `OPENWEATHER_API_KEY=your_key_here`

## Example Prompts:

- Find the result of a calculation. Prompt: "What is 5 * 5?" -> It will write AppleScript to open up a calculator and type in 5 * 5.
- Find restaurants nearby. Prompt: "Find restaurants near me" -> It will open up Google search, read the text on the page, and say the best restaurants.

## Video Example

https://github.com/Tristan296/LangchainGPT/assets/109927879/8878e476-83a5-4a6c-8c65-63289f3c1c5a

## Contribution

Feel free to fork this project, make some changes, and submit a pull request. All contributions are welcome!

## TODO:

- [ ] Integrate File system tools in MacOS
- [ ] Create more AppleScripts

## License

This project is licensed under the MIT License - see the LICENSE file for details.
