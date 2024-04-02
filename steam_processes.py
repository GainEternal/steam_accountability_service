import psutil
import re

def get_games_running():
    steam_location = r'\Steam\steamapps\common'
    game_list = set()
    for p in psutil.process_iter():
        try:
            executable_location = psutil.Process(p.pid).exe()
            if steam_location in executable_location:
                pattern = r'{}\\([^\\]+)\\'.format(re.escape(steam_location))
                match = re.search(pattern, executable_location)
                if match:
                    subdir = match.group(1)
            game_list.add(subdir)
        except:
            pass
    return list(game_list)