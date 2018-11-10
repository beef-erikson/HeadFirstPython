import sys
import os
import datetime
import time
import html

print(sys.platform)
print(sys.version)

print(os.getenv('HOME'))

print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.isoformat(datetime.date.today()))

print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))

print(html.escape("This HTML fragment contains a <script>script</string> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))
