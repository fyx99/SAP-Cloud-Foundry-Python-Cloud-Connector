# SAP Cloud Foundry Python Cloud Connector

This respository provides a few examples on how to use the SAP Cloud Connector to connect to on-premises systems from SAP Cloud Foundry.

## Content:

This repository contains two Python scripts demonstrating how to use the Connectivity Service as a proxy in a Python environment to send requests to an on-premises backend via the Cloud Connector.

*Commands:*

### Establish connectivity to the Connectivity Service proxy host for local testing:

cf ssh -L 8888:connectivityproxy.internal.cf.sap.hana.ondemand.com:20003 myapp

### Deploy Task Example:

cf push cloud_connector_test_task --task

cf run-task cloud_connector_test_task --command "python tcp_app.py" --name example_task
cf logs cloud_connector_test_task --recent
