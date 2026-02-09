import argparse

parser = argparse.ArgumentParser(
    prog='scratchpole',
    description='A tool for extracting data from Prusa Slicer gcode.',
)

# The file to slice

parser.add_argument('file',
                    help='The file to extract data from.',
                    required=True,
                    metavar='FILE',
                    type=str
                    )

# Debugging
parser.add_argument('--debug',
                    help='Display debugging information.',
                    action='store_true',
                    )

# Name of the gcode output file
parser.add_argument('--gcode-output',
                    metavar='FILE',
                    type=str,
                    default='scratched-pole.gcode'
                    )

# Do not delete the gcode file
parser.add_argument('--dont-delete-gcode',
                    action='store_true',
                    )

# Prusa Slicer settings to load
parser.add_argument('-s', '--settings',
                    help='The settings file(s) to load',
                    metavar='FILE',
                    type=str,
                    nargs='*',
                    required=True
                    )

args = parser.parse_args()
