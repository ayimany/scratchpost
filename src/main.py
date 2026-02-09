import subprocess
import data_interests
from arguments import args

def main():
    command = ['prusa-slicer']

    for setting in args.settings:
        command.append('--load')
        command.append(setting)

    command.append('-g')
    command.append('-s')
    command.append('--output')
    command.append(args.output)
    command.append(args.file)

    # Run the PS command
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Parse the thang
    with open(args.output) as f:
        data = f.read()
        for interest in data_interests.Interest:
            value = data_interests.find_interest(interest, data)
            if value:
                print(f"{interest.info.label}: {value}")





if __name__ == '__main__':
    main()