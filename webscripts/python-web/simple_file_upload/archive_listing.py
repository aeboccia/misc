#!/usr/bin/env python
#Author Anthony Boccia <anthony@boccia.me>
#This python web cgi script can be used to list the contents of a directory in your web root, each file will be listed as a hyperlink
import os
import cgi
import cgitb; cgitb.enable()
basepath = '../archives'
count = 0
#The following for loop will get a listing of everything under ../
for files in os.listdir(basepath):
	#The following join and isdir filter out folders and anything with .html from the listing
	path = os.path.join(basepath, files)

	if not os.path.isdir(path) and not files.endswith(".html") and count <= 0:
		print "Content-Type: text/html\n\n"
		print "<h1>Listing of Uploaded Archives</h1>"
	        print "<html><body><p><a href=""http://example.org/uploads/archives/%s"">%s</p></body></html>" %(files,files)
	else:
		print "<html><body><p><a href=""http://example.org/uploads/archives/%s"">%s</p></body></html>" %(files,files)
	count = count + 1

print "<html><body><a href=""http://example.org/uploads""> Click Here</a> to return to the uploads page</body></html>"
