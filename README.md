# EX01 Developing a Simple Webserver
## Date:1:03:2024

## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
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



## OUTPUT:
![alt text](<Screenshot 2024-03-12 113234.png>) 
![alt text](<Screenshot 2024-03-12 113358.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
