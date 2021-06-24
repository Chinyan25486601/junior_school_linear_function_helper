from ducky_cli import *
from linear_function_calc import *
import re

def middle_ware(sender: ducky_cli, command, command_name):
    # TODO:添加对无理数的处理
    try:
        command = [(float(x)) for x in command[1:]]
    except ValueError:
        sender.error(ERROR_MESSAGE_MODE.PARAM_ERROR)
        return
    return command

def sl(sender: ducky_cli, command, command_name):
    if len(command)!=4:
        sender.error(ERROR_MESSAGE_MODE.PARAM_ERROR)
        return

    sender.output(get_length_of_segment_from_two_points(Point(command[0],command[1]),Point(command[2],command[3])))

def pf(sender: ducky_cli, command, command_name):
    if len(command)!=2:
        sender.error(ERROR_MESSAGE_MODE.PARAM_ERROR)
        return

    rk=str((get_analytic_expression_of_directly_proportional_function_from_one_point(Point(command[0],command[1]))).evalf(5))
    k=rk

    sender.output("k="+k)
    sender.output("y="+k+"x")
    pass

if __name__=="__main__":
    cli = ducky_cli(welcome_message="Welcome to function Helper!\nCopyright © 2021 Qinyan")
    cli.add_middle_ware(middle_ware)
    cli.add_command_rule("sl", sl)
    cli.add_command_rule("segmentl_length", sl)
    cli.add_command_rule("pf",pf)
    cli.add_command_rule("proportional_function",pf)
    cli.mainloop()