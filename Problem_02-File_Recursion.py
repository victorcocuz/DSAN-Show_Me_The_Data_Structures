import os

# Create a recursive function to check through each folder and append the given suffix to a list of items
def find_files(suffix, path):
    file_list = []
    for item in os.listdir(path):
        file_path = os.path.join(path, item)
        if os.path.isdir(file_path):
            file_list.extend(find_files(suffix, file_path))
        if item.endswith('.c'):
            file_list.append(file_path)
    return file_list

# Print results of function, with suffix and path as input
for item in find_files('.c', os.path.join(os.path.abspath(os.getcwd()), 'testdir')):
    print(item)
