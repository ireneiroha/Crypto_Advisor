from crypto_data import get_crypto_data, get_crypto_by_symbol, get_sustainable_cryptos, get_low_risk_cryptos
import random

class CryptoAdvisor:
    def __init__(self):
        self.crypto_data = get_crypto_data()
        self.risk_profiles = {
            "low": {
                "max_volatility": "Medium",
                "min_market_cap_rank": 15,
                "min_regulatory_clarity": 6,
                "preferred_risk_levels": ["Low", "Medium"]
            },
            "medium": {
                "max_volatility": "High",
                "min_market_cap_rank": 25,
                "min_regulatory_clarity": 5,
                "preferred_risk_levels": ["Medium", "Medium-High"]
            },
            "high": {
                "max_volatility": "Very High",
                "min_market_cap_rank": 50,
                "min_regulatory_clarity": 4,
                "preferred_risk_levels": ["Medium-High", "High"]
            }
        }
    
    def get_investment_recommendations(self, risk_tolerance="medium"):
        """
        Generate investment recommendations based on risk tolerance.
        """
        profile = self.risk_profiles.get(risk_tolerance, self.risk_profiles["medium"])
        recommendations = []
        
        # Filter cryptocurrencies based on risk profile
        suitable_cryptos = self._filter_cryptos_by_risk(profile)
        
        if not suitable_cryptos:
            return "No suitable cryptocurrencies found for your risk profile. Please try a different risk level."
        
        # Sort by multiple criteria
        ranked_cryptos = self._rank_cryptos(suitable_cryptos, risk_tolerance)
        
        # Generate recommendations
        response = f"## Investment Recommendations for {risk_tolerance.title()} Risk Tolerance\n\n"
        
        for i, (symbol, crypto) in enumerate(ranked_cryptos[:5]):
            score = self._calculate_investment_score(crypto, risk_tolerance)
            
            response += f"### {i+1}. {crypto['name']} ({symbol})\n"
            response += f"**Investment Score: {score}/10**\n\n"
            response += f"📊 **Market Cap Rank**: #{crypto['market_cap_rank']}\n"
            response += f"💰 **Current Price**: ${crypto['price_usd']:,.2f}\n"
            response += f"📈 **30-day Performance**: {crypto['price_change_30d']:+.1f}%\n"
            response += f"⚡ **Energy Efficiency**: {crypto['energy_consumption']}\n"
            response += f"🛡️ **Risk Level**: {crypto['risk_level']}\n\n"
            
            # Why this recommendation
            response += f"**Why {crypto['name']}?**\n"
            response += self._generate_recommendation_reasoning(crypto, risk_tolerance)
            response += "\n\n"
        
        # Add portfolio allocation suggestion
        response += self._generate_portfolio_allocation(ranked_cryptos[:5], risk_tolerance)
        
        # Add important disclaimer
        response += "\n\n⚠️ **Important**: These recommendations are for educational purposes only. Always do your own research and never invest more than you can afford to lose."
        
        return response
    
    def analyze_specific_crypto(self, symbol):
        """
        Provide detailed analysis of a specific cryptocurrency.
        """
        crypto = get_crypto_by_symbol(symbol)
        
        if not crypto:
            return f"Sorry, I don't have information about {symbol}. Please try another cryptocurrency."
        
        score = self._calculate_investment_score(crypto, "medium")
        
        response = f"# {crypto['name']} ({crypto['symbol']}) Analysis\n\n"
        
        # Current metrics
        response += "## 📊 Current Metrics\n"
        response += f"- **Price**: ${crypto['price_usd']:,.2f}\n"
        response += f"- **Market Cap Rank**: #{crypto['market_cap_rank']}\n"
        response += f"- **Market Cap**: ${crypto['market_cap']:,.0f}\n"
        response += f"- **24h Volume**: ${crypto['volume_24h']:,.0f}\n\n"
        
        # Performance
        response += "## 📈 Performance\n"
        response += f"- **24h Change**: {crypto['price_change_24h']:+.1f}%\n"
        response += f"- **7d Change**: {crypto['price_change_7d']:+.1f}%\n"
        response += f"- **30d Change**: {crypto['price_change_30d']:+.1f}%\n\n"
        
        # Sustainability & Technology
        response += "## 🌱 Sustainability & Technology\n"
        response += f"- **Energy Consumption**: {crypto['energy_consumption']}\n"
        response += f"- **Consensus Mechanism**: {crypto['consensus_mechanism']}\n"
        response += f"- **Sustainability Score**: {crypto['sustainability_score']}/10\n"
        response += f"- **Technology Maturity**: {crypto['technology_maturity']}/10\n\n"
        
        # Risk Assessment
        response += "## ⚠️ Risk Assessment\n"
        response += f"- **Overall Risk Level**: {crypto['risk_level']}\n"
        response += f"- **Volatility**: {crypto['volatility']}\n"
        response += f"- **Regulatory Clarity**: {crypto['regulatory_clarity']}/10\n"
        response += f"- **Adoption Score**: {crypto['adoption_score']}/10\n\n"
        
        # Use Cases
        response += "## 🎯 Primary Use Cases\n"
        for use_case in crypto['use_cases']:
            response += f"- {use_case}\n"
        response += "\n"
        
        # Investment verdict
        response += f"## 🎯 Investment Verdict (Score: {score}/10)\n"
        response += self._generate_investment_verdict(crypto, score)
        
        return response
    
    def get_market_analysis(self):
        """
        Provide general market analysis and trends.
        """
        response = "# 📊 Cryptocurrency Market Analysis\n\n"
        
        # Market leaders
        top_performers = self._get_top_performers()
        response += "## 🚀 Top Performers (30-day)\n"
        for symbol, crypto in top_performers:
            response += f"- **{crypto['name']}**: {crypto['price_change_30d']:+.1f}%\n"
        response += "\n"
        
        # Market cap analysis
        response += "## 💰 Market Cap Analysis\n"
        large_cap = [c for c in self.crypto_data.values() if c['market_cap'] > 50000000000]
        mid_cap = [c for c in self.crypto_data.values() if 10000000000 <= c['market_cap'] <= 50000000000]
        small_cap = [c for c in self.crypto_data.values() if c['market_cap'] < 10000000000]
        
        response += f"- **Large Cap (>$50B)**: {len(large_cap)} cryptocurrencies\n"
        response += f"- **Mid Cap ($10B-$50B)**: {len(mid_cap)} cryptocurrencies\n"
        response += f"- **Small Cap (<$10B)**: {len(small_cap)} cryptocurrencies\n\n"
        
        # Sustainability trends
        sustainable_cryptos = get_sustainable_cryptos()
        response += "## 🌱 Sustainability Trends\n"
        response += f"**{len(sustainable_cryptos)} cryptocurrencies** have high sustainability scores (7+/10)\n\n"
        response += "**Most Sustainable Options:**\n"
        for symbol, crypto in list(sustainable_cryptos.items())[:3]:
            response += f"- {crypto['name']}: {crypto['sustainability_score']}/10 ({crypto['consensus_mechanism']})\n"
        
        response += "\n## 📈 Market Insights\n"
        response += "- Proof of Stake networks are gaining adoption due to energy efficiency\n"
        response += "- DeFi and smart contract platforms showing strong growth\n"
        response += "- Regulatory clarity is improving for established cryptocurrencies\n"
        response += "- Institutional adoption continues to drive large-cap crypto stability\n"
        
        return response
    
    def get_sustainability_analysis(self):
        """
        Provide analysis focused on sustainable cryptocurrency options.
        """
        sustainable_cryptos = get_sustainable_cryptos()
        
        response = "# 🌱 Sustainable Cryptocurrency Analysis\n\n"
        response += "Environmental impact is increasingly important in crypto investments. Here are the most sustainable options:\n\n"
        
        # Sort by sustainability score
        sorted_sustainable = sorted(sustainable_cryptos.items(), 
                                  key=lambda x: x[1]['sustainability_score'], reverse=True)
        
        for symbol, crypto in sorted_sustainable:
            response += f"## {crypto['name']} ({symbol})\n"
            response += f"**Sustainability Score: {crypto['sustainability_score']}/10**\n\n"
            response += f"- **Consensus**: {crypto['consensus_mechanism']}\n"
            response += f"- **Energy Use**: {crypto['energy_consumption']}\n"
            response += f"- **Market Cap Rank**: #{crypto['market_cap_rank']}\n"
            response += f"- **Why It's Sustainable**: "
            
            if crypto['consensus_mechanism'] == "Proof of Stake":
                response += "Uses Proof of Stake which requires 99%+ less energy than Bitcoin's Proof of Work\n"
            elif "Proof of History" in crypto['consensus_mechanism']:
                response += "Innovative consensus mechanism designed for efficiency and speed\n"
            elif crypto['consensus_mechanism'] == "Stellar Consensus Protocol":
                response += "Custom consensus protocol optimized for energy efficiency and fast settlements\n"
            else:
                response += "Designed with energy efficiency and sustainability in mind\n"
            
            response += "\n"
        
        response += "## 🌍 Why Sustainability Matters\n"
        response += "- **Environmental Impact**: Sustainable cryptos use 99% less energy\n"
        response += "- **Future Regulations**: Governments favor eco-friendly technologies\n"
        response += "- **Corporate Adoption**: Companies prefer sustainable blockchain solutions\n"
        response += "- **Long-term Viability**: Lower operating costs and regulatory risks\n"
        
        return response
    
    def _filter_cryptos_by_risk(self, profile):
        """Filter cryptocurrencies based on risk profile criteria."""
        suitable = {}
        
        for symbol, crypto in self.crypto_data.items():
            # Check market cap rank
            if crypto['market_cap_rank'] > profile['min_market_cap_rank']:
                continue
            
            # Check regulatory clarity
            if crypto['regulatory_clarity'] < profile['min_regulatory_clarity']:
                continue
            
            # Check risk level
            if crypto['risk_level'] not in profile['preferred_risk_levels']:
                continue
            
            suitable[symbol] = crypto
        
        return suitable
    
    def _rank_cryptos(self, cryptos, risk_tolerance):
        """Rank cryptocurrencies based on multiple criteria."""
        ranked = []
        
        for symbol, crypto in cryptos.items():
            score = self._calculate_investment_score(crypto, risk_tolerance)
            ranked.append((symbol, crypto, score))
        
        # Sort by score descending
        ranked.sort(key=lambda x: x[2], reverse=True)
        
        return [(symbol, crypto) for symbol, crypto, score in ranked]
    
    def _calculate_investment_score(self, crypto, risk_tolerance):
        """Calculate investment score based on multiple factors."""
        score = 0
        
        # Market cap rank (higher rank = lower score)
        if crypto['market_cap_rank'] <= 5:
            score += 3
        elif crypto['market_cap_rank'] <= 15:
            score += 2
        else:
            score += 1
        
        # Performance (30-day change)
        if crypto['price_change_30d'] > 20:
            score += 2
        elif crypto['price_change_30d'] > 0:
            score += 1
        
        # Sustainability
        if crypto['sustainability_score'] >= 8:
            score += 2
        elif crypto['sustainability_score'] >= 6:
            score += 1
        
        # Technology maturity
        if crypto['technology_maturity'] >= 8:
            score += 1
        
        # Adoption and regulatory clarity
        score += min(crypto['adoption_score'] // 3, 2)
        score += min(crypto['regulatory_clarity'] // 3, 2)
        
        # Risk adjustment based on tolerance
        if risk_tolerance == "low" and crypto['volatility'] in ["Low", "Medium"]:
            score += 1
        elif risk_tolerance == "high" and crypto['volatility'] == "Very High":
            score += 1
        
        return min(score, 10)  # Cap at 10
    
    def _generate_recommendation_reasoning(self, crypto, risk_tolerance):
        """Generate reasoning for why a crypto is recommended."""
        reasons = []
        
        if crypto['market_cap_rank'] <= 5:
            reasons.append("Top 5 market cap provides stability and liquidity")
        elif crypto['market_cap_rank'] <= 15:
            reasons.append("Established market position with good liquidity")
        
        if crypto['sustainability_score'] >= 8:
            reasons.append("Excellent sustainability profile for long-term viability")
        elif crypto['sustainability_score'] >= 6:
            reasons.append("Good environmental credentials")
        
        if crypto['price_change_30d'] > 15:
            reasons.append("Strong recent performance indicating positive momentum")
        elif crypto['price_change_30d'] > 0:
            reasons.append("Positive price trend over the past month")
        
        if crypto['technology_maturity'] >= 8:
            reasons.append("Mature and battle-tested technology")
        
        if crypto['regulatory_clarity'] >= 7:
            reasons.append("Clear regulatory status reduces compliance risks")
        
        return "- " + "\n- ".join(reasons) if reasons else "Solid fundamentals across multiple metrics"
    
    def _generate_investment_verdict(self, crypto, score):
        """Generate investment verdict based on score."""
        if score >= 8:
            return f"**Strong Buy** - {crypto['name']} shows excellent fundamentals across profitability and sustainability metrics. Well-suited for long-term holding."
        elif score >= 6:
            return f"**Buy** - {crypto['name']} demonstrates solid potential with good balance of risk and return. Consider for portfolio diversification."
        elif score >= 4:
            return f"**Hold/Cautious** - {crypto['name']} has mixed signals. Suitable for experienced investors who understand the risks."
        else:
            return f"**Avoid** - {crypto['name']} shows concerning metrics for conservative investors. High risk with uncertain returns."
    
    def _get_top_performers(self):
        """Get top performing cryptocurrencies by 30-day change."""
        performers = [(symbol, crypto) for symbol, crypto in self.crypto_data.items()]
        performers.sort(key=lambda x: x[1]['price_change_30d'], reverse=True)
        return performers[:5]
    
    def _generate_portfolio_allocation(self, top_cryptos, risk_tolerance):
        """Generate portfolio allocation suggestions."""
        response = "## 💼 Suggested Portfolio Allocation\n\n"
        
        if risk_tolerance == "low":
            response += "**Conservative Portfolio (Low Risk):**\n"
            allocations = [40, 30, 15, 10, 5]
            response += "- Focus on large-cap, established cryptocurrencies\n"
            response += "- Emphasize stability and regulatory clarity\n\n"
        elif risk_tolerance == "medium":
            response += "**Balanced Portfolio (Medium Risk):**\n"
            allocations = [30, 25, 20, 15, 10]
            response += "- Mix of large-cap stability and mid-cap growth potential\n"
            response += "- Balance between safety and opportunity\n\n"
        else:
            response += "**Aggressive Portfolio (High Risk):**\n"
            allocations = [25, 25, 20, 15, 15]
            response += "- Higher allocation to growth-oriented cryptocurrencies\n"
            response += "- Accept higher volatility for potential higher returns\n\n"
        
        for i, (symbol, crypto) in enumerate(top_cryptos):
            if i < len(allocations):
                response += f"- **{crypto['name']} ({symbol})**: {allocations[i]}%\n"
        
        response += "\n**Portfolio Guidelines:**\n"
        response += "- Never invest more than you can afford to lose\n"
        response += "- Rebalance quarterly or when allocations drift >5%\n"
        response += "- Keep some cash reserves for opportunities\n"
        response += "- Consider dollar-cost averaging for entry\n"
        
        return response
