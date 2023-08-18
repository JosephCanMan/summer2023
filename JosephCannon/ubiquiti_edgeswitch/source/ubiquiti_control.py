from paramiko import SSHClient, AutoAddPolicy
from rich import print, pretty, inspect
pretty.install()

client = SSHClient()
#LOAD HOST KEYS
client.load_system_host_keys()

#Known_host policy
client.set_missing_host_key_policy(AutoAddPolicy())


#client.connect('host', username='username', password='password')
client.connect('10.31.81.2', username='ubnt', password='', look_for_keys=False,
               allow_agent=False)


# Run a command (execute PHP interpreter)
#client.exec_command('hostname')
stdin, stdout, stderr = client.exec_command('10.31.81.2')
print(type(stdin))
print(type(stdout))
print(type(stderr))

# Optionally, send data via STDIN, and shutdown when done
stdin.write('show port-channel brief\n')
# poe opmode shutdown
# poe opmode auto
stdin.channel.shutdown_write()

# # Print output of command. Will wait for command to finish.
# print(f'STDOUT: {stdout.read().decode("utf8")}')
# print(f'STDERR: {stderr.read().decode("utf8")}')

string = stdout.read().decode("utf8")

command = 'show port-channel brief\n'
idx = command.rfind('\n', 0, command.rfind('\n'))  # remove everything before the second to last '\n'

if (idx != -1):  # only do this if '\n' is found in command
    command = command[idx + 1:]  # remove characters (left-to-right) until second to last '\n' is reached

idx_last = command.rfind('\n')  # remove the last '\n'
if (idx_last != -1):  # only do this if '\n' is found in command
    command = command[:idx_last]  # remove characters (right-to-left) until '\n' is reached

print(command)

# print(string[string.index("(UBNT EdgeSwitch) #" + str(command)) + len("(UBNT EdgeSwitch) #" + str(command)) + 2:])
# print(string[string.index("(UBNT EdgeSwitch) >" + str(command)) + len("(UBNT EdgeSwitch) >" + str(command)) + 2:])
# print(string[string.index("(UBNT EdgeSwitch) (Config)#" + str(command)) + len("(UBNT EdgeSwitch) (Config)#" + str(command)) + 2:])

# Get return code from command (0 is default for success)
print(f'Return code: {stdout.channel.recv_exit_status()}')

# Because they are file objects, they need to be closed
stdin.close()
stdout.close()
stderr.close()

# Close the client itself
client.close()
