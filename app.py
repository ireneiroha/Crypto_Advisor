import streamlit as st
import pandas as pd
from crypto_data import get_crypto_data, get_market_trends
from advisor_logic import CryptoAdvisor
from education import get_educational_content, get_risk_explanation

# Page configuration
st.set_page_config(
    page_title="Crypto Investment Advisor",
    page_icon="₿",
    layout="wide"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_stage" not in st.session_state:
    st.session_state.conversation_stage = "greeting"
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}
if "advisor" not in st.session_state:
    st.session_state.advisor = CryptoAdvisor()

def initialize_chat():
    """Initialize chat with welcome message"""
    if not st.session_state.messages:
        welcome_msg = """
        👋 Welcome to your Cryptocurrency Investment Advisor!
        
        I'm here to help beginners understand cryptocurrency investments based on:
        • 📈 **Profitability metrics** (price trends, market cap)
        • 🌱 **Sustainability factors** (energy consumption, long-term viability)
        
        **Important Disclaimer**: This is for educational purposes only. Always do your own research and never invest more than you can afford to lose.
        
        How can I help you today? You can ask me about:
        - Specific cryptocurrencies
        - Investment recommendations based on your risk tolerance
        - Basic cryptocurrency education
        - Market trends and analysis
        """
        st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

def process_user_input(user_input):
    """Process user input and generate appropriate response"""
    advisor = st.session_state.advisor
    user_input_lower = user_input.lower()
    
    # Educational queries
    if any(word in user_input_lower for word in ["what is", "explain", "help", "learn", "beginner"]):
        if "bitcoin" in user_input_lower or "btc" in user_input_lower:
            return get_educational_content("bitcoin")
        elif "ethereum" in user_input_lower or "eth" in user_input_lower:
            return get_educational_content("ethereum")
        elif "risk" in user_input_lower:
            return get_risk_explanation()
        else:
            return get_educational_content("general")
    
    # Investment recommendations
    elif any(word in user_input_lower for word in ["recommend", "invest", "buy", "portfolio", "suggestion"]):
        return handle_investment_query(user_input_lower, advisor)
    
    # Specific cryptocurrency queries
    elif any(crypto in user_input_lower for crypto in ["bitcoin", "btc", "ethereum", "eth", "cardano", "ada", "solana", "sol", "polygon", "matic", "chainlink", "link", "polkadot", "dot", "litecoin", "ltc", "avalanche", "avax", "stellar", "xlm"]):
        return handle_crypto_specific_query(user_input_lower, advisor)
    
    # Market analysis
    elif any(word in user_input_lower for word in ["market", "trend", "analysis", "performance"]):
        return advisor.get_market_analysis()
    
    # Sustainability queries
    elif any(word in user_input_lower for word in ["green", "sustainable", "energy", "environment", "eco"]):
        return advisor.get_sustainability_analysis()
    
    # Default response
    else:
        return """
        I can help you with:
        
        🎓 **Education**: Ask me to explain cryptocurrencies, risks, or specific coins
        📊 **Recommendations**: Ask for investment suggestions based on your risk tolerance
        🔍 **Analysis**: Ask about specific cryptocurrencies or market trends
        🌱 **Sustainability**: Ask about eco-friendly crypto options
        
        Try asking something like:
        - "What is Bitcoin?"
        - "Recommend some cryptocurrencies for a beginner"
        - "Which cryptos are most sustainable?"
        - "What are the risks of crypto investing?"
        """

def handle_investment_query(user_input, advisor):
    """Handle investment recommendation queries"""
    risk_tolerance = "medium"  # default
    
    if any(word in user_input for word in ["conservative", "safe", "low risk", "careful"]):
        risk_tolerance = "low"
    elif any(word in user_input for word in ["aggressive", "high risk", "risky"]):
        risk_tolerance = "high"
    
    return advisor.get_investment_recommendations(risk_tolerance)

def handle_crypto_specific_query(user_input, advisor):
    """Handle queries about specific cryptocurrencies"""
    crypto_map = {
        "bitcoin": "BTC", "btc": "BTC",
        "ethereum": "ETH", "eth": "ETH",
        "cardano": "ADA", "ada": "ADA",
        "solana": "SOL", "sol": "SOL",
        "polygon": "MATIC", "matic": "MATIC",
        "chainlink": "LINK", "link": "LINK",
        "polkadot": "DOT", "dot": "DOT",
        "litecoin": "LTC", "ltc": "LTC",
        "avalanche": "AVAX", "avax": "AVAX",
        "stellar": "XLM", "xlm": "XLM"
    }
    
    for name, symbol in crypto_map.items():
        if name in user_input:
            return advisor.analyze_specific_crypto(symbol)
    
    return "I couldn't identify which cryptocurrency you're asking about. Please try again with a specific name like 'Bitcoin' or 'Ethereum'."

# Main app layout
st.title("₿ Cryptocurrency Investment Advisor")
st.markdown("*Your beginner-friendly guide to crypto investments*")

# Sidebar with educational resources
with st.sidebar:
    st.header("📚 Quick Education")
    
    with st.expander("🚀 Crypto Basics"):
        st.markdown("""
        **Cryptocurrency** is digital money secured by cryptography.
        
        **Key Concepts:**
        - **Market Cap**: Total value of all coins
        - **Volatility**: Price fluctuation frequency
        - **Blockchain**: Technology behind crypto
        - **Wallet**: Storage for your crypto
        """)
    
    with st.expander("⚠️ Investment Risks"):
        st.markdown("""
        **High Volatility**: Prices can change rapidly
        
        **Regulatory Risk**: Laws may change
        
        **Technology Risk**: Technical failures possible
        
        **Market Risk**: Overall market downturns
        
        **Never invest more than you can afford to lose!**
        """)
    
    with st.expander("🌱 Sustainability Info"):
        st.markdown("""
        **Energy Consumption**: Some cryptos use more energy
        
        **Proof of Work**: Bitcoin, Litecoin (high energy)
        
        **Proof of Stake**: Ethereum, Cardano (low energy)
        
        **Green Alternatives**: Focus on eco-friendly options
        """)
    
    st.header("📊 Market Overview")
    trends = get_market_trends()
    for trend in trends:
        if trend["change"] > 0:
            st.success(f"{trend['category']}: +{trend['change']:.1f}%")
        else:
            st.error(f"{trend['category']}: {trend['change']:.1f}%")

# Initialize chat
initialize_chat()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me about cryptocurrency investments..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            response = process_user_input(prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# Footer with disclaimer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; font-size: 0.8em;'>
⚠️ <strong>Important Disclaimer</strong>: This chatbot provides educational information only. 
Cryptocurrency investments are highly risky and volatile. Always consult with a financial advisor 
and do your own research before making investment decisions. Past performance does not guarantee future results.
</div>
""", unsafe_allow_html=True)
