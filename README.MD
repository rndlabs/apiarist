# Apiarist

For those that have been active in the [Ethereum Swarm](https://swarm.ethereum.org)
for a while have come to know the desire to scale their hives 🐝, in effect
working to perfect the ancient art of bee keeping - to become *the* apiarist.

## Motivations

If you want your hives to *hummmm*, they need to be well planned. *Apiarist* is
designed with the following intentions:

1. Number of 🐝 nodes: >1
2. Swap endpoint: Running our own geth goerli endpoint, independent of slock.it
   and infura.
3. Metrics: A template setup for *prometheus*, *grafana*, and *alertmanager*.
4. Clef: Scalable use of *clef* with one instance per hive.

## Data structure design

Everything is designed initially to run from `/hive` with the following file
structure (it is assumed that you mount suitable disk space to `/hive`:

```
drwxr-xr-x 39     0     0 4.0K Apr 29 01:15 .
drwxr-xr-x 21     0     0 4.0K Apr 28 23:07 ..
drwxr-xr-x  5   999   999 4.0K Apr 29 02:02 bee-1
drwxr-xr-x  5   999   999 4.0K Apr 29 03:38 bee-10
drwxr-xr-x  5   999   999 4.0K Apr 29 04:59 bee-2
drwxr-xr-x  5   999   999 4.0K Apr 29 05:01 bee-3
drwxr-xr-x  5   999   999 4.0K Apr 29 03:08 bee-4
drwxr-xr-x  5   999   999 4.0K Apr 29 02:59 bee-5
drwxr-xr-x  5   999   999 4.0K Apr 29 02:59 bee-6
drwxr-xr-x  5   999   999 4.0K Apr 29 02:59 bee-7
drwxr-xr-x  5   999   999 4.0K Apr 29 03:35 bee-8
drwxr-xr-x  5   999   999 4.0K Apr 29 03:33 bee-9
drwxr-x---  4 65534     0 4.0K Apr 28 13:53 clef
drwx------  3     0     0 4.0K Apr 28 13:10 ethereum
drwxr-xr-x  4   472     0 4.0K Apr 29 13:09 grafana
drwx------  2     0     0  16K Apr 28 23:07 lost+found
-rwxrwxrwx  1   997   997   32 Apr 28 13:51 password
drwxrwxrwx  3 65534 65534 4.0K Apr 29 01:55 prometheus
```

**WARNING: FAILURE TO OBSERVE THE ABOVE FILE PERMISSIONS AND FILE OWNERSHIP
WILL RESULT IN ERRORS WHEN DEPLOYING THE HIVE.**

To fix permission errors:

```bash
sudo mkdir /hive
sudo mkdir /hive/{bee-1,2,3,4,6,7,8,9,10}
sudo mkdir /hive/{clef,ethereum,grafana,prometheus}
sudo chown 999:999 /hive/{bee-1,2,3,4,6,7,8,9,10}
sudo chown 65534:0 /hive/clef
sudo chown 65534:65534 /hive/prometheus
sudo chmod 755 /hive/{bee-1,2,3,4,6,7,8,9,10}
sudo chmod 750 /hive/clef
sudo chmod 755 /hive/{prometheus,grafana}
```

## Clef configuration

Initially install `bee-clef` using the [documentation](https://docs.ethswarm.org/docs/installation/bee-clef). Once this is installed, this will create a default
password to protect the keystore, and also create a new account (Ethereum
address).

Now:

1. Edit `generate_addresses.sh` appropriately to determine how many addresses
   to create and use with `clef`.
2. Run:

   ```bash
   sudo bash generate_addresses.sh
   ```
3. This will output all the Ethereum addresses that are available now in `clef`.
4. Let's copy over the `clef` data to our hive area....

   ```bash
   sudo cp -pR /var/lib/bee-clef/* /hive/clef/
   ```
5. Copy the keystore password to the correct area.

   **WARNING: THIS IS ONLY FOR TESTING PURPOSES. THIS IS NOT BEST SECURITY
   PRACTICES.**

   I've elected to use the same password for the `clef` keystore and for `bee`.
   I haven't checked if they could be different, so for the moment, I set them
   to be the same, but due to the active user for `bee` (uid/gid 999/999), and
   `clef` (uid/gid 65534/0), the password must be set to readable by all.

   Once again, this is terrible security practices. USE WITH EXTREME CAUTION,
   YOU'VE BEEN WARNED.

   ```bash
   cp -pR /var/lib/bee-clef/password /hive/password
   chmod 777 /hive/password
   ```

## Docker compose setup

Now edit the `docker-compose.yml` and edit the respective YAML, eg:

```yaml
    - BEE_CLEF_SIGNER_ETHEREUM_ADDRESS=0000000000000000000000000000000000000000
```

Unfortunately there's no automatic provisioning yet to extract the keys from
clef, this would essentially require a two-pass system to set this up, which
it's a bit easier at the moment to do manually.

## Operation

Before you start it, **CHECK THE PROBLEMS / FAULTS** in the section below.

To start everything:

```bash
docker-compose up -d
```

## Problems / Faults

1. Installs everything with a local geth node that syncs with goerli. As such,
   it will start everything from scratch. Either copy your existing geth
   folder into `/hive/ethereum` or set slock.it temporarily in `.env` while
   it geth syncs.
2. There exists a very weird race condition that I observed whereby when
   starting multiple bee nodes, one bee node would successfully deploy it's
   chequebook contract, but subsequent nodes would fail with an `Out of Gas`
   error. Only way around this was adding nodes individually which was very
   painful.
3. For any other faults, please file an [issue](https://github.com/mfw78/apiarist/issues)!

# Donations

As with everything, donations are welcome to help support me to become more
active in this scene.

* ETH: 0x44DCcA483E0d7aD6A5a1b4CE2B6DfDCBc568F545
* BTC: bc1qm93lvp69cucvgfvxv3u78nphnrz7g8tla8apgh

Or if it helped you and you use Brave please tip!

Catch me on Swarm's discord

mfw78.
