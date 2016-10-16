import json
import socket

sock = socket.socket()
sock.bind(('', 9999))
sock.listen(1)

while True:
    conn, addr = sock.accept()

    print "connection opened: ", addr

    while True:
        try:
            js = json.loads(conn.recv(1024))

            if u"m1" == js[u"method"]:
                conn.send(json.dumps({
                    "method": "m1",
                    "result": 10
                }))
            elif u"m2" == js[u"method"]:
                conn.send(json.dumps({
                    "method": "m2",
                    "result": 3.1415
                }))
            elif u"m3" == js[u"method"]:
                conn.send(json.dumps({
                    "method": "m2",
                    "result": {
                        "r1": 42,
                        "r2": "Rrrr"
                    }
                }))
            elif u"m4" == js[u"method"]:
                conn.send(json.dumps({
                    "method": "m2",
                    "result": {
                        "r3": 10
                    }
                }))
            elif u"quit" == js[u"method"]:
                conn.close()
                print "connection closed: ", addr
                break

        except Exception as e:
            print e
            break
