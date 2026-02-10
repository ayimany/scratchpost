import subprocess


def build_command(args):
    command = ['prusa-slicer']

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(args.gcode_output)
    command.append(args.file)

    return command

def run_command(command, debug: bool):
    # Run the PS command
    stdout = None if debug else subprocess.DEVNULL
    stderr = None if debug else subprocess.DEVNULL
    subprocess.run(command, stdout=stdout, stderr=stderr)

def read_gcode(filename):
    with open(filename) as f:
        return f.read()

def clean_gcode(filename):
    with open(filename) as f:
        lines = list(filter(lambda l: l.startswith(';'), f.readlines()))
        data = "".join(lines)
        return data


