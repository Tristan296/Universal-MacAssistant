from selenium import webdriver

driver = webdriver.Chrome()
driver.get("www.youtube.com")
# find last item and scroll to it
driver.execute_script("""
let items=document.querySelectorAll('.yt-formatted-string');
items[items.length-1].scrollIntoView();
""")