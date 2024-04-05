import http.client

conn = http.client.HTTPConnection("127.0.0.1:8000")

payload = ""

headers = {"User-Agent": "insomnia/8.5.1"}

conn.request("GET", "/", payload, headers)

res = conn.getresponse()

if res.read().decode("utf-8") == """{"message":"Hello VTS!"}""":
    print(res.status, res.reason, "Success")

else:
    print(res.status, res.reason, "Failed")
    print(res.res.read().decode("utf-8"))
    exit(code=res.status)
