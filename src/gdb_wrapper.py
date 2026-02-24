# GDB Wrapper Module

class GDBWrapper:
    def __init__(self, gdb_path):
        self.gdb_path = gdb_path

    def start_session(self):
        """Starts a GDB session."""
        import subprocess
        self.process = subprocess.Popen([self.gdb_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return self.process

    def execute_command(self, command):
        """Executes a command in the GDB session."""
        if self.process:
            self.process.stdin.write((command + '\n').encode())
            self.process.stdin.flush()
            return self.process.stdout.readline().decode()
        else:
            raise Exception('GDB session not started.')

    def terminate_session(self):
        """Terminates the GDB session."""
        if self.process:
            self.process.terminate()
        else:
            raise Exception('GDB session not started.')
