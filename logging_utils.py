LOG_FILE = "keylogger_logs.txt"

def append_log(string):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(string + "\n")