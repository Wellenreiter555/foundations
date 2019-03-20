#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()

v_name = form.getvalue("name")

print("""
<html>
<body>
<p>
Thanks, %s
</p>
</body>
</html>
""" % v_name)
