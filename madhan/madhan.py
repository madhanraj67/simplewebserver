from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>Top software companies with revenue table</title>
<body >	
<h1 align="center">Top five revenue generating software companies</h1>

<center>
<table border ="3"cellspacing="3" cellpadding="6" height="30" width="70" >
<tr>
<th>sno</th>
<th> name</th>
<th>register number </th>
<th>cgpa</th>
</tr>

<tr>
<th>1</th>
<td>Madhan </td>
<td>100 </td>
<td>10.0 </td>
</tr>

<tr>
<th>2</th>
<td>karthi </td>
<td >200 </td>
<td>10.0 </td>
</tr>

<tr>
<th>3</th>
<td>samantha </td>
<td>300</td><td>10.0 </td>
</tr>

<tr>
<th>4</th>
<td>vijay</td>
<td>400 </td><td>10.0 </td>
</tr>

<tr>
<th>5</th>
<td>ajith</td>
<td>500 </td><td>10.0 </td>
</tr>

</table>
</center>
</body>
</head>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
