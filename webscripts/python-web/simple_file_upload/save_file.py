#!/usr/bin/env python
#Original Code http://webpython.codepoint.net/cgi_big_file_upload
#Modified by aboccia to test uploaded file types by MIME
#This script can be changed to check for any desired MIME types for uploaded files

import cgi, os
import cgitb; cgitb.enable()
import mimetypes

form = cgi.FieldStorage()

# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
   while True:
      chunk = f.read(chunk_size)
      if not chunk: break
      yield chunk
      
# A nested FieldStorage instance holds the file
fileitem = form['file']

# Test if the file was uploaded
if fileitem.filename:
	#Define archive MIME types we would like to test for
   mime_type_list = ['application/x-tar','application/zip','multipart/x-zip','multipart/x-gzip','application/x-gzip','application/x-gtar']
   mime = mimetypes.guess_type(fileitem.filename)
   #Check the uploaded file against the allowed mime types, if it matches any than accept the upload
   for mtype in mime_type_list:
	if mime[0] == mtype:
   # strip leading path from file name to avoid directory traversal attacks
   # ../archives/ is one level up from the script which is where we want files saved
		fn = os.path.basename(fileitem.filename)
		f = open('../archives/' + fn, 'wb', 10000)

# Read the file in chunks
		for chunk in fbuffer(fileitem.file):
			f.write(chunk)
		f.close()
		message = 'Your archive "' + fn + '" was uploaded successfully.'
		break

	else:
		message = 'No file was uploaded, are you sure you attempted to upload a valid source archive?'

print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
<p></p>
<p><a href="http://example.org/uploads">Click Here</a> to upload more files</p>
<p><a href="http://example.org/uploads/cgi-bin/archive_listing.py">Click Here</a> to view a listing of uploaded files</p>
</body></html>
""" % (message,)
