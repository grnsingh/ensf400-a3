import requests
import subprocess

minikube_ip = subprocess.getoutput('minikube ip').strip()
count = 0
for i in range(10000):
    response = requests.get(f"http://{minikube_ip}/")
    if response.status_code == 200:
        if response.text.startswith("Hello World from [app-1-deploym"):
            count+=1
    else:
        print(f"Test failed: Expected 200 response, but got {response.status_code}.")

print("TEST COMPLETED")
print("App1 was routed to " , count, "times out of 10000")