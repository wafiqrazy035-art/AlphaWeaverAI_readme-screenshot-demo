import time
import logging
import random

# === UPDATED DEMO LOGIC FOR ALPHAWEAVER AI ===
# Menunjukkan kemampuan teknik tingkat lanjut:
# 1. Resilience: Penanganan Error 521 (Cloudflare)
# 2. Deep Learning: Pre-processing data untuk PriceTransformer
# 3. Reinforcement Learning: Mekanisme Reward untuk PPO Agent
# 4. Experience Replay: Simulasi Memory Bank (Dyna-Style)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("AlphaWeaver_Professional_Demo")

class AlphaLearningEngine:
    """Mendemonstrasikan bagaimana AI belajar dari kesalahan dan keberhasilan."""
    
    def calculate_reward(self, pnl, trade_duration, volatility):
        """Logika inti Reinforcement Learning untuk melatih PPO Agent."""
        reward = 0
        # Reward positif untuk profit
        if pnl > 0:
            reward += 2.0 
        # Penalti untuk kerugian (Loss)
        elif pnl < 0:
            reward -= 2.5 
            
        # Penalti efisiensi jika terlalu lama menahan posisi tanpa profit
        if trade_duration > 10 and pnl <= 0:
            reward -= 0.5
            
        return reward

class MarketDataProcessor:
    """Menunjukkan cara normalisasi data sebelum masuk ke model Transformer."""
    
    def prepare_transformer_input(self, raw_data):
        try:
            # Normalisasi harga agar model fokus pada pola pergerakan, bukan nilai nominal
            base_price = raw_data[0]
            processed = [x / base_price for x in raw_data]
            logger.info("Transformer Data Normalization: SUCCESS")
            return processed
        except Exception as e:
            logger.error(f"Data Processing Error: {e}")
            return None

class ConnectionManager:
    """Solusi untuk masalah infrastruktur seperti Cloudflare 521."""
    
    def connect_with_retry(self, api_call_func, max_retries=3):
        for attempt in range(max_retries):
            try:
                # Simulasi pemanggilan API bursa (WEEX/Indodax)
                result = api_call_func()
                logger.info("API Connection: ESTABLISHED")
                return result
            except Exception as e:
                if "521" in str(e):
                    logger.warning(f"Attempt {attempt+1}: Cloudflare 521 Detected. Retrying in 2s...")
                    time.sleep(2)
                else:
                    logger.error(f"Critical Connection Error: {e}")
                    break
        return None

if __name__ == "__main__":
    print("=== ALPHAWEAVER AI: UPDATED TECHNICAL DEMO ===")
    
    # 1. Demo Penanganan Error (Engineering Skill)
    conn = ConnectionManager()
    def mock_521_error(): raise Exception("Error 521: Web Server is Down")
    print("\n[1] Testing Connection Resilience:")
    conn.connect_with_retry(mock_521_error)
    
    # 2. Demo Pre-processing (Deep Learning Skill)
    processor = MarketDataProcessor()
    sample_prices = [1500000000, 1510000000, 1505000000]
    print(f"\n[2] Testing Transformer Pre-processing:")
    print(f"Input: {sample_prices} -> Output: {processor.prepare_transformer_input(sample_prices)}")
    
    # 3. Demo Reward Logic (Reinforcement Learning Skill)
    learner = AlphaLearningEngine()
    print("\n[3] Testing Reinforcement Learning Reward:")
    print(f"Scenario Profit: Reward {learner.calculate_reward(0.05, 2, 0.01)}")
    print(f"Scenario Loss  : Reward {learner.calculate_reward(-0.02, 5, 0.01)}")