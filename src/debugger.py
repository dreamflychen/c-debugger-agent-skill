class Debugger:
    def __init__(self):
        self.breakpoints = []
        self.current_line = 0

    def set_breakpoint(self, line_number):
        if line_number not in self.breakpoints:
            self.breakpoints.append(line_number)

    def remove_breakpoint(self, line_number):
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)

    def run(self, code):
        lines = code.split('\n')
        while self.current_line < len(lines):
            if self.current_line in self.breakpoints:
                print(f'Breakpoint hit at line {self.current_line + 1}')
                input('Press Enter to continue...')
            exec(lines[self.current_line])
            self.current_line += 1

    def reset(self):
        self.current_line = 0
        self.breakpoints = []
