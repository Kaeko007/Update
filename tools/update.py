import requests
import subprocess
import sys
from time import sleep


class Update():
    def __init__(self):
        self.version = '1.1.0'
        self.github = 'https://github.com/Kaeko007/Update/blob/main/tools/update.py'
        self.zipfile = 'https://github.com/Kaeko007/Update/archive/refs/heads/main.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.1.0'" in code:
            print('This version is up to date!')
            sleep(1)
            sys.exit(0)
        else:
            print('''
                    ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                    ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                    ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                    ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                                      Your version of Luna Token Grabber is outdated!''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                print('Downloading Update...')
                new_version_source = requests.get(self.zipfile)
                with open("Update.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)

                subprocess.Popen([sys.executable, 'updater.py'])

                sys.exit(2)
            if choice.lower() == 'n':
                sys.exit(0)


if __name__ == '__main__':
    Update()
