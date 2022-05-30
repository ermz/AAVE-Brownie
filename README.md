1. Swap our ETH for WETH
2. Deposit some ETH (WETH) into AAVE
3. Borrow some asset with ETH collateral
    1. Sell that borrowed asset. (Short selling)
4. Repay everything back

Testing:

Integration test: Kovan
Unit tests: Mainnet-fork (Fork everything from mainnet into our local development, basically mock the entire network)

"""
    Default Testing Network: Development with Mocking (You need mocks when using oracles, Oracles will only run in mainnet)
    If you have no oracles: You can use mainnet-fork for testing
"""
