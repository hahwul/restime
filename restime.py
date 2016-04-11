import urllib
import datetime
import sys
import os
import time

varlen = len(sys.argv)
cnt = 0

if varlen <2:
    print "Usage : restime [URL] [URL] [URL] ..."
    print "--------------Menual---------------"
    print "URL    :  Single URL or URL List"
    print "          restime http://google.com"
    print "          restime http://google.com http://www.hahwul.com"
    print "By HaHwul"
else:
    while 1:
        #os.system('cls')
        ck=0
        urllist =[]
        for i in sys.argv:
            if ck!=0:
                if i[:5] != "http:":
                    sys.argv[ck] = "http://"+sys.argv[ck]
                urllist.append(sys.argv[ck])
            ck+=1
        nowtime = datetime.datetime.now()
        if cnt==0:
            print "Check the Response Time "+str(len(sys.argv)-1)+" Host...at "+str(nowtime)
            print "\n___________Report______________"
        for url in urllist:
            opener = urllib.FancyURLopener({})
            try:
                start = datetime.datetime.now()
                f = urllib.urlopen(url)
                end = datetime.datetime.now()
                diff = end - start
                rtime = float(float(diff.microseconds) / 100000)
            except IOError, e:
                print 'Connection Fail..\a', url
            else:
                header = str(f.info())
                if header.find("Server") == -1:
                    print "| ["+str(nowtime)+"] Response Time : "+str(rtime) + " sec -> " ,f.geturl() , "[no data]"
                else:
                    print "| ["+str(nowtime)+"] Response Time : "+str(rtime) + " sec -> " ,f.geturl() ,"  ["+str(f.info()['server'])+" Server]"
        cnt+=1
        time.sleep(4)
    if varlen >1:
        print "|_______________"










