import pandas as pd
from datetime import datetime, timedelta
import random

def get_crypto_data():
    """
    Returns predefined cryptocurrency data with profitability and sustainability metrics.
    This data represents realistic market conditions but should not be used for actual trading.
    """
    crypto_data = {
        "BTC": {
            "name": "Bitcoin",
            "symbol": "BTC",
            "market_cap_rank": 1,
            "market_cap": 850000000000,  # $850B
            "price_usd": 43500,
            "price_change_24h": 2.5,
            "price_change_7d": 8.2,
            "price_change_30d": 15.8,
            "volume_24h": 25000000000,
            "energy_consumption": "High",  # Proof of Work
            "consensus_mechanism": "Proof of Work",
            "sustainability_score": 3,  # 1-10 scale
            "volatility": "High",
            "adoption_score": 10,
            "technology_maturity": 9,
            "regulatory_clarity": 7,
            "use_cases": ["Store of Value", "Digital Gold", "Payment"],
            "risk_level": "Medium-High"
        },
        "ETH": {
            "name": "Ethereum",
            "symbol": "ETH",
            "market_cap_rank": 2,
            "market_cap": 280000000000,  # $280B
            "price_usd": 2350,
            "price_change_24h": 3.1,
            "price_change_7d": 12.4,
            "price_change_30d": 22.1,
            "volume_24h": 15000000000,
            "energy_consumption": "Low",  # Post-merge PoS
            "consensus_mechanism": "Proof of Stake",
            "sustainability_score": 8,
            "volatility": "High",
            "adoption_score": 9,
            "technology_maturity": 8,
            "regulatory_clarity": 6,
            "use_cases": ["Smart Contracts", "DeFi", "NFTs", "dApps"],
            "risk_level": "Medium-High"
        },
        "ADA": {
            "name": "Cardano",
            "symbol": "ADA",
            "market_cap_rank": 8,
            "market_cap": 18000000000,  # $18B
            "price_usd": 0.52,
            "price_change_24h": 1.8,
            "price_change_7d": 6.3,
            "price_change_30d": 18.5,
            "volume_24h": 400000000,
            "energy_consumption": "Very Low",
            "consensus_mechanism": "Proof of Stake",
            "sustainability_score": 9,
            "volatility": "High",
            "adoption_score": 6,
            "technology_maturity": 7,
            "regulatory_clarity": 8,
            "use_cases": ["Smart Contracts", "Academic Research", "Sustainability"],
            "risk_level": "Medium"
        },
        "SOL": {
            "name": "Solana",
            "symbol": "SOL",
            "market_cap_rank": 5,
            "market_cap": 45000000000,  # $45B
            "price_usd": 105,
            "price_change_24h": 4.2,
            "price_change_7d": 15.1,
            "price_change_30d": 28.7,
            "volume_24h": 2000000000,
            "energy_consumption": "Low",
            "consensus_mechanism": "Proof of History + Proof of Stake",
            "sustainability_score": 7,
            "volatility": "Very High",
            "adoption_score": 7,
            "technology_maturity": 6,
            "regulatory_clarity": 5,
            "use_cases": ["Fast Transactions", "DeFi", "NFTs", "Gaming"],
            "risk_level": "High"
        },
        "MATIC": {
            "name": "Polygon",
            "symbol": "MATIC",
            "market_cap_rank": 12,
            "market_cap": 8500000000,  # $8.5B
            "price_usd": 0.92,
            "price_change_24h": 2.7,
            "price_change_7d": 11.8,
            "price_change_30d": 25.3,
            "volume_24h": 450000000,
            "energy_consumption": "Very Low",
            "consensus_mechanism": "Proof of Stake",
            "sustainability_score": 9,
            "volatility": "Very High",
            "adoption_score": 7,
            "technology_maturity": 7,
            "regulatory_clarity": 6,
            "use_cases": ["Ethereum Scaling", "DeFi", "Gaming", "NFTs"],
            "risk_level": "High"
        },
        "LINK": {
            "name": "Chainlink",
            "symbol": "LINK",
            "market_cap_rank": 15,
            "market_cap": 7800000000,  # $7.8B
            "price_usd": 14.20,
            "price_change_24h": 1.5,
            "price_change_7d": 5.8,
            "price_change_30d": 12.4,
            "volume_24h": 350000000,
            "energy_consumption": "Low",
            "consensus_mechanism": "Oracle Network",
            "sustainability_score": 7,
            "volatility": "High",
            "adoption_score": 8,
            "technology_maturity": 8,
            "regulatory_clarity": 7,
            "use_cases": ["Oracle Services", "DeFi Data", "Smart Contract Integration"],
            "risk_level": "Medium"
        },
        "DOT": {
            "name": "Polkadot",
            "symbol": "DOT",
            "market_cap_rank": 11,
            "market_cap": 9200000000,  # $9.2B
            "price_usd": 7.35,
            "price_change_24h": 2.1,
            "price_change_7d": 8.9,
            "price_change_30d": 16.7,
            "volume_24h": 280000000,
            "energy_consumption": "Low",
            "consensus_mechanism": "Nominated Proof of Stake",
            "sustainability_score": 8,
            "volatility": "High",
            "adoption_score": 6,
            "technology_maturity": 7,
            "regulatory_clarity": 6,
            "use_cases": ["Interoperability", "Parachain Ecosystem", "Cross-chain"],
            "risk_level": "Medium-High"
        },
        "LTC": {
            "name": "Litecoin",
            "symbol": "LTC",
            "market_cap_rank": 14,
            "market_cap": 6800000000,  # $6.8B
            "price_usd": 92.50,
            "price_change_24h": 1.2,
            "price_change_7d": 4.5,
            "price_change_30d": 8.9,
            "volume_24h": 650000000,
            "energy_consumption": "Medium",
            "consensus_mechanism": "Proof of Work (Scrypt)",
            "sustainability_score": 5,
            "volatility": "Medium",
            "adoption_score": 8,
            "technology_maturity": 9,
            "regulatory_clarity": 8,
            "use_cases": ["Fast Payments", "Bitcoin Alternative", "P2P Transactions"],
            "risk_level": "Medium"
        },
        "AVAX": {
            "name": "Avalanche",
            "symbol": "AVAX",
            "market_cap_rank": 9,
            "market_cap": 14500000000,  # $14.5B
            "price_usd": 38.20,
            "price_change_24h": 3.8,
            "price_change_7d": 13.2,
            "price_change_30d": 21.8,
            "volume_24h": 520000000,
            "energy_consumption": "Low",
            "consensus_mechanism": "Avalanche Consensus",
            "sustainability_score": 8,
            "volatility": "Very High",
            "adoption_score": 6,
            "technology_maturity": 6,
            "regulatory_clarity": 5,
            "use_cases": ["DeFi", "Enterprise Blockchain", "Fast Finality"],
            "risk_level": "High"
        },
        "XLM": {
            "name": "Stellar",
            "symbol": "XLM",
            "market_cap_rank": 25,
            "market_cap": 3200000000,  # $3.2B
            "price_usd": 0.115,
            "price_change_24h": 0.8,
            "price_change_7d": 3.2,
            "price_change_30d": 7.5,
            "volume_24h": 180000000,
            "energy_consumption": "Very Low",
            "consensus_mechanism": "Stellar Consensus Protocol",
            "sustainability_score": 9,
            "volatility": "Medium",
            "adoption_score": 7,
            "technology_maturity": 8,
            "regulatory_clarity": 7,
            "use_cases": ["Cross-border Payments", "Remittances", "Financial Inclusion"],
            "risk_level": "Medium"
        }
    }
    
    return crypto_data

