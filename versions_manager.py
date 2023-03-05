class VersionManager:
    def __init__(self, version=None):
        if version == "" or version is None:
            version = "0.0.1"
            self.version = version
        else:
            self.version = version

    def release(self):
        return self.version

    def major(self):
        values = [x for x in self.version]
        values[0] = str(int(values[0]) + 1)
        major_version = ''.join([str(elem) for elem in values])
        return major_version

    def minor(self):
        pass

    def patch(self):
        pass

    def rollback(self):
        pass


a = VersionManager("0.0.1")
print(a.major())
