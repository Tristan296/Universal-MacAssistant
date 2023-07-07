import subprocess

def spotlight_search(query):
    script = f'''
        set query to "{query}"
        set searchResults to paragraphs of (do shell script "mdfind -name " & quoted form of query)
        return searchResults
    '''

    process = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate(script)

    if error:
        print(f"Error: {error.strip()}")
        return []

    search_results = output.strip().split('\n')
    return search_results

def ask_siri(prompt):
    script = f"""
    tell application "System Events" to tell the front menu bar of process "SystemUIServer"
        tell (first menu bar item whose description is "Siri")
            perform action "AXPress"
        end tell
    
    keystroke "{prompt}"
    keystroke return
    end tell
    """
    
    process = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    process.communicate(script)

