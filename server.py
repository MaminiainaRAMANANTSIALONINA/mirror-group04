import web
web.config.debug = False

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        db = web.database(
            dbn='mysql',
            host='tmp-insi.rktmb.org',
            port=3306,
            user='insigroup00',
            pw='insigroup00',
            db='project00',
        )
        a2=db.select('Album', limit=10)
        artists=db.select('Artist', limit=10)
        result = '<html><head><title>test</title></head>'
        result += '<body><table border=2>'
        result +='<tr> <th> Album </th> <th> Artist </th></tr>'
        for a in a2:
            result +='<tr> <td>'+ a.Title + ',</br>'
            result+='  </tr></td>'
        result += '</table></body>'
        result += '</html>'
        return result
         #for a in artists:
            
           

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
