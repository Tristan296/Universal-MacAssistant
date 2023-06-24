from dotenv import load_dotenv

from langchain.agents import initialize_agent
from langchain.llms import OpenAI

from commands import chrome_click_on_link, chrome_get_the_links_on_the_page, chrome_open_url, chrome_read_the_page, computer_applescript_action

load_dotenv()

llm = OpenAI(temperature=0) # type: ignore

tools = [
    computer_applescript_action,
    chrome_open_url,
    chrome_get_the_links_on_the_page,
    chrome_read_the_page,
    chrome_click_on_link
]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True) # type: ignore