def get_market_trends():
    """
    Returns current market trend data for different categories.
    """
    trends = [
        {"category": "Large Cap (>$10B)", "change": 5.2},
        {"category": "Mid Cap ($1B-$10B)", "change": 8.7},
        {"category": "Small Cap (<$1B)", "change": -2.1},
        {"category": "DeFi Tokens", "change": 12.4},
        {"category": "Layer 1 Protocols", "change": 7.8},
        {"category": "Sustainable Cryptos", "change": 9.1}
    ]
    
    return trends

def get_crypto_by_symbol(symbol):
    """
    Returns specific cryptocurrency data by symbol.
    """
    data = get_crypto_data()
    return data.get(symbol.upper())

def get_top_cryptos_by_market_cap(limit=10):
    """
    Returns top cryptocurrencies sorted by market cap.
    """
    data = get_crypto_data()
    sorted_cryptos = sorted(data.items(), key=lambda x: x[1]['market_cap'], reverse=True)
    return dict(sorted_cryptos[:limit])

def get_sustainable_cryptos():
    """
    Returns cryptocurrencies with high sustainability scores.
    """
    data = get_crypto_data()
    sustainable = {k: v for k, v in data.items() if v['sustainability_score'] >= 7}
    return sustainable

def get_low_risk_cryptos():
    """
    Returns cryptocurrencies considered lower risk.
    """
    data = get_crypto_data()
    low_risk = {k: v for k, v in data.items() if v['risk_level'] in ['Medium', 'Medium-Low'] and v['market_cap_rank'] <= 15}
    return low_risk
