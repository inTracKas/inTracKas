#!/usr/bin/python
import textwrap
 
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
 
 
class HelloRequestHandler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        response_text = textwrap.dedent('''\
            <html>
<!DOCTYPE html>
<html>

<head>
	<meta content="initial-scale=1, maximum-scale=1, user-scalable=0" name="viewport" />
	<meta name="viewport" content="width=device-width" />

	<!--Datatable plugin CSS file -->
	<link rel="stylesheet" href= "https://cdn.datatables.net/1.10.22/css/jquery.dataTables.min.css" />

	<!--jQuery library file -->
	<script type="text/javascript" src=	"https://code.jquery.com/jquery-3.5.1.js">
	</script>

	<!--Datatable plugin JS library file -->
	<script type="text/javascript" src= "https://cdn.datatables.net/1.10.22/js/jquery.dataTables.min.js">
	</script>
</head>

<body>
	<h2>AWS Ip ranges</h2>

	<!--HTML table with student data-->
<table id="example" class="display" style="width:100%">
        <thead>
            <tr>
                <th>Ip prefixe</th>
                <th>Region</th>
                <th>Service</th>
                <th>Network border group</th>

            </tr>
        </thead>
        <tfoot>
            <tr>
                <th>Ip prefixe</th>
                <th>Region</th>
                <th>Service</th>
                <th>Network border group</th>

            </tr>
        </tfoot>
    </table>

	<script>
	
$(document).ready(function() {
    $('#example').DataTable( {

        	 "ajax":     {
                method: 'GET',
                url: 'https://ip-ranges.amazonaws.com/ip-ranges.json',
                dataSrc: 'prefixes'
     },
        "columns": [
            { "data": "ip_prefix" },
            { "data": "region" },
            { "data": "service" },
            { "data": "network_border_group" }
        ]
    } );
    
     $('.dataTables_length').addClass('bs-select');
} );


	</script>
</body>

</html>







            </html>
        ''')
        self.wfile.write(response_text.encode('utf-8'))
 
 
server_address = ('', 9090)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()
