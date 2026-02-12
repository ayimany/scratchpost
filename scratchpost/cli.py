import os
from .arguments import parse_args
from .data_interests import extract_interests
from .export import export_file
from .prusa import build_command, run_command, clean_gcode
from .logfmt import logger


def main():
    arguments = parse_args()
    has_non_existent_files = False

    if not os.path.exists(arguments.file):
        logger.error(f"File {arguments.file} does not exist")
        has_non_existent_files = True

    for path in arguments.settings:
        if not os.path.exists(path):
            logger.error(f"File {path} does not exist")
            has_non_existent_files = True

    if has_non_existent_files:
        exit(1)

    command = build_command(arguments)
    run_command(command, arguments.debug)
    data = clean_gcode(arguments.gcode_output)

    extracted = extract_interests(data, arguments.interests, arguments.time_format)

    if arguments.export is not None:
        export_file(extracted, arguments.export)

    if not arguments.silent:
        if arguments.pretty_print:
            for interest in extracted:
                print(f"{interest.label}: {interest.value}")
        else:
            for interest in extracted:
                print(f"{interest.key}: {interest.value}")

    # Cleanup
    if not arguments.dont_delete_gcode:
        os.remove(arguments.gcode_output)


if __name__ == '__main__':
    main()
