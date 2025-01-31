WEEK_SCHEDULE = "Schedule for the next week:\n\n{schedule}"

MORNING_REMINDER = "Good morning, {username}! Today you are on duty. Have a nice day :)"
EVENING_REMINDER = "Good evening, {username}! Tomorrow you will be on duty. Good luck :)"

REMINDER_MAP = {0: MORNING_REMINDER, 1: EVENING_REMINDER}

PERSON_ADDED = "User {username} was successfully added to schedule"
PERSON_REMOVED = "User {username} was removed from schedule"

HELP_START_TEXT = (
    "Use /week to get schedule for this week\n"
    "Use /create to create schedule for this week or you can "
    "wait for the end of the week and it will create automatically\n"
    "Use /add @username to add person to schedule\n"
    "Use /remove @username to remove person from schedule"
)
HELP_NO_SCHEDULE_TEXT = "There are no users in schedule"
HELP_ADD_TEXT = "Usage: /add @username"
HELP_REMOVE_TEXT = "Usage: /remove @username"
