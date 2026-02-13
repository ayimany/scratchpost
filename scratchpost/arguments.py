import argparse
import tempfile


def get_parser():
    parser = argparse.ArgumentParser(
        prog='scratchpost',
        description='A tool for extracting data from Prusa Slicer gcode.',
    )

    # The files to slice
    parser.add_argument('files',
                        help='The files to extract data from.',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        )

    # Prusa Slicer settings to load
    parser.add_argument('-s', '--settings',
                        help='The settings file(s) to load',
                        metavar='FILE',
                        type=str,
                        nargs='*',
                        required=True
                        )

    # Interests
    parser.add_argument('-i', '--interests',
                        help='The data interests to extract from the gcode.',
                        type=str,
                        nargs='*',
                        )

    # Debugging
    parser.add_argument('--debug',
                        help='Display debugging information.',
                        action='store_true',
                        )

    # Name of the gcode output file
    parser.add_argument('--gcode-output',
                        help='The path to the intermediate gcode file.',
                        metavar='FILE',
                        type=str,
                        default=tempfile.gettempdir() + '/scratched-pole.gcode',
                        )

    # Do not delete the gcode file
    parser.add_argument('--dont-delete-gcode',
                        help='Keep the intermediate gcode file after processing.',
                        action='store_true',
                        )

    parser.add_argument('--export',
                        help='The path to export the extracted data to.',
                        metavar='FILE',
                        type=str,
                        )

    parser.add_argument('--silent',
                        help='Suppress output to the console.',
                        action='store_true',
                        )

    parser.add_argument('--pretty-print',
                        help='Display data using descriptive labels.',
                        action='store_true',
                        )

    parser.add_argument('--time-format',
                        choices=['hours', 'minutes', 'seconds', 'full'],
                        default='full',
                        help='The format to display time-related keys in.',
                        )
    return parser


def parse_args():
    return get_parser().parse_args()
