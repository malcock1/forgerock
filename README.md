# Martin's Forgerock tech test

## About

This webserver application will return the last NDAYS closing stock results and an average of those results for a given stock SYMBOL upon receiving a HTTP GET request.

The application container image can be found on DockerHub [here](https://hub.docker.com/r/malcock/webserver)

## How to deploy

### Ansible deployment

1. Ensure Python is installed on the deployment machine, details of installing Python can be found [here](https://www.python.org/downloads/)

2. Ensure Pip is installed on the deployment machine, details of how to install for you Operating system can be found [here](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers)

2. Ensure Ansible is installed on the deployment machine. You can following the installation instructions for your Operating system [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

3. Ensure the following Python dependencies are met by running the following command:

  `# pip install openshift PyYAML`
  
4. Clone this repository

  `# git clone https://github.com/malcock1/forgerock.git`
  
5. From within the cloned repository dirctory, deploy the application using the following Ansible-playbook command, please note the APIKEY is encrypt and therefore the playbook will ask for a 'Vault Password':

  `# ansible-playbook webserver-deployment-playbook.yml --ask-vault-pass`
  
#### Customizing Ansible deployment

You can change the way the application is deployed and configured by changing the variables in the Ansible playbook (webserver-deployment-playbook.yml)

Example of these variables are:

    deployment_state: present
    namespace: techtest
    symbol: "MSFT"
    ndays: 7
    apikey: _Ansible vault encrypted value_
  
### Kubectl deployment

If an Ansible deployment is not appropriate or possible, a Kubernetes manifests is also included and can be deployed using the following command. **Please note that you'll need to replace APIKEY value with your own key. please search for the string _!! Removed !!_ to find the location.**

`# kubectl create -f webserver-deployment.yml`
