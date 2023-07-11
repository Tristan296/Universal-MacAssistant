# Universal Assistant for MacOS

[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/Tristan296/82e0272a21bddb472fb3feebea622050/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)
[![CodeQL](https://github.com/Tristan296/Universal-MacAssistant/workflows/CodeQL/badge.svg)](https://github.com/Tristan296/Universal-MacAssistant/actions?query=workflow%3ACodeQL)

![alt text](https://github.com/Tristan296/LangChain-GPT-Voice-Assistant/blob/main/assistant_logo.png)

## Features

* **Voice Recognition**: Listens to user's voice commands and transcribes them to text.
* **Text-to-Speech**: Converts the assistant's text responses into voice and speaks them out.
* **Reminders**: Create reminders in the reminders app
* **To-do-list**: Create to do lists in the notes app
* **Internet Statistics**: Check internet speed and ping
* **Internet History**: Check previous internet results
* **Weather**: Get several weather metrics in chosen city
* **Files**: Open any file or folder without need for manual search
* **Siri Integration**: 
  * Create reminders
  * Open applications
  * Increase/reduce brightness and volume
  * Enable/disable WIFI and Bluetooth
  * Search the web

## Usage

1. Clone this repository with `git clone https://github.com/Tristan296/Universal-MacAssistant.git`
2. run `python setup.py install` in terminal
3. Open terminal and run `python3 main.py`
4. Choose from the available prompts

## Additional Features:

### OpenWeatherMap API:
- Create an openweather acccount and generate an api key
- in `.env` add api key to:
- `OPENWEATHER_API_KEY=your_key_here`

### Siri:
- To allow siri to work, please ensure 'Type to Siri' is enabled in system preferences:
  - `Accessbility > Siri > Type to siri`
 
## Example Prompts:
- Open apps and files -> "Open safari" or "Open setup.py"
- "What is my internet speed?" -> asks user what speed test metric and performs testing.
- "Where is the nearest cafe?" -> asks siri to find nearest cafe.

## Contribution

Feel free to fork this project, make some changes, and submit a pull request. All contributions are welcome!

## TODO:

- [ ] Integrate File system tools in MacOS
- [ ] Create more AppleScripts
 - In progress

## License

This project is licensed under the MIT License - see the LICENSE file for details.
