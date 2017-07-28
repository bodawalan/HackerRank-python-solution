ROOT = "/"
DIV = "/"
PREV = ".."


class Path:
    def __init__(self, path):
        self.dirs = []
        self.cd(path)

    @property
    def current_path(self):
        return str(self)

    def cd(self, path):
        if path.startswith(ROOT):
            # absolute path - start from the beginning
            self.dirs = []
            path = path[len(ROOT):]

        # follow relative path
        for dir in path.split(DIV):
            if dir == PREV:
                self.dirs.pop()
            else:
                self.dirs.append(dir)

    def __str__(self):
        return ROOT + DIV.join(self.dirs)


path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)
