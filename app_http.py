import requests

# Connectivity Service Service Key
connectivity_service_key = {
    "clientid": "sb-sampleclientid!b3008|connectivity!b137",
    "clientsecret": "****-****-****-****",
    "url": "https://tenant_name.authentication.sap.hana.ondemand.com",
    "identityzone": "sample-zone",
    "tenantid": "xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "tenantmode": "dedicated",
    "verificationkey": "-----BEGIN PUBLIC KEY-----\nXXXXXX...\n-----END PUBLIC KEY-----",
    "xsappname": "sampleappname!b3008|connectivity!b137",
    "uaadomain": "authentication.sap.hana.ondemand.com",
    "credential-type": "binding-secret",
    "onpremise_proxy_host": "connectivityproxy.internal.cf.sap.hana.ondemand.com",
    "onpremise_proxy_http_port": "20003",
    "onpremise_proxy_ldap_port": "20001",
    "onpremise_proxy_port": "20003",
    "onpremise_proxy_rfc_port": "20001",
    "onpremise_socks5_proxy_port": "20004",
    "token_service_domain": "authentication.sap.hana.ondemand.com",
    "token_service_url": "https://tenant_name.authentication.sap.hana.ondemand.com"
}


# Target Application Details (replace with your app information)
application_host = "virtualhost"
application_port = 3333
application_path = "/hello"
location_id = "FELIXLAPTOP"  # Adjust to match your Cloud Connector location

def get_connectivity_service_token(client_id, client_secret, token_service_url):
    """
    Fetches an OAuth token from the SAP Connectivity Service.
    """
    response = requests.post(
        url=token_service_url,
        params={"grant_type": "client_credentials"},
        auth=(client_id, client_secret)
    )

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        exit(-1)

    return response.json().get("access_token")


def example_http_request(host, port, path, auth_token, location_id, proxy_host):
    """
    Performs an HTTP GET request through SAP Cloud Connector.
    """
    url = f"http://{host}:{port}{path}"
    headers = {
        "Proxy-Authorization": f"Bearer {auth_token}",
        "SAP-Connectivity-SCC-Location_ID": location_id
    }
    proxies = {"http": proxy_host}

    response = requests.get(url, headers=headers, proxies=proxies, verify=False, timeout=10)
    return response


# Fetch OAuth Token
print("Fetching OAuth token...")
token = get_connectivity_service_token(
    connectivity_service_key["clientid"],
    connectivity_service_key["clientsecret"],
    connectivity_service_key["token_service_url"] + "/oauth/token"
)
print("Token acquired successfully.")

# Build proxy URL
proxy_host = "http://" + connectivity_service_key["onpremise_proxy_host"] + ":" + connectivity_service_key["onpremise_proxy_port"]

# Perform HTTP Request
try:
    print("Sending HTTP request through SAP Cloud Connector...")
    response = example_http_request(application_host, application_port, application_path, token, location_id, proxy_host)
    print("Response received:")
    print(response.content.decode("utf-8"))
except Exception as e:
    print(f"An error occurred: {e}")

print("Script execution completed.")