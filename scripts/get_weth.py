from brownie import interface, network, config
from scripts.helpful_scripts import get_account


def main():
    pass

def get_weth():
    """
    Mints WETH by depositing ETH
    """
    account = get_account()
    weth = interface.IWETH(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    print("Received 0.1 WETH")
    return tx
