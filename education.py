def get_educational_content(topic):
    """
    Provides educational content about cryptocurrency topics.
    """
    
    if topic == "bitcoin":
        return """
# 📚 Bitcoin (BTC) Education

## What is Bitcoin?
Bitcoin is the first and largest cryptocurrency, created in 2009 by the pseudonymous Satoshi Nakamoto. It's often called "digital gold" due to its store-of-value properties.

## Key Features:
- **Decentralized**: No central authority controls it
- **Limited Supply**: Only 21 million bitcoins will ever exist
- **Proof of Work**: Uses mining to secure the network
- **Store of Value**: Many consider it a hedge against inflation

## How Bitcoin Works:
1. **Blockchain**: All transactions are recorded on a public ledger
2. **Mining**: Computers solve complex puzzles to validate transactions
3. **Wallets**: Software that stores your private keys
4. **Addresses**: Like bank account numbers for receiving Bitcoin

## Investment Considerations:
- **High Volatility**: Prices can swing dramatically
- **Regulatory Risk**: Government actions can impact price
- **Energy Consumption**: Mining uses significant electricity
- **Adoption**: Growing institutional and corporate acceptance

## Bitcoin vs Traditional Money:
- ✅ **Inflation Resistant**: Fixed supply vs unlimited printing
- ✅ **Borderless**: Send globally without banks
- ✅ **Transparent**: All transactions are public
- ❌ **Volatile**: Price fluctuates more than stable currencies
- ❌ **Energy Intensive**: Environmental concerns

**Remember**: Bitcoin is highly speculative. Only invest what you can afford to lose.
        """
    
    elif topic == "ethereum":
        return """
# 📚 Ethereum (ETH) Education

## What is Ethereum?
Ethereum is a blockchain platform that enables "smart contracts" - self-executing contracts with terms directly written into code. It's the foundation for most decentralized applications (dApps).

## Key Features:
- **Smart Contracts**: Automated agreements without intermediaries
- **dApps**: Decentralized applications run on the network
- **EVM**: Ethereum Virtual Machine executes smart contracts
- **Proof of Stake**: Energy-efficient consensus mechanism

## Ethereum Ecosystem:
1. **DeFi**: Decentralized Finance applications
2. **NFTs**: Non-Fungible Tokens for digital ownership
3. **DAOs**: Decentralized Autonomous Organizations
4. **Layer 2**: Scaling solutions like Polygon and Arbitrum

## The Merge (2022):
Ethereum transitioned from Proof of Work to Proof of Stake, reducing energy consumption by over 99%.

## Investment Considerations:
- **Utility Token**: ETH is used to pay for transactions and smart contracts
- **Deflationary**: Transaction fees are burned, reducing supply
- **Developer Activity**: Largest ecosystem of blockchain developers
- **Competition**: Faces competition from newer blockchains

## Use Cases:
- **DeFi Protocols**: Lending, borrowing, trading without banks
- **NFT Marketplaces**: Digital art and collectibles
- **Gaming**: Blockchain-based games and virtual worlds
- **Identity**: Decentralized identity solutions

**Ethereum is more than a currency - it's a platform for the decentralized web.**
        """
    
    elif topic == "general":
        return """
# 📚 Cryptocurrency Basics for Beginners

## What is Cryptocurrency?
Cryptocurrency is digital or virtual money secured by cryptography. Unlike traditional currency, it's decentralized and typically runs on blockchain technology.

## Key Concepts:

### 🔗 Blockchain
- Digital ledger that records all transactions
- Distributed across many computers worldwide
- Immutable: Once recorded, very difficult to change

### 💰 Market Cap
- Total value of all coins in circulation
- Calculated as: Price × Circulating Supply
- Indicates the overall size and stability of a cryptocurrency

### 📊 Volatility
- How much the price fluctuates
- Crypto is generally more volatile than traditional assets
- Higher volatility = higher risk and potential reward

### 🏦 Wallets
- Software or hardware that stores your cryptocurrency
- **Hot Wallets**: Connected to internet (convenient but less secure)
- **Cold Wallets**: Offline storage (more secure for large amounts)

## Types of Cryptocurrencies:

### 1. Bitcoin (BTC)
- First cryptocurrency, digital gold
- Store of value, limited supply

### 2. Altcoins
- All cryptocurrencies other than Bitcoin
- Examples: Ethereum, Cardano, Solana

### 3. Stablecoins
- Pegged to stable assets like US Dollar
- Less volatile, used for trading and payments

### 4. Utility Tokens
- Provide access to specific blockchain services
- Examples: ETH for Ethereum, BNB for Binance

## Investment Principles:

### ✅ Do:
- Research before investing (DYOR - Do Your Own Research)
- Start with small amounts
- Diversify across multiple cryptocurrencies
- Use reputable exchanges
- Secure your private keys

### ❌ Don't:
- Invest more than you can afford to lose
- Fall for "get rich quick" schemes
- Share your private keys with anyone
- Make emotional decisions based on FOMO
- Put all money in one cryptocurrency

## Common Mistakes to Avoid:
1. **FOMO Buying**: Buying at peak prices due to fear of missing out
2. **No Research**: Investing without understanding the technology
3. **Weak Security**: Not properly securing wallets and keys
4. **Overinvesting**: Putting too much money at risk
5. **Day Trading**: Trying to time the market without experience

**Remember**: Cryptocurrency is a high-risk, high-reward investment. Never invest more than you can afford to lose completely.
        """
    
    else:
        return get_educational_content("general")

