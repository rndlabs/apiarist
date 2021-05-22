# Apiarist

Those that have been active in the [Ethereum Swarm](https://swarm.ethereum.org)
for a while have come to know the desire to scale their hives 🐝, in effect
working to perfect the ancient art of bee keeping - to become *the* apiarist.

## Motivations

If you want your hives to *hummmm*, they need to be well planned. *Apiarist* is designed with the following intentions:

1. Number of 🐝 nodes: >1
2. Swap endpoint: Running our *own* geth goerli endpoint, independent of 
   slock.it and infura. We choose syncmode *light* here, but you could
   change it in the template.
3. Metrics: A template setup for *prometheus*, *grafana*, and *alertmanager*.
4. Clef: Scalable use of *clef* with one instance per hive.

## Dependencies

Use of this repository requires the following dependencies:

* Python
* virtualenv
* Build essentials
* npm / node (required for [monBee](https://github.com/ldeffenb/monBee)
  integration)
* docker
* docker-compose

## Configuration

All configuration is handled in `build.py` in easily digestible variable
names:

```python
# Every bee has it's day
versions = {
    'clef': '0.4.12',
    'bee': '0.6.1',
    'geth': 'v1.10.2'
}

# Where do we keep the sweet honey. This best be an SSD with enough storage
# space for all and plenty of IOPs.
paths = {
    'root': '/var/hive',
}

# The clef password - used to encrypt new ethereum accounts. Make this a 
# good password!
clef = {
    'password': 'passwordhere'
}

# Network port settings - let's make it easier to share pollen!
network = {
    'base_host_port': 1633,
    'base_external_port': 31000,
    'host_ip_addr': "192.168.1.100",         # Docker host's IP address.
    'external_ip_addr': "199.199.199.199",   # External IP address.
    'grafana_port': 3000,
    'geth_http_port': 8545,
    'geth_ws_port': 8546,
}
```

## Deploying

OK, you've donned your bee suit and ready to step out into the Swarm...

Bring the deployment up by:

```bash
$ sudo ./up.sh
```

This will bring the swarm up and print out the tearsheet, showing useful
information. An example follows:

```raw
$ sudo ./up.sh
[sudo] password for user: 
created virtual environment CPython3.9.5.final.0-64 in 181ms
  creator CPython3Posix(dest=/home/user/src/bee-docker/.virtualenv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: Jinja2==3.0.1, MarkupSafe==2.0.1, bitarray==1.2.2, cytoolz==0.11.0, eth_abi==2.1.1, eth_account==0.5.4, eth_hash==0.3.1, eth_keyfile==0.5.1, eth_keys==0.3.3, eth_rlp==0.2.1, eth_typing==2.2.2, eth_utils==1.10.0, hexbytes==0.2.1, parsimonious==0.8.1, pip==21.1.1, pycryptodome==3.10.1, rlp==2.0.1, setuptools==56.0.0, six==1.16.0, toolz==0.11.1, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
Requirement already satisfied: eth_account in ./.virtualenv/lib/python3.9/site-packages (from -r requirements.txt (line 1)) (0.5.4)
Requirement already satisfied: Jinja2 in ./.virtualenv/lib/python3.9/site-packages (from -r requirements.txt (line 2)) (3.0.1)
Requirement already satisfied: eth-keyfile<0.6.0,>=0.5.0 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (0.5.1)
Requirement already satisfied: rlp<3,>=1.0.0 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (2.0.1)
Requirement already satisfied: eth-abi<3,>=2.0.0b7 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (2.1.1)
Requirement already satisfied: eth-rlp<2,>=0.1.2 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (0.2.1)
Requirement already satisfied: eth-keys!=0.3.2,<0.4.0,>=0.2.1 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (0.3.3)
Requirement already satisfied: eth-utils<2,>=1.3.0 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (1.10.0)
Requirement already satisfied: hexbytes<1,>=0.1.0 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (0.2.1)
Requirement already satisfied: bitarray<1.3.0,>=1.2.1 in ./.virtualenv/lib/python3.9/site-packages (from eth_account->-r requirements.txt (line 1)) (1.2.2)
Requirement already satisfied: parsimonious<0.9.0,>=0.8.0 in ./.virtualenv/lib/python3.9/site-packages (from eth-abi<3,>=2.0.0b7->eth_account->-r requirements.txt (line 1)) (0.8.1)
Requirement already satisfied: eth-typing<3.0.0,>=2.0.0 in ./.virtualenv/lib/python3.9/site-packages (from eth-abi<3,>=2.0.0b7->eth_account->-r requirements.txt (line 1)) (2.2.2)
Requirement already satisfied: cytoolz<1.0.0,>=0.9.0 in ./.virtualenv/lib/python3.9/site-packages (from eth-keyfile<0.6.0,>=0.5.0->eth_account->-r requirements.txt (line 1)) (0.11.0)
Requirement already satisfied: pycryptodome<4.0.0,>=3.4.7 in ./.virtualenv/lib/python3.9/site-packages (from eth-keyfile<0.6.0,>=0.5.0->eth_account->-r requirements.txt (line 1)) (3.10.1)
Requirement already satisfied: toolz>=0.8.0 in ./.virtualenv/lib/python3.9/site-packages (from cytoolz<1.0.0,>=0.9.0->eth-keyfile<0.6.0,>=0.5.0->eth_account->-r requirements.txt (line 1)) (0.11.1)
Requirement already satisfied: eth-hash<0.4.0,>=0.3.1 in ./.virtualenv/lib/python3.9/site-packages (from eth-utils<2,>=1.3.0->eth_account->-r requirements.txt (line 1)) (0.3.1)
Requirement already satisfied: six>=1.9.0 in ./.virtualenv/lib/python3.9/site-packages (from parsimonious<0.9.0,>=0.8.0->eth-abi<3,>=2.0.0b7->eth_account->-r requirements.txt (line 1)) (1.16.0)
Requirement already satisfied: MarkupSafe>=2.0 in ./.virtualenv/lib/python3.9/site-packages (from Jinja2->-r requirements.txt (line 2)) (2.0.1)
Creating network "bee-docker_default" with the default driver
Pulling bee-1 (ethersphere/bee:0.6.1)...
0.6.1: Pulling from ethersphere/bee
69692152171a: Already exists
4cedb8ecebc9: Pull complete
532a3c115c17: Pull complete
4f47ac1b10f2: Pull complete
Digest: sha256:e1dab670816992856e60af5c00220c123bb2268a227756f37d936b21444de5b6
Status: Downloaded newer image for ethersphere/bee:0.6.1
Creating bee-docker_geth-goerli_1   ... done
Creating bee-docker_clef_1          ... done
Creating bee-docker_node-exporter_1 ... done
Creating cadvisor                          ... done
Creating bee-docker_bee-1_1                ... done
Creating bee-docker_bee-2_1                ... done
Creating bee-docker_bee-3_1                ... done
Creating bee-docker_geth-goerli-exporter_1 ... done
Creating prometheus                        ... done
Creating bee-docker_grafana_1              ... done
Creating bee-docker_alertmanager_1         ... done
Welcome to beeee keeping!

Your hive has been successfully deployed. The details are as follows:

Number of bees:         3
Grafana metrics:        http://192.168.1.100:3000
Grafana credentials:    admin/foobar
Goerli Endpoint (HTTP): http://192.168.1.100:8545
Goerli Endpoint (WS):   ws://192.168.1.100:8546


------------------------------------------------------------------------------
NODE FUNDING
------------------------------------------------------------------------------

Now, you need to get your bee's funded, so head to #faucet on Ethereum Swarm's
discord server, and when you get there...

/sprinkle 0xD3bd5bcEF1a41e7f89c31E22C00F7fB235dfbaa7
/sprinkle 0x4E73B8fe0B2E9D1DCffDe684dd1C311281A9DD14
/sprinkle 0x167c8779ADD5541663cA7D5F19230F28f9CC79f8


------------------------------------------------------------------------------
CHECK YOUR NODE IS WORKING / GET LOGS
------------------------------------------------------------------------------

You've funded your nodes, now you want to check if they're working OK. This 
means we need to dig into the logs! To do so, you can use these commands for
the respective nodes.

    docker logs bee-docker_bee-1_1
    docker logs bee-docker_bee-2_1
    docker logs bee-docker_bee-3_1

You can use the above command varied slightly to change the container name
to check on the status of other containers, like geth, etc.

How about checking for the metrics containers? This will show you all your
containers and how they're doing

    docker ps -a

------------------------------------------------------------------------------
FIREWALL / ROUTING RULES REQUIRED
------------------------------------------------------------------------------

Awesome, you've made it this far. One of the problems plaguing the network at
the moment is "Peer not reachable when attempting to connect". Many, many,
people about this - the problem is that MOST nodes have failed to configure
inbound access, so when you try connect to them, YOU CAN'T! 

Now, as an enthusiastic apiarist, we know our honey tastes great, so we best
share it with the world! If you do NOT have a UPnP router, set the following
rules to ensure you can get inbound connections.

TCP: 199.199.199.199:31000 -> 192.168.1.100:1634
TCP: 199.199.199.199:31001 -> 192.168.1.100:1637
TCP: 199.199.199.199:31002 -> 192.168.1.100:1640

Once you've set these port forwarding firewall / routing rules, you can
monitor your bee's once again using the above docker logs commands and
monitor for inbound connections. If you've got them, congratulations, you're
making the Swarm a better place!


------------------------------------------------------------------------------
DETAILED INFORMATION: bee-1
------------------------------------------------------------------------------

id:                 bee-1
ethereum address:   0xD3bd5bcEF1a41e7f89c31E22C00F7fB235dfbaa7 
etherscan:          https://goerli.etherscan.io/address/0xD3bd5bcEF1a41e7f89c31E22C00F7fB235dfbaa7
debug_api:          http://localhost:1635

sanity checks: 
* Topology:             curl http://localhost:1635/topology | jq
* Addresses:            curl http://localhost:1635/addresses | jq
* Chequebook Address:   curl http://localhost:1635/chequebook/address | jq 

------------------------------------------------------------------------------
DETAILED INFORMATION: bee-2
------------------------------------------------------------------------------

id:                 bee-2
ethereum address:   0x4E73B8fe0B2E9D1DCffDe684dd1C311281A9DD14 
etherscan:          https://goerli.etherscan.io/address/0x4E73B8fe0B2E9D1DCffDe684dd1C311281A9DD14
debug_api:          http://localhost:1638

sanity checks: 
* Topology:             curl http://localhost:1638/topology | jq
* Addresses:            curl http://localhost:1638/addresses | jq
* Chequebook Address:   curl http://localhost:1638/chequebook/address | jq 

------------------------------------------------------------------------------
DETAILED INFORMATION: bee-3
------------------------------------------------------------------------------

id:                 bee-3
ethereum address:   0x167c8779ADD5541663cA7D5F19230F28f9CC79f8 
etherscan:          https://goerli.etherscan.io/address/0x167c8779ADD5541663cA7D5F19230F28f9CC79f8
debug_api:          http://localhost:1641

sanity checks: 
* Topology:             curl http://localhost:1641/topology | jq
* Addresses:            curl http://localhost:1641/addresses | jq
* Chequebook Address:   curl http://localhost:1641/chequebook/address | jq 


up to date, audited 17 packages in 1s

found 0 vulnerabilities
```

## Cashout

The best way to handle cashout is by using [monBee](https://github.com/ldeffenb/monBee), 
an excellent terminal frontend for monitoring your hive. The command to run 
has already been generated by the templates. From the main directory, simply
run:

```bash
$ ./monBee.sh
```

## Bringing down a hive

So the bees have been hard at work, but now it's time to dismantle the hive.
Simply run:

```bash
$ sudo ./down.sh
```

**NOTE**: This does NOT delete the hive directory hosting all the data.


# Donations

As with everything, donations are welcome to help support me to become more
active in this scene.

* ETH: 0x44DCcA483E0d7aD6A5a1b4CE2B6DfDCBc568F545
* BTC: bc1qm93lvp69cucvgfvxv3u78nphnrz7g8tla8apgh

Or if it helped you and you use Brave please tip!

Catch me on Swarm's discord

mfw78.
