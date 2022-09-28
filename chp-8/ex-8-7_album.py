def make_album(artist_name, album_title, songs=None):
    """Shows artist's name, album title and number of songa with a default value of none"""
    info = {'artist':artist_name, 'album':album_title}
    if songs:
        info['song']=songs
    return info
arrdee = make_album('Arrdee', 'Peer pressure')
print(arrdee)
justin = make_album('Justin Bieber', 'Intentions','234')
print(justin)
ed = make_album('Ed Sheeran', 'Shivers')
print(ed)