import requests
import json

def upload_report(report_json):
    #Mock API for an example
    endpoint = "https://security-platform.local/api/upload"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(endpoint, data=json.dumps(report_json), headers=headers)
    return response.status_code, response.text

if __name__ == "__main__":
    dummy_report = {"scan": "snyk", "status": "vulnerabilities found", "count": 3}
    status, msg = upload_report(dummy_report)
    print(f"Upload status: {status}, message: {msg}")