import os
def print_directory_contents(root_dir, indent=0):
    indent_str = '.   ' * indent
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"{indent_str}[{os.path.basename(dirpath)}]")
        for filename in filenames:
            print(f".   {indent_str}{filename}")
        if dirnames:
            for dirname in dirnames:
                print_directory_contents(os.path.join(dirpath, dirname), indent + 1)
root_directory = os.path.dirname(os.path.abspath(__file__))
print_directory_contents(root_directory)
