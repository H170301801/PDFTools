import webbrowser
NEXT_HTML = "Sillyuan_1.html"
f = open(NEXT_HTML,'w')
message = """
<html>
<head></head>
<body>
<p>NEXT</p>
<p>Nuck Fortheastern University</p>
</body>
</html>"""
f.write(message)
f.close()
webbrowser.open(NEXT_HTML,new = 1)
