def make_album(artist_name, album_title, songs = None):
    info = {'artist':artist_name, 'album':album_title}
    if songs:
        info['song']=songs
    return info
while True:
    print("Please enter info:")
    print("You can use 'q' anytime to quit")
    artist = input("Enter artist's name:")
    if artist == 'q':
        break
    album = input("Enter album's name:")
    if album == 'q':
        break
    case_1 = make_album( artist, album)
    print(case_1)