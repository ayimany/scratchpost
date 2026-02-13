import os
from .arguments import parse_args
from .data_interests import extract_interests
from .export import export_file
from .prusa import build_command, run_command, clean_gcode
from .logfmt import logger


def main():
    arguments = parse_args()
    has_non_existent_files = False

    for path in arguments.files:
        if not os.path.exists(path):
            logger.error(f"File {path} does not exist")
            has_non_existent_files = True

    for path in arguments.settings:
        if not os.path.exists(path):
            logger.error(f"File {path} does not exist")
            has_non_existent_files = True

    if has_non_existent_files:
        exit(1)

    for i, input_file in enumerate(arguments.files):
        gcode_output = arguments.gcode_output
        if len(arguments.files) > 1:
            # If there are multiple files, we should probably have unique gcode outputs too
            # to avoid collisions if we were to run in parallel (though here it is sequential)
            # or just to be safe.
            base, ext = os.path.splitext(arguments.gcode_output)
            gcode_output = f"{base}_{i+1}{ext}"

        command = build_command(arguments, input_file, gcode_output)
        run_command(command, arguments.debug)
        data = clean_gcode(gcode_output)

        extracted = extract_interests(data, arguments.interests, arguments.time_format)

        if arguments.export is not None:
            export_path = arguments.export
            if len(arguments.files) > 1:
                base, ext = os.path.splitext(arguments.export)
                export_path = f"{base}_{i+1}{ext}"
            export_file(extracted, export_path)

        if not arguments.silent:
            if len(arguments.files) > 1:
                print(f"--- {input_file} ---")
            if arguments.pretty_print:
                for interest in extracted:
                    print(f"{interest.label}: {interest.value}")
            else:
                for interest in extracted:
                    print(f"{interest.key}: {interest.value}")

        # Cleanup
        if not arguments.dont_delete_gcode:
            if os.path.exists(gcode_output):
                os.remove(gcode_output)


if __name__ == '__main__':
    main()
