## Chapter 2. Build up one Ethereum Network at Your Home

The best learning strategy is just do it. Before we use real money to jump into the crucial Ethereum world, we will build up one mimic Ethereum network in our home. We will continue Ethereum journey after become familar with all the concepts and tricks. Find a couple of spared computers or laptops, we run build and run an Ethereum at home.

I found 3 old computers from my basement. I'm going to setup my Ethereum with them.

1. 5 years old HP Pavilion desktop with i7-8700, 16G RAM, 1T Harddrive, 120G SSD. 
2. 6 years old Macbook Pro.
3. 9 years old Lenovo V330 Laptop. 

The Windows 11 is too slow in the old computer. I changed them to Windows Server 2022 (it's not necessary if you have a faster computer or you don't mind waiting). The Windows OS is installed on the 1T harddrive. 

On top of Windows Server 2022, download VMWare Workstation 17. Create a new Virtual Machine and install Ubuntu 14.04. The virtual machine is installed on 120G SSD.

The plan is building an Ethereum network with these 3 computers, then conduct all the transactions or other functions same with real ETH2.0 network. 

We'll start from the HP Pavilion. I will set up our home private Ethereum network of two nodes in HP. Both nodes will run on the my HP Desktop. Below is a step-by-step instruction to build our own Ethereum network. 


**Table of content:**
- [Step 1. Setup Directory Structure](#directory)
- [Step 2. Hello World](#item-one)
- [First Item](#item-two)
- [Second Item](#item-three)

<a id="directory"></a>
### Step 1. Setup Directory Structure
The data directories in HP Desktop for each node will be named <span style="background-color:green">HPNode1</span> and <span style="background-color:green">HPNode2</span>. 

The HP is running Ubuntu in VMWare. After starting Ubuntu, use Xshell to connect it from Windows. 

```
mkdir hypech/
mkdir hypech/privatenetwork
mkdir hypech/privatenetwork/HPNode1
mkdir hypech/privatenetwork/HPNode2
```

![The Directory Strucution is like this](image.png)

<a id="item-two"></a>
### Step 2: Create Ethereum accounts. 
Each node is supposed to have one account connected. We will created one account for each node. To make the life easier, we store the password as a text file. 

```
cd hypech
echo "hpnode1pwd" > HPNode1/hpnode1pwd.txt
echo "hpnode2pwd" > HPNode2/hpnode2pwd.txt
geth --datadir HPNode1/ account new --password HPNode1/hpnode1pwd.txt
geth --datadir HPNode2/ account new --password HPNode2/hpnode2pwd.txt
```
![Alt text](image-1.png)

Make note of the public key generated for each account, as it will be referenced in the genesis block configuration below.

`Public address of the key for HPNode1:   0x4915D4a7fbb61881BC312de78301C48949539aFD`

`Public address of the key for HPNode2:   0x454C8CFdD4b1753f0169e7E74cd2c1766cd9272C`



<a id="item-three"></a>
### Step 3: Genesis block

The first block of every Ethereum-based blockchain is known as the genesis block. Since we are not connected to the public Ethereum network, we have to create the genesis block by ourselves. In the case of Ethereum mainnet, the genesis block is [hard-coded](https://github.com/ethereum/go-ethereum/blob/master/core/genesis.go) into the `geth` source code. In the case of a private/custom `geth` network, the genesis block is configurable. Create a new file called `genesis.json` and insert the following. 
In Genesis block time, the ETH coins are assinged, not mined or through other ways. In our case, we assign 100 ETHs to HPNode1, and 200 ETHs to HPNode2. The ETH network by default is using wei as the units. One ETH equals 1 following 18 0s wei. That's why we have so many 0s in our code. 
Other parts have specific meaning. We'll get back it later. For now, just create this file using your favorite way. 

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
    "4915D4a7fbb61881BC312de78301C48949539aFD": { "balance": "100000000000000000000" },
    "454C8CFdD4b1753f0169e7E74cd2c1766cd9272C": { "balance": "200000000000000000000" }
  }
}
```
![Alt text](image-2.png)


Second Item
Second item content goes here




1. [Setup Directory Structure](#ajax)
3. [C](#c)
* [HTML and CSS](#html-and-css)
* [Javascript](#javascript)
* [MySQL](#mysql)
* [PHP](#php)
* [Scratch](#scratch)


### Ajax

* [Ajax](http://etutoriale.ro/articles/1483/1/Tutorial-Ajax/)


### C

* [Ghidul Beej pentru Programarea in Retea - Folosind socket de internet](https://web.archive.org/web/20180710112954/http://weknowyourdreams.com/beej.html) - Brian "Beej Jorgensen" Hall, Dragos Moroianu (HTML) *(:card_file_box: archived)*





Chapter 2. Hello World Ethereum POA Network on Your Own Computer

Here is an end-to-end example. We'll build up it from scratch on.
