from calendar import c
from tenacity import retry_unless_exception_type
from constants import *

class Parser():
    def __init__(self, filepath):
        self.current_command = None
        self.f_vm = open(filepath)

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.f_vm.close()

    def advance(self):
        while True:
            line = self.f_vm.read_line()
            if not line:
                self.current_command = None
                return self.current_command

            line = line.rstrip().lstrip()

            comment_i = line.find("//")
            if comment_i != -1:
                line = line[:comment_i]

            if line != "":
                self.current_command = line.split()
                return self.current_command

    def command_type(self):
        current_command = self.current_command[0]
        if current_command == "push":
            return C_PUSH
        elif current_command == "pop":
            return C_POP
        elif current_command == "label":
            return C_LABEL
        elif current_command == "goto":
            return C_GOTO
        elif current_command == "if-goto":
            return C_IF
        elif current_command == "function":
            return C_FUNCTION
        elif current_command == "return":
            return C_RETURN
        elif current_command == "call":
            return C_CALL
        elif current_command in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return C_ARITHMETIC

    def arg1(self):
        if self.current_command() == C_ARITHMETIC:
            return self.current_command[0]
        else:
            return self.current_command[0]

    def arg2(self):
        if self.command_type() in [C_PUSH, C_POP, C_FUNCTION, C_CALL]:
            return self.command_type[2]
