import os
import subprocess

from .logfmt import logger


def build_command(args, input_file, gcode_output):
    command = ['prusa-slicer']

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(gcode_output)
    command.append(input_file)

    return command

def run_command(command, debug: bool):
    # Run the PS command
    res = subprocess.run(command, capture_output=True, text=True)

    if debug:
        if res.stdout:
            print(res.stdout)
        if res.stderr:
            print(res.stderr)

    if res.returncode != 0:
        error_msg = "The file contains polygons with more than 4 vertices"
        if error_msg in res.stdout or error_msg in res.stderr:
            exit(4)

        logger.warning(f"Prusa Slicer failed with exit code {res.returncode}. Use --debug to see the full output.")
        exit(res.returncode)

def read_gcode(filename):
    with open(filename) as f:
        return f.read()


def clean_gcode(filename):
    header_size = 4096  # 4KB for header comments
    footer_size = 65536 # 64KB for footer metadata

    with open(filename, 'rb') as f:
        f.seek(0, os.SEEK_END)
        file_size = f.tell()

        # Read header
        f.seek(0)
        header = f.read(min(file_size, header_size)).decode('utf-8', errors='ignore')

        # Read footer
        footer = ""
        if file_size > header_size:
            read_pos = max(header_size, file_size - footer_size)
            f.seek(read_pos)
            footer = f.read(file_size - read_pos).decode('utf-8', errors='ignore')

    lines = []
    for line in (header + footer).splitlines():
        if line.startswith(';'):
            lines.append(line)
    
    return "\n".join(lines)


