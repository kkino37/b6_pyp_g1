class Open(object):
    def __init__(self, file_path, access_mode='r'):
        self.file_path = file_path
        self.access_mode = access_mode

    def __enter__(self):
        self.file = open(self.file_path, self.access_mode)
        return (self.file, self.file_path)

    def __exit__(self, _type, value, traceback):
        print("Closing the file: (%s, %s, %s)" % (_type, value, traceback))
        self.file.close()
        return True


with Open('test.txt') as (fp, path):
    print("Reading from path: %s" % path)
    print(fp.read())

user_request = "djangocon-2015"
path = os.path.join(os.path.join(os.path.join('pyvideo-data'), 'data'), user_request)

p = Path("pyvideo-data")
path = p / 'data' / user_request