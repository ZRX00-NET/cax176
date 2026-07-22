from colorama import just_fix_windows_console

just_fix_windows_console()

from colorama import Fore, Back, Style

print(Fore.RED + 'BLUE')
print(Back.GREEN + 'BACKGROUND')
print(Style.RESET_ALL)
print('HELLO')
