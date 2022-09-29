
from mitmproxy.net.http.http1.assemble import assemble_request, assemble_response

f = open('/root/mitm/output.txt', 'w')
f.close()

def response(flow):
    f = open('/root/mitm/output.txt', 'a')
    req = assemble_request(flow.request).decode('utf-8', 'replace').splitlines()
    if(req[0][0:3] == "GET"):
        f.write(req[0] + "\n" + req[1] + "\n")
        f.write(assemble_response(flow.response).decode('utf-8', 'replace').splitlines()[0] + "\n")
        #f.write("----------\n")
        f.close()
