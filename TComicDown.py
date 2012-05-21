#!/usr/bin/python2.7

#########################################
# Simple Comic Strip Downloading Script #
# Tanmay Chaudhry                       #
#########################################

import bs4
import urllib2
import sys
import os

def download_comic(site, index_start, index_end):
    """
        Dispatch to the specific comic downloader, based on the site
    """
    if site=="http://xkcd.com" or site=='xkcd':
        download_xkcd(site, index_start, index_end)
        
def download_xkcd(site, index_start, index_end):
    """
        Download the XKCD Comic
        Filename index_xkcd_Title
        Saved in ./XKCD/index_xkcd_Title
    """
    dir_exists = os.path.isdir('XKCD')
    if dir_exists:
        pass
    else:
        os.mkdir('XKCD')
    
    selection = range(index_start, index_end+1)
    selection.reverse()
        
    for index in selection:
        try:
            connection = urllib2.urlopen('http://xkcd.com/' + str(index))
            print "Connected To" + connection.geturl()
            html_soup = bs4.BeautifulSoup(connection.read())
            connection.close()
        except Exception:
            print Exception
            
        #Get Title, also used as Filename
        title = html_soup.find(id="ctitle").contents
        title = title[0]
        
        #Skip if file already exists
        filename = "XKCD/"+str(index)+"_xkcd_"+title
        if os.path.isfile(filename):
            print filename + " Exists Skipping.."
            continue
    
        #Get Actual Image
        img = html_soup.find(id="comic")
        img = img.img
        img_url = img.__getitem__('src')
        try:
            img_download = urllib2.urlopen(img_url)
        except Exception:
            print "Failed To Connect to image.."
            print Exception
    
        #Write to File
        try:
            comic = open(filename, 'wb')
            comic.write(img_download.read())
            comic.close()
            print "Downloaded " + filename
        except Exception:
            print "Error Writing To File.."
            print Exception
        

if __name__=="__main__":
    site = sys.argv[1]
    index_start = int(sys.argv[2])
    index_end = int(sys.argv[3])      
    
    download_comic(site, index_start, index_end)
    
    