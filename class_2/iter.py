class Photo(object):
    def __init__(self, path):
        self.path = path
    
    def __str__(self):
        return "Photo(%s)" % self.path


def read_photos_from_disk(year):
    return [
        '/home/santiago/photos/cats.jpg',
        '/home/santiago/photos/humans.jpg',
        '/home/santiago/photos/dogs.jpg',
    ]


class PhotoAlbum(object):
    def __init__(self, year):
        self.year = year
        self.index = 0
        self._photo_paths = read_photos_from_disk(self.year)

    def __iter__(self):
        return PhotoAlbum(year=self.year)

    def __next__(self):
        if len(self._photo_paths) > self.index:
            photo = Photo(self._photo_paths[self.index])
            self.index += 1
            return photo

        raise StopIteration()
    
    next = __next__


album = PhotoAlbum(year=2015)

for photo in album:
    print(photo)
    break

print("============")

for photo in album:
    print(photo)