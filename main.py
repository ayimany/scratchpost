import argparse
import re
import subprocess

def main():
    command = ['prusa-slicer']

    parser = argparse.ArgumentParser(
        prog='scratchpole',
        description='Helps you scratch my pole',
        epilog='Happy slicing.',
    )

    parser.add_argument('file', metavar='FILE', type=str)
    parser.add_argument('-o', '--output', metavar='FILE', type=str, default='scratched-pole.gcode')
    parser.add_argument('--settings', metavar='FILE', type=str, nargs='*', required=True)

    args = parser.parse_args()

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(args.output)
    command.append(args.file)

    print(command)

    # Run the PS command
    subprocess.run(command)

    # Parse the thang
    with open(args.output) as f:
        interest_1 = '; filament used \[mm] = (.*)'
        interest_2 = '; filament used \[cm3] = (.*)'
        interest_3 = '; filament used \[g] = (.*)'
        interest_4 = '; filament cost = (.*)'
        interest_5 = '; total filament used \[g] = (.*)'
        interest_6 = '; total filament cost = (.*)'
        interest_7 = '; total filament used for wipe tower \[g] = (.*)'
        interest_8 = '; estimated printing time \(normal mode\) = (.*)'
        interest_9 = '; estimated printing time \(silent mode\) = (.*)'
        interest_10 = '; estimated first layer printing time \(normal mode\) = (.*)'
        interest_11 = '; estimated first layer printing time \(silent mode\) = (.*)'
        data = f.read()
        cc = re.search(interest_8, data)
        print(cc.group(1))





if __name__ == '__main__':
    main()