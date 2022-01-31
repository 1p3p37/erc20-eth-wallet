#!/usr/bin/python3

import os
from brownie import *
from brownie import Token, accounts, network, Wallet, SwapContract, ContractContainer
from distutils.util import strtobool


#
# #network.connect("development")
def main():
    dev = accounts.add(os.getenv('PRIVATE_KEY'))
    publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False

    return ContractContainer.deploy({'from': dev}, publish_source=publish_source)
