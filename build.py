#
# Author mfw78@chasingseed.com
#

import os
from jinja2 import Environment, FileSystemLoader
from eth_account import Account
from datetime import datetime
import time
import json


# Number of bees at the queen's service should she choose.
num_nodes = 3

# Every bee has it's day
versions = {
    'clef': '0.4.12',
    'bee': '0.6.2',
    'geth': 'v1.10.2'
}

# Where do we keep the sweet honey
paths = {
    'root': '/var/hive',
}

# The clef password - used to encrypt new ethereum accounts.
# WARNING: THIS MUST BE AT LEAST 10 CHARACTERS LONG.
#          REFER TO https://geth.ethereum.org/docs/getting-started
clef = {
    'password': 'passwordhere'
}

# Network port settings - let's make it easier to share pollen!
network = {
    'base_host_port': 1633,
    'base_external_port': 31000,
    'host_ip_addr': "192.168.1.100",
    'external_ip_addr': "199.199.199.199",
    'grafana_port': 3000,
    'geth_http_port': 8545,
    'geth_ws_port': 8546,
}


# First let's go through and generate all the Ethereum accounts for the
# nodes.
Account.enable_unaudited_hdwallet_features()
accounts = [ Account.create() for x in range(num_nodes) ]

# Encrypt all the node's private keys and store them into clef.
# This is why clef's password is required.
for account in accounts:
    encrypted = account.encrypt(clef['password'])

    now = datetime.utcnow()
    pretty_address = account.address[2:].lower()

    file_name = "UTC--{}--{}".format(
        now.strftime("%Y-%m-%dT%H-%M-%S.%f"),
        pretty_address
    )

    # Let's save it in a file format hopefully usable by clef
    with open(file_name, 'w') as f:
         f.write(json.dumps(encrypted))

file_loader = FileSystemLoader('templates')
env = Environment(
    loader=file_loader, trim_blocks=True, lstrip_blocks=True
)

# Process a template file
def process(input, output):
    # Process the docker-compose.yaml
    template = env.get_template(input)

    rendered = template.render(
        num_nodes=num_nodes, paths=paths, clef=clef, network=network,
        versions=versions, accounts=accounts
    )

    with open(output, 'w') as f:
        f.write(rendered)

templates = [
    ('docker.txt', 'docker-compose.yaml'),
    ('env.txt', '.env'),
    ('password.txt', 'password'),
    ('clef.txt', 'clef.sh'),
    ('deploy.txt', 'deploy.sh'),
    ('prometheus.txt', 'prometheus/prometheus.yml'),
    ('tearsheet.txt', 'tearsheet.txt'),
    ('monBee.txt', 'monBee.sh')
]

# Process the templates
for t in templates:
    process(*t)

os.chmod("deploy.sh", 0o755)