def get_risk_explanation():
    """
    Provides detailed explanation of cryptocurrency investment risks.
    """
    return """
# ⚠️ Cryptocurrency Investment Risks

Understanding risks is crucial before investing in cryptocurrency. Here are the main risks to consider:

## 1. 📈 Market Volatility
**Description**: Crypto prices can swing dramatically in short periods.
- Bitcoin has experienced 80%+ drops from all-time highs
- Daily price swings of 10-20% are common
- News and sentiment can cause rapid price movements

**Example**: In 2022, many cryptocurrencies lost 70-90% of their value.

## 2. 🏛️ Regulatory Risk
**Description**: Government actions can significantly impact cryptocurrency prices.
- Countries may ban or restrict cryptocurrency use
- New regulations can affect trading and adoption
- Tax law changes can impact profitability

**Example**: China's crypto ban in 2021 caused major market drops.

## 3. 🔧 Technology Risk
**Description**: Blockchain technology is still evolving and can face technical issues.
- Smart contract bugs can lead to losses
- Network congestion can cause high fees
- Scaling challenges may limit adoption

**Example**: The DAO hack in 2016 led to Ethereum's controversial hard fork.

## 4. 🔐 Security Risk
**Description**: Digital assets can be lost through hacking or user error.
- Exchange hacks can result in total loss
- Lost private keys mean permanently lost funds
- Phishing attacks and scams are common

**Example**: Mt. Gox exchange collapse in 2014 caused $460M in losses.

## 5. 💧 Liquidity Risk
**Description**: Some cryptocurrencies may be difficult to sell quickly.
- Smaller cryptocurrencies may have low trading volume
- Market stress can reduce liquidity
- Large sales can significantly impact price

## 6. 🌍 Environmental Risk
**Description**: Energy consumption concerns may affect adoption.
- Proof of Work cryptocurrencies use significant energy
- Environmental regulations may impact mining
- ESG concerns from institutions and governments

## Risk Management Strategies:

### 💼 Portfolio Diversification
- Don't put all funds in one cryptocurrency
- Mix large-cap and smaller cryptocurrencies
- Consider traditional assets alongside crypto

### 🎯 Position Sizing
- **Conservative**: 1-5% of total investment portfolio
- **Moderate**: 5-10% of total investment portfolio
- **Aggressive**: 10-20% of total investment portfolio

### 📅 Time Management
- **Dollar-Cost Averaging**: Invest fixed amounts regularly
- **HODL Strategy**: Hold long-term through volatility
- **Take Profits**: Gradually sell portions during gains

### 🔒 Security Best Practices
- Use reputable exchanges with insurance
- Enable two-factor authentication
- Store large amounts in hardware wallets
- Never share private keys

## Risk Assessment Questions:
Before investing, ask yourself:

1. **Can I afford to lose this money completely?**
2. **Do I understand the technology and use case?**
3. **Am I prepared for 50%+ price drops?**
4. **Do I have an emergency fund first?**
5. **Am I investing or gambling?**

## Warning Signs to Avoid:
- 🚨 Promises of guaranteed returns
- 🚨 Pressure to invest immediately
- 🚨 Requests for private keys or passwords
- 🚨 Unknown or unaudited projects
- 🚨 Celebrity endorsements without substance

**Remember**: Higher potential returns come with higher risks. Never invest more than you can afford to lose, and always do your own research before making investment decisions.

**This is not financial advice. Consult with a qualified financial advisor before making investment decisions.**
    """
