import requests

try:
    reply = requests.get('http://localhost:3000/cars')
except:
    print("Comms Err")
else:
    if reply.status_code == requests.codes.ok:
        print(reply.headers['Content-Type'])
        print(reply.json())
    else:
        print("Server error")
