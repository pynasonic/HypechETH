## Chapter 2. Build up one Ethereum Network at Your Home

The best learning strategy is just do it. Before we use real money to jump into the crucial Ethereum world, we will build up one mimic Ethereum network in our home. We will continue Ethereum journey after become familar with all the concepts and tricks. Find a couple of spared computers or laptops, we run build and run an Ethereum at home.

I found 3 old computers from my basement. I'm going to setup my Ethereum with them.

1. 5 years old RIO desktop with i7-8700, 16G RAM, 1T Harddrive, 120G SSD. 
2. 6 years old Macbook Pro.
3. 9 years old Lenovo V330 Laptop. 

RIO and Laptop are Windows 11. 

On top of Windows Server 2022, download VMWare Workstation 17. Create a new Virtual Machine and install Ubuntu 14.04. The virtual machine is installed on 120G SSD.

The plan is building an Ethereum network with these 3 computers, then conduct all the transactions or other functions same with real ETH2.0 network. 

We'll start from the HP Pavilion. I will set up our home private Ethereum network of two nodes in HP. Both nodes will run on the my HP Desktop. Below is a step-by-step instruction to build our own Ethereum network. 


**Table of content:**
- [Step 1. Setup Directory Structure](#directory)
- [Step 2. Create New Accounts](#newaccount)
- [Step 3. Genesis Block](#genesieblock)
- [Step 4. Initializing the Geth Database](#initializegeth)

<a id="directory"></a>
### Step 1. Setup Directory Structure
The data directories in HP Desktop for each node will be named <span style="background-color:green">HPNode1</span> and <span style="background-color:green">HPNode2</span>. 

The HP is running Ubuntu in VMWare. After starting Ubuntu, use Xshell to connect it from Windows. 

```
mkdir hypech
mkdir hypech/myNet
mkdir hypech/myNet/HPNode1
mkdir hypech/myNet/HPNode2
```
![Directory Structure](image-4.png)

<a id="newaccount"></a>
### Step 2: Create Ethereum accounts. 
Each node is supposed to have one account connected. We will created one account for each node. To make the life easier, we store the password as a text file. 

```
cd hypech
echo "hpnode1pwd" > myNet/HPNode1/hpnode1pwd.txt
echo "hpnode2pwd" > myNet/HPNode2/hpnode2pwd.txt
geth --datadir myNet/HPNode1/ account new --password myNet/HPNode1/hpnode1pwd.txt
geth --datadir myNet/HPNode2/ account new --password myNet/HPNode2/hpnode2pwd.txt
```
![new account](image-5.png)

Make note of the public key generated for each account, as it will be referenced in the genesis block configuration below.

`Public address of the key for HPNode1:   0x79f04797E9e1aF0d31ee22079e7d83F553841DE7`

`Public address of the key for HPNode2:   0x1144933E7DDFb887Ea5aaee4D5dD1498D817FAbe`

<a id="genesisblock"></a>
### Step 3: Genesis block

The first block of every Ethereum-based blockchain is known as the genesis block. Since we are not connected to the public Ethereum network, we have to create the genesis block by ourselves. In the case of Ethereum mainnet, the genesis block is [hard-coded](https://github.com/ethereum/go-ethereum/blob/master/core/genesis.go) into the `geth` source code. In the case of a private/custom `geth` network, the genesis block is configurable. Create a new file called `genesis.json` and insert the following. 
In Genesis block time, the ETH coins are assinged, not mined or through other ways. In our case, we assign 100 ETHs to HPNode1, and 200 ETHs to HPNode2. The ETH network by default is using wei as the units. One ETH equals 1 following 18 0s wei. That's why we have so many 0s in our code. 
Other parts have specific meaning. We'll get back it later. For now, just create this file using your favorite way. I use nano to creat it.

```
nano genesis.json
```


```json
{
  "config": {
    "chainId": 12345,
    "homesteadBlock": 0,
    "eip150Block": 0,
    "eip155Block": 0,
    "eip158Block": 0,
    "byzantiumBlock": 0,
    "constantinopleBlock": 0,
    "petersburgBlock": 0,
    "istanbulBlock": 0,
    "berlinBlock": 0,
    "clique": {
      "period": 5,
      "epoch": 30000
    }
  },
  "difficulty": "1",
  "gasLimit": "80000000000000000",
  "extradata": "0x00000000000000000000000000000000000000000000000000000000000000007df9a875a174b3bc565e6424a0050ebc1b2d1d820000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
  "alloc": {
    "79f04797E9e1aF0d31ee22079e7d83F553841DE7": { "balance": "100000000000000000000" },
    "1144933E7DDFb887Ea5aaee4D5dD1498D817FAbe": { "balance": "200000000000000000000" }
  }
}
```
![Alt text](image-7.png)
Before moving to the next step, let's see what we've done so far:
![Alt text](image-8.png)


<a id="initializegeth"></a>
### Step 4: Initializing the Geth Database

To create a blockchain node that uses this genesis block, first use geth init to import and sets the canonical genesis block for the new chain. This requires the path to genesis.json to be passed as an argument.

```
geth --datadir myNet/HPNode1/ init genesis.json
geth --datadir myNet/HPNode2/ init genesis.json
```

![Alt text](image-9.png)

The default value for the storage scheme is hash. In case the plan is to use the path based storage scheme, the --state.scheme=path needs to be passed during the init step. This will ensure that the database is initialized with the correct storage scheme for the network.

`geth --state.scheme=path init --datadir data genesis.json`

<a id="bootnode"></a>
### Step 5: Setting Up Networking

With the node configured and initialized, the next step is to set up a peer-to-peer network. This requires a bootstrap node. The bootstrap node is a normal node that is designated to be the entry point that other nodes use to join the network. Any node can be chosen to be the bootstrap node.

To configure a bootstrap node, the IP address of the machine the bootstrap node will run on must be known. The bootstrap node needs to know its own IP address so that it can broadcast it to other nodes. On a local machine this can be found using tools such as ifconfig and on cloud instances such as Amazon EC2 the IP address of the virtual machine can be found in the management console. Any firewalls must allow UDP and TCP traffic on port 30303.

The bootstrap node IP is set using the --nat flag (the command below contains an example address - replace it with the correct one).

`geth --datadir data --networkid 998101 --nat extip:192.168.68.62`


The next step is to configure a bootnode. This can be any node, but for this tutorial the developer tool bootnode will be used to quickly and easily configure a dedicated bootnode. First the bootnode requires a key, which can be created with the following command, which will save a key to boot.key:

`bootnode -genkey boot.key`

This key can then be used to generate a bootnode as follows:

`bootnode -nodekey boot.key -addr :30305`

The choice of port passed to -addr is arbitrary, but public Ethereum networks use 30303, so this is best avoided. The bootnode command returns the following logs to the terminal, confirming that it is running:
![Alt text](image-11.png)


<a id="startnodes"></a>
### Step 6: Start Nodes

The two nodes can now be started. Open separate terminals for each node, leaving the bootnode running in the original terminal. In each terminal, run the following command (replacing node1 with node2 where appropriate, and giving each node different --port and authrpc.port IDs. The account address and password file for node 1 must also be provided:

```
cd myNet
geth --datadir HPNode1 --port 30306 --bootnodes enode://49b24d4d9f43cb6bedb870082f7c101acfa12d6dae9f701341258eb9be5a104f6c3bc5199dc8a1b133a4b06fa4413bb9735374b09d7c04e29e1e10435c74660d@127.0.0.1:0?discport=30305  --networkid 998101 --unlock 0x79f04797E9e1aF0d31ee22079e7d83F553841DE7 --password HPNode1/hpnode1pwd.txt --authrpc.port 8551
```

This will start the node using the bootnode as an entry point. Repeat the same command with the information appropriate to node 2. In each terminal, the following logs indicate success:
