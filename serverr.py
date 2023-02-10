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
        genres = db.select('Genre', limit = 10)
        
        result = '<html><head><title>test</title></head><body>'
        result = '<div><a href="#">Lien1<a><a href="#">Lien2<a><a href="#">Lien3<a><a href="#">Lien4<a></div>'
        result += '<table border="1">'
        result += '<tr><th>Id_artist</th><th>Artist</th><th>Genre</th><th>Album</th></tr>'
        for artist in artists:
            result += '<tr>'
            result += '<td>' + artist.Name + '</td>'
            for genre in genres:
                result += '<tr>'
                result += '<td>' + genre.Name + '</td>'
            for album in albums:
                result += '<td>' + album.Title + '</td>'
                break
            result += '</tr>'
        result += '</table>'
        result += '</body></html>'
        return result
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()