import http.client

conn = http.client.HTTPConnection("127.0.0.1:8000")

payload = '{\n\t"username": "Jhon Doe",\n\t"password": "pass1"\n}'

headers = {"Content-Type": "application/json", "User-Agent": "insomnia/8.5.1"}

conn.request("POST", "/api/v1/auth/login/", payload, headers)

res = conn.getresponse()

if res.status not in [200, 201, 400, 401, 404, 423]:
    print(res.status, res.reason, "Failed")
    print(res.res.read().decode("utf-8"))
    exit(code=res.status)

print(res.status, res.reason, "Success")
