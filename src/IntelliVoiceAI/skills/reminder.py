import subprocess
from datetime import datetime, timedelta
from src.IntelliVoiceAI.core.voice_assistant import assistant

def create_reminder_in_app(reminder_text, reminder_datetime):
    script = f'tell application "Reminders" to make new reminder with properties {{name:"{reminder_text}", due date: date ("{reminder_datetime.strftime("%Y-%m-%dT%H:%M:%S")}"), remind me date: date ("{reminder_datetime.strftime("%Y-%m-%dT%H:%M:%S")}")}}'
    subprocess.run(["osascript", "-e", script])


def set_reminder():
    assistant.speak("What should I remind you about?")
    reminder = assistant.listen()

    assistant.speak("When did you want to be reminded?")
    reminder_time = assistant.listen()

    try:
        time_str = reminder_time.lower()  # Convert to lowercase for case insensitivity
        time_str = time_str.replace(".", "")  # Remove periods in the time string

        hour, minute = 0, 0
        if "pm" in time_str or "am" in time_str:
            time_parts = time_str.split()
            time_parts[0] = time_parts[0].replace("am", "").replace("pm", "")
            hour, minute = map(int, time_parts[0].split(":"))
            if "pm" in time_str and hour != 12:
                hour += 12

        now = datetime.now()
        reminder_datetime = now.replace(
            hour=hour, minute=minute, second=0, microsecond=0
        )
        if now > reminder_datetime:
            reminder_datetime = reminder_datetime + timedelta(
                days=1
            )  # Adjust the reminder time

        print(
            f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}."
        )

        # Execute the script via shell to create a new reminder in the Apple Reminders app
        create_reminder_in_app(reminder, reminder_datetime)

    except ValueError:
        print("Sorry, I couldn't understand the time you provided. Please try again.")
