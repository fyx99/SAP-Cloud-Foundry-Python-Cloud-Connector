# SAP Cloud Foundry Python Cloud Connector

This repository contains example implementations demonstrating how to use the **SAP Cloud Connector** to connect to on-premises systems from **SAP Cloud Foundry**.

For detailed explanations and step-by-step guides, refer to the following blog posts:

- [SAP Cloud Foundry: Python and Cloud Connector (HTTP)](https://community.sap.com/t5/technology-blogs-by-sap/sap-cloud-foundry-python-and-cloud-connector-http/ba-p/13965916)  
- [SAP Cloud Foundry: Python and Cloud Connector (TCP)](https://community.sap.com/t5/technology-blogs-by-sap/sap-cloud-foundry-python-and-cloud-connector-tcp/ba-p/13967140)  
- [Hybrid Local Development with SAP Cloud Foundry: Access On-Premises APIs via Cloud Connector](https://community.sap.com/t5/technology-blogs-by-sap/hybrid-local-development-with-sap-cloud-foundry-access-on-premises-apis-via/ba-p/13967660)  


## Content:

This repository contains two Python scripts demonstrating how to use the Connectivity Service as a proxy in a Python environment to send requests to an on-premises backend via the Cloud Connector.

*Commands:*

### Establish connectivity to the Connectivity Service proxy host for local testing:

```bash
cf ssh -L 8888:connectivityproxy.internal.cf.sap.hana.ondemand.com:20003 myapp 
```

### Deploy Task Example:

```bash 
cf push cloud_connector_test_task --task```

cf run-task cloud_connector_test_task --command "python tcp_app.py" --name example_task
cf logs cloud_connector_test_task --recent
```
