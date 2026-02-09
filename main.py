import argparse
import subprocess

def main():
    command = ['prusa-slicer']

    parser = argparse.ArgumentParser(
        prog='scratchpole',
        description='Helps you scratch my pole',
        epilog='Happy slicing.',
    )

    parser.add_argument('file', metavar='FILE', type=str)
    parser.add_argument('--settings', metavar='FILE', type=str, nargs='*', required=True)

    args = parser.parse_args()

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append(args.file)

    print(command)

    subprocess.run(command)


if __name__ == '__main__':
    main()