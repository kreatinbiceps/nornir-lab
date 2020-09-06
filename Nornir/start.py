from nornir import InitNornir
nr = InitNornir("config.yml")

from nornir.core.inventory import ConnectionOptions
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.plugins.functions.text import print_result


def showcomm(command):
    result = nr.run(netmiko_send_command, command_string = command)
    return print_result(result)

def confcomm(command):
    result = nr.run(netmiko_send_config, config_commands = command)
    return print_result(result)


def filecomm(command):
    result = nr.run(netmiko_send_config, config_file = command)
    return print_result(result)



while True:
    choice = input("Press 1 for show commands. Press 2 for conf commands. Press 3 to load a file: ")
    if choice == "1":
        inputComm = input("Enter show command: ")
        showcomm(inputComm)

    elif choice == "2":
        inputConfComm = input("Enter conf command: ")
        confcomm(inputConfComm)

    elif choice == "3":
        inputFileComm = input("Enter file name: ")
        filecomm(inputFileComm)
