import time
from datetime import datetime
import os

import steam_processes
from steam_logger import Steam_Logger

dir_path = os.path.dirname(os.path.realpath(__file__))
from dotenv import load_dotenv
dotenv_path = os.path.join(dir_path, '.env')
load_dotenv(dotenv_path)

log_path = os.path.join(dir_path, 'steam_log.txt')
logger = Steam_Logger(log_path)
logger.log(str(datetime.now()))
logger.section_break()

games = steam_processes.get_games_running()

game_state = os.path.join(dir_path, 'game_state.txt')
if os.path.exists(game_state):
    with open(game_state, 'r') as f:
        start_time = f.read()
else:
    start_time = ''

email_subject = ''
email_content = ''

if games and not start_time:
    logger.log('game started')
    # write current time to file
    with open(game_state, 'w') as f:
        new_start_time = time.time()
        f.write(str(new_start_time))
    # prep email
    email_subject = 'A Game Has Been Started'
    email_content = 'Sender is currently playing:\n'
    for game in games:
        email_content += str(game) + '\n'
elif start_time and not games:
    logger.log('game ended')
    # overwrite file with blank
    with open(game_state, 'w') as f:
        f.write('')
    # calculate time passed
    total_time = time.time() - float(start_time)
    # prep email
    hours = int(total_time // 3600)
    minutes = int((total_time % 3600) // 60)
    seconds = int((total_time % 60) // 1)
    email_subject = 'Game Ended'
    email_content = f'Play Complete. Total time: {hours:d} hrs {minutes:d} min {seconds:d} sec'

logger.log(f'subject: {email_subject}')
logger.log(f'content: {email_content}')

if email_content and email_subject:
    import steam_emailer
    receiver_email = os.environ.get('EMAIL_RECEIVER_EMAIL')
    sender_email = os.environ.get('GMAIL_SENDER_EMAIL')
    password = os.environ.get("GMAIL_SENDER_PASSWORD")
    steam_emailer.send_game_email(
        email_content, 
        sender_email, 
        password, 
        receiver_email, 
        email_subject, logger
        )
    logger.write()
