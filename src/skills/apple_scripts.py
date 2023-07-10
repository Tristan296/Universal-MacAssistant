import subprocess
import re 
import os


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

    search_results = output.strip().split(',')
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


def filter_search(query, results):
    extensions = {}

    # Iterate over each path and extract the file name and extension
    for path in results:
        basename = os.path.basename(path)
        result = re.sub(r'\.\w+$', '', basename)
        extension = os.path.splitext(basename)[1]
        if extension == "":
            break
        extensions[path] = {'file_name': result, 'file_extension': extension}
    
    return extensions

def open_file(query):
    # Extract the file name from the query
    match = re.search(r'open\s+(\S+)', query)
    if match:
        file = match.group(1)
        results = spotlight_search(file)
        filtered_results = filter_search(query, results)

        # Check if any matching files are found
        if filtered_results:
            file_path = next(iter(filtered_results))  # Get the first matching file path
            subprocess.call(['open', file_path])
            quit()
        else:
            print("No matching files found.")
    else:
        print("Invalid command format. Please provide the file name.")
