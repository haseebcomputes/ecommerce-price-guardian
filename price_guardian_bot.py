# =====================================================================
# PROJECT 1: THE E-COMMERCE GLOBAL PRICE GUARDIAN BOT (PREMIUM PRODUCTION)
# DEVELOPER: J. HASEEB
# =====================================================================

print("=" * 65)
print("--- LAUNCHING ENGINE: ENTERPRISE PRICE GUARDIAN MASTER v3.0 ---")
print("=" * 65 + "\n")

# Global Financial Parameter Configuration
USD_TO_PKR_EXCHANGE_RATE = 278.00

# Strict Product Inventory Configuration
product_inventory_config = {
    "prod_001": {
        "product_title": "Apple MacBook Pro M3",
        "original_market_price_usd": 1615.00,
        "target_alert_price_usd": 1470.00,
        "client_routing_email": "client.alpha@globaltech.com",
    },
    "prod_002": {
        "product_title": "Sony WH-1000XM5 Headphones",
        "original_market_price_usd": 340.00,
        "target_alert_price_usd": 305.00,
        "client_routing_email": "user.beta@remotework.io",
    },
    "prod_003": {
        "product_title": "Samsung Galaxy S24 Ultra",
        "original_market_price_usd": 1365.00,
        "target_alert_price_usd": 1255.00,
        "client_routing_email": "manager.delta@cloudsystems.com",
    },
}

# LIVE MARKET PRICE STREAM SIMULATION (Simulated Incoming Server Data)
live_market_price_stream = {
    "prod_001": 1399.00,  # CRASHED: Below Target $1470 -> Trigger Alert!
    "prod_002": 320.00,  # DROPPED: But still above target $305 -> Stay Stable!
    "prod_003": 1199.00,  # CRASHED: Below Target $1255 -> Trigger Alert!
}

print("[STATUS]: Enterprise Schema Verified Stable.")
print("[STATUS]: Core Looping & Decision Execution Matrix Active...\n")

# Processing, Validation & Decision Engine Loop
for product_id, configrutation in product_inventory_config.items():
    title = configrutation.get("product_title")
    prise_usd = configrutation.get("original_market_price_usd")
    target_prise = configrutation.get("target_alert_price_usd")
    client_email = configrutation.get("client_routing_email")

    # Input Type Validation Guards
    if not title or prise_usd is None or target_prise is None or not client_email:
        print(f"[SECURITY ERROR]: Node {product_id} missing critical data. Skipping.")
        continue

    valid_numaric_type = (int, float)
    if (
        isinstance(prise_usd, bool)
        or not isinstance(prise_usd, valid_numaric_type)
        or isinstance(target_prise, bool)
        or not isinstance(target_prise, valid_numaric_type)
    ):
        print(
            f"[DATA CORRUPTION ERROR]: Node {product_id} formatting invalid. Skipping."
        )
        continue

    if prise_usd <= 0 or target_prise <= 0:
        print(
            f"[BUSINESS LOGIC ERROR]: Node {product_id} contains negative metrics. Skipping."
        )
        continue

    # Currency Conversion Module
    prise_pkr = prise_usd * USD_TO_PKR_EXCHANGE_RATE
    target_prise_pkr = target_prise * USD_TO_PKR_EXCHANGE_RATE

    print(f"-> Active Tracking ID : {product_id} | {title}")
    print(f"   Original Baseline  : ${prise_usd:,.2f} USD  |  Rs. {prise_pkr:,.2f} PKR")
    print(
        f"   Target Threshold   : ${target_prise:,.2f} USD  |  Rs. {target_prise_pkr:,.2f} PKR"
    )

    # Extract Live Price Stream Data
    live_price_usd = live_market_price_stream.get(product_id)

    # AUTOMATED DECISION & ALERT DISPATCH ENGINE
    if live_price_usd is not None:
        live_price_pkr = live_price_usd * USD_TO_PKR_EXCHANGE_RATE
        print(
            f"   [LIVE MARKET VALUE]: Currently Trading At ${live_price_usd:,.2f} USD (Rs. {live_price_pkr:,.2f} PKR)"
        )

        # Checking if the current market price hit the client's threshold
        if live_price_usd <= target_prise:
            price_drop_usd = prise_usd - live_price_usd
            price_drop_pkr = price_drop_usd * USD_TO_PKR_EXCHANGE_RATE
            discount_percentage = (price_drop_usd / prise_usd) * 100

            print(
                f"   🚨 [CRITICAL ALERT]: Price dropped by {discount_percentage:.1f}% OFF! (${price_drop_usd:,.2f} USD saved)"
            )
            print(f"   📧 [DISPATCH STATUS]: Triggering Automated Email Protocol...")
            print(
                f"   >> SENT TO [{client_email}]: 'Deal Alert! {title} crashed to ${live_price_usd:,.2f} USD!'"
            )
        else:
            # Case where price dropped but didn't hit target threshold
            print(
                f"   ✅ [STABLE]: Asset dropped, but has not crossed target threshold yet. No alert dispatched."
            )
    else:
        print(
            f"   ⚠️ [CONNECTION ERROR]: Live stream data for {product_id} is unavailable."
        )

    print("-" * 65)
