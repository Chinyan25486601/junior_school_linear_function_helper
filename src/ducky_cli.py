import _thread
from enum import Enum

class COMMAND_PROCESSING_MODE(Enum):
    DEFAULT = 0
    CUSTOMIZE = 1

class ducky_cli(object):
    def __init__(self, get_command=None, prompt=">", welcome_message="Welcome to ducky_cli", default_exit_command=True):
        super().__init__()

        # 初始化各项属性
        self.prompt = prompt
        self.welcome_message = welcome_message
        self.command_table = dict()
        self.supported_commands = list()
        self.should_exit = False

        # 添加命令处理程序
        if get_command:
            self.get_command = get_command
        else:
            self.get_command = self.process_command

        if default_exit_command:
            def stop_process(sender,command):
                self.stop()
            self.add_command_rule("stop", stop_process)
            self.add_command_rule("exit", stop_process)

    def mainloop(self):
        print(self.welcome_message)
        def loop_thread():
            try:
                while True:
                    if self.should_exit:
                        _thread.exit()
                    command = input(self.prompt)
                    self.get_command(self, command)
            except EOFError:
                pass
        self._t = _thread.start_new_thread(loop_thread, ())
        while True:
            if self.should_exit:
                break
    
    def stop(self):
        print("stoping...")
        self.should_exit = True

    def output(self, message: str):
        print(message)

    def process_command(self, sender, raw_command: str):
        raw_command_cutted = raw_command.split(" ")
        if raw_command_cutted[0] in self.supported_commands:
            self.command_table[raw_command_cutted[0]](self, raw_command_cutted)
        else:
            pass

    def set_command_processing_mode(self, mode, get_command=None):
        if mode==COMMAND_PROCESSING_MODE.DEFAULT:
            self.get_command = self.process_command
        elif mode==COMMAND_PROCESSING_MODE.CUSTOMIZE:
            if get_command:
                self.get_command = get_command
        else:
            raise ValueError

    def add_command_rule(self, command, callback):
        self.command_table[command]=callback
        self.supported_commands.append(command)

    def add_command_rules(self, command_rules):
        for rule in command_rules:
            self.command_table[rule[0]]=rule[1]
            self.supported_commands.append(rule[0])

if __name__=="__main__":
    def test_get_command(sender: ducky_cli, command: str):
        sender.output(command)
    cli = ducky_cli()
    cli.add_command_rule("test",test_get_command)
    cli.mainloop()