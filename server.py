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
        albums = db.select('Album', limit=10)
        artists = db.select('Artist', limit=10)
        genres = db.select('Genre', limit=10)
        result = '<html><head><title>ListAlbum</title></head><body>'
        result += '<table border="1">'
        result += '<tr><th>Artist</th><th>Album</th><th>Genre</th></tr>'
        for artist in artists:
            result += '<tr>'
            result += '<td>' + artist.Name + '</td>'
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()