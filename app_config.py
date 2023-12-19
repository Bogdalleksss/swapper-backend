config = {
    'PRIVATE_KEY': '5a24485623ee9da433f6dab51d3aaeb624cdacdcd0acf452011876ec28aa8707',
    'WALLET_ADDRESS': '0xC65fe8747f502CF41051938De0f3413970D34737',
    'INCH': {
        'INCH_API_KEY': 'fB6l26FxrqjIr3JWlVbLVglbmi6PkrnW',
        'INCH_SWAP_API_KEY': 'fB6l26FxrqjIr3JWlVbLVglbmi6PkrnW',
    },

    'CHAINS': [
        # Ethereum
        {
            'PRIVATE_KEY': '5a24485623ee9da433f6dab51d3aaeb624cdacdcd0acf452011876ec28aa8707',
            'WALLET_ADDRESS': '0xC65fe8747f502CF41051938De0f3413970D34737',
            'NAME': 'Ethereum',
            'ID': 1,
            'NATIVE_TOKEN_SYMBOL': 'ETH',
            'RPC': 'https://sly-quaint-darkness.discover.quiknode.pro/52c519a37c5f45040d411f6356338391cd60195e/',
            'GAS_LIMIT': 500_000,
            'BASE_TOKEN_SYMBOL': 'USDT',
            'BASE_TOKEN_ADDRESS': '0xdAC17F958D2ee523a2206206994597C13D831ec7',
            'BASE_TOKE_DECIMALS': 6,
            'GAS_FACTOR': 0.3,  # Множитель газа 30% = 0.3
        },

        # BSC
        {
            'PRIVATE_KEY': '5a24485623ee9da433f6dab51d3aaeb624cdacdcd0acf452011876ec28aa8707',
            'WALLET_ADDRESS': '0xC65fe8747f502CF41051938De0f3413970D34737',
            'NAME': 'BSC',
            'ID': 56,
            'NATIVE_TOKEN_SYMBOL': 'BNB',
            'RPC': 'https://thrilling-restless-butterfly.bsc.discover.quiknode.pro/6dde1f42b8ce101d0ecd0666dc7b68e4697dd197/',
            'GAS_LIMIT': 500_000,
            'BASE_TOKEN_SYMBOL': 'USDT',
            'BASE_TOKEN_ADDRESS': '0x55d398326f99059fF775485246999027B3197955',
            'BASE_TOKE_DECIMALS': 18,
            'GAS_FACTOR': 0.3,  # Множитель газа 30% = 0.3
        }

    ]
}
