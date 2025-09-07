import os


class path:
    def __init__(self,directory_path):
        self.all_paths = []
        for root, dirs, files in os.walk(directory_path):
            for name in files:
                self.all_paths.append(os.path.join(root, name))
            for name in dirs:
                self.all_paths.append(os.path.join(root, name))
    def get_list(self):
        return self.all_paths
