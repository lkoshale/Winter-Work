
import searchengine
import nn

pagelist=['https://en.wikipedia.org/wiki/JavaScript']

mynet=nn.searchnet('nn.db')

wWorld,wRiver,wBank =101,102,103
uWorldBank,uRiver,uEarth =201,202,203
# mynet.generatehiddennode([wWorld,wBank],[uWorldBank,uRiver,uEarth])
for c in mynet.con.execute('select * from wordhidden'): print c
for c in mynet.con.execute('select * from hiddenurl'): print c

print '*************'
# mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
# print mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth])


print "**************"
allurls=[uWorldBank,uRiver,uEarth]
for i in range(30):
    mynet.trainquery([wWorld,wBank],allurls,uWorldBank)
    mynet.trainquery([wRiver,wBank],allurls,uRiver)
    mynet.trainquery([wWorld],allurls,uEarth)

print mynet.getresult([wBank],allurls)

#crawler.crawl(pagelist)
#
# crawler=searchengine.crawler('searchindex.db')
# crawler.calculatepagerank( )
# #crawler.createindextables( )
#
# cur=crawler.con.execute('select * from pagerank order by score desc')
# for i in range(3): print cur.next( )
#
#
#
# #crawler.crawl(pagelist)
# #print [row for row in crawler.con.execute('select rowid from wordlocation where wordid=1')]
#
# print " "
# e=searchengine.searcher('searchindex.db')
# print "***************"
# print e.query('computer science')
