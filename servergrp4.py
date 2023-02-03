import web

web.config.debug = False

urls = (
    '/', 'Index'
)

class Index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00'
        )
        albums = db.select('Album', limit=15)
        artists = db.select('Artist', limit=15)
        genres = db.select('Genre', limit=15)
        result = '<html><head><title>ListAlbum</title></head><body>'
        result += '<table border="1">'
        result += '<tr><th>Id_artists</th><th>Artist</th><th>Genre</th><th>Album</th></tr>'
        for artist in artists:
            result += '<tr>'
            result += '<td>'+str(artist.AtristId)+'</td>'
            result += '<td>' + artist.Name + '</td>'
            for album in albums:
                result += '<td>' + album.Title + '</td>'
                break
            for genre in genres:
                result += '<td>' +  genre.Name + '</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()