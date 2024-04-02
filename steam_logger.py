class Steam_Logger():

    def __init__(self, log_filepath, width=40) -> None:
        self.filepath = log_filepath
        self.s = ''
        self.width = width

    def log(self, s:str=''):
        self.s += s + '\n'

    def section_break(self):
        self.s += '-' * self.width

    def write(self):
        with open(self.filepath, 'a') as f:
            f.write(self.s + '\n')
