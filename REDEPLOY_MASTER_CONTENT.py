import os

def write_cv(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

base = r"e:\000VSCODE PROJECT MULAI DARI DESEMBER 2025\CV KERJA\my-professional-resumes\Master-CVs"

# --- COMMON FRAGMENTS ---
KPI_SOLQ = "- **Architected** a functional non-custodial payment orchestrator bridging Solana assets with Indonesia's **QRIS** national standard; processed **100+ transactions** on Devnet with **0% failure rate**."
KPI_TIKTOK = "- **60,000+ Followers on TikTok**: Cultivated a massive Web3-native reach; driving awareness and scaling creative branding through technical storytelling."
KPI_BMI = "- **Developed MOVV BMI**: High-stability health utility maintained 99.9% crash-free sessions across production deployment on Google Play."

# --- CATEGORY WRITING ---

def build_suite():
    # 01. SOLANA
    write_cv(os.path.join(base, "01-Web3-Solana", "Web3_Solana_ATS_Handle.md"), f"# Web3 Engineer (Solana) | @nayrbryanGaming\n\n## Artifacts\n{KPI_SOLQ}\n- **Proof of Play**: Engineered 100% on-chain game logic for Colosseum Hackathon.\n\n## Impact\n{KPI_TIKTOK}")
    write_cv(os.path.join(base, "01-Web3-Solana", "Web3_Solana_Visual_Handle.md"), f"# @nayrbryanGaming | Solana Battle-Tested Builder\n\n- **SOLQ Builder**: Bridging QRIS to Solana liquidity.\n- **MVP Machine**: 43+ Public repos.\n\n{KPI_TIKTOK}")

    # 02. ETH/BASE
    write_cv(os.path.join(base, "02-Eth-Base", "Eth_Base_ATS_Handle.md"), "# Eth/Base Developer | @nayrbryanGaming\n\n## Artifacts\n- **Basedrop**: Automated airdrop infrastructure for L2 communities.\n- **EscrowKita**: Secure non-custodial escrow protocol on Base Mainnet.\n\n## Experience\n- **Ketua UKM E-Sport**: Digital orchestration for high-engagement tournaments.")
    write_cv(os.path.join(base, "02-Eth-Base", "Eth_Base_Visual_Handle.md"), "# @nayrbryanGaming | Base Ecosystem Architect\n\n- **Escrow Specialist**: Shipping secure logic for trustless trade.\n- **L2 Optimizer**: Focus on Solidity gas efficiency.")

    # 03. MOBILE FLUTTER
    write_cv(os.path.join(base, "03-Mobile-Flutter", "Mobile_Flutter_ATS_RealName.md"), f"# Vincentius Bryan Kwandou | Mobile Application Engineer\n\n## Production Experience\n{KPI_BMI}\n- **NNG Cinema**: Scalable entertainment platform with modular API orchestration.\n\n## Leadership\n- **Ketua UKM E-Sport (Binus)**: Scaling national student gaming infrastructure.")
    write_cv(os.path.join(base, "03-Mobile-Flutter", "Mobile_Flutter_Visual_RealName.md"), "# Vincentius Bryan | Premium Flutter Engineer\n\n- **Mobile Masterpieces**: MOVV BMI & NNG Cinema.\n- **Clean Architecture**: Built for scale and long-term production stability.")

    # 04. AI AUTOMATION
    write_cv(os.path.join(base, "04-AI-Automation", "AI_Automation_ATS_Handle.md"), "# AI Agent Specialist | @nayrbryanGaming\n\n## Artifacts\n- **Botcall-Protocol**: Autonomous API interceptor for cross-chain execution.\n- **X-Autopilot**: Viral engagement agent achieving 60k+ reach.\n\n## Tech\n- **LangChain**, OpenAI, Chainlink CRE.")
    write_cv(os.path.join(base, "04-AI-Automation", "AI_Automation_Visual_Handle.md"), "# @nayrbryanGaming | AI Agent Architect\n\n- **Autonomous Infrastructure**: Building agents that ship artifacts.\n- **Social Scale**: Automating growth for technical ecosystems.")

    # 05. GAMEFI
    write_cv(os.path.join(base, "05-GameFi-Degen", "GameFi_ATS_Handle.md"), "# GameFi Developer | @nayrbryanGaming\n\n## Logic Artifacts\n- **ChainShift**: Procedural graphics explorer on Avalanche.\n- **Proof of Play**: High-throughput on-chain state management for Solana gaming.\n\n## Background\n- **UKM E-Sport Lead**: Competitive ecosystem builder.")
    write_cv(os.path.join(base, "05-GameFi-Degen", "GameFi_Visual_Handle.md"), "# @nayrbryanGaming | GameFi Architect\n\n- **Merging Graphics & Logic**: Three.js meets Anchor Rust.\n- **On-Chain State**: Expert in persistence and metadata orchestration.")

    # 06. COMMUNITY GROWTH
    write_cv(os.path.join(base, "06-Community-Growth", "Community_Growth_ATS_RealName.md"), f"# Vincentius Bryan Kwandou | Community & Growth Lead\n\n## Proven Scale\n{KPI_TIKTOK}\n- **UKM E-Sport Binus**: Scaling the nation's largest student e-sport body.\n\n## Strategy\n- **Engagement Analytics**: Data-driven viral funnel orchestration.")
    write_cv(os.path.join(base, "06-Community-Growth", "Community_Growth_Visual_RealName.md"), "# Vincentius Bryan | Growth Architect\n\n- **0 to 60,000**: Scaling technical trust at high velocity.\n- **Ecosystem Builder**: Architecting communities that ship code.")

    # 07. WEB3 STRATEGY
    write_cv(os.path.join(base, "07-Web3-Strategy", "Web3_Strategy_ATS_Handle.md"), "# Web3 Strategist | @nayrbryanGaming\n\n## Narrative Artifacts\n- **Drip.haus Narrative**: Viral content funnels for Solana communities.\n- **Objkt Curator**: Scaling Tezos L1 adoption via curated storytelling.\n\n## Reach\n- **60k+ Technical Followers** on TikTok.")
    write_cv(os.path.join(base, "07-Web3-Strategy", "Web3_Strategy_Visual_Handle.md"), "# @nayrbryanGaming | Web3 Strategy Lead\n\n- **NFT Storytelling**: Building loyalty through on-chain narrative.\n- **Viral Mechanics**: Understanding the math of engagement.")

    # 08. FINTECH
    write_cv(os.path.join(base, "08-Fintech-Payments", "Fintech_ATS_RealName.md"), f"# Vincentius Bryan Kwandou | Fintech Payments Specialist\n\n## Financial Infrastructure\n{KPI_SOLQ}\n- **WarungPay**: Original QRIS gateway for localized MSMEs.\n\n## Core\n- **Payment Orchestration**: ASPI Standard compliance & Non-custodial logic.")
    write_cv(os.path.join(base, "08-Fintech-Payments", "Fintech_Visual_RealName.md"), "# Vincentius Bryan | Fintech Infrastructure Lead\n\n- **QRIS Specialist**: Bridging Banks to Blockchains.\n- **Battle-Tested Builder**: Shipping national standard payment logic.")

    print("MISSION ACCOMPLISHED: 16-CV MASTER SUITE RE-DEPLOYED.")

if __name__ == "__main__":
    build_suite()
