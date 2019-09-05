# Martin's Forgerock tech test

## About

This webserver application will return the last NDAYS closing stock results and an average of those results for a given stock SYMBOL upon receiving a HTTP GET request.

## How to deploy

1. Ensure Ansible is installed on the deployment machine. You can following the installation instructions for your Operating system [here](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
2. Ensure the following Python dependencies are met by running the following command:
  `# pip install openshift PyYAML`
3. Clone this repository
  `# git clone https://github.com/malcock1/forgerock.git`
4. From within the cloned repository dirctory, deploy the application using the following Ansible-playbook command, please note the APIKEY is encrypt and therefore the playbook will ask for a 'Vault Password':
  `# ansible-playbook webserver-deployment-playbook.yml --ask-vault-pass`
