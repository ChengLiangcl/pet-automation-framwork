import os


def create_init_files(base_path):
    for root, dirs, files in os.walk(base_path):
        # Check if __init__.py already exists
        if '__init__.py' not in files:
            init_path = os.path.join(root, '__init__.py')
            with open(init_path, 'w') as f:
                # You can optionally add some content here, but it's not necessary
                f.write('# This file makes the directory a package\n')
            print(f'Created {init_path}')


if __name__ == "__main__":
    base_path = os.path.abspath('')  # Change this to the path of your project
    create_init_files(base_path)
