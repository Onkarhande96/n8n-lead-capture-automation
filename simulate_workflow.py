"""
Lead Automation Simulator & Test Suite
Demonstrates the exact business logic and execution results of the n8n workflow.
"""
import json
import re
from datetime import datetime

SAMPLE_RAW_LEADS = [
    {
        "name": "  vikas jadhav  ",
        "email": "VIKAS.J@EXAMPLE.COM ",
        "phone": "9823456789",
        "service": "E-Commerce Website Development",
        "budget": 45000
    },
    {
        "name": "sneha shinde",
        "email": "sneha.shinde@business.in",
        "phone": "+91 91234 56780",
        "service": "Social Media Marketing",
        "budget": 12000
    },
    {
        "name": "RAJESH KHANNA",
        "email": "rajesh@khannatraders.com",
        "phone": "8877665544",
        "service": "Automation Workflow Setup",
        "budget": 25000
    }
]

def transform_lead(raw):
    # 1. Clean Name
    name = raw.get("name", "Valued Lead").strip().title()
    
    # 2. Clean Email & Phone
    email = raw.get("email", "").strip().lower()
    clean_digits = re.sub(r"[^0-9]", "", str(raw.get("phone", "")))
    phone = f"91{clean_digits}" if len(clean_digits) == 10 else clean_digits
    
    # 3. Budget & Priority Score
    budget = int(raw.get("budget", 0))
    if budget >= 30000:
        priority = "HIGH PRIORITY 🔥"
    elif budget >= 15000:
        priority = "Medium Priority ⚡"
    else:
        priority = "Standard Lead 📌"
        
    lead_id = f"LD-{int(datetime.now().timestamp() * 1000) % 1000000:06d}"
    received_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    whatsapp_url = f"https://wa.me/{phone}?text=Hello%20{name},%20we%20received%20your%20inquiry%20regarding%20{raw.get('service')}."

    return {
        "lead_id": lead_id,
        "name": name,
        "email": email,
        "phone": f"+{phone}",
        "service": raw.get("service"),
        "budget": f"₹{budget:,}",
        "priority": priority,
        "received_at": received_at,
        "whatsapp_one_click": whatsapp_url
    }

def run_simulation():
    print("=" * 65)
    print(" 🚀 n8n LEAD AUTOMATION ENGINE - EXECUTION LOG")
    print("=" * 65)
    
    processed = []
    for i, lead in enumerate(SAMPLE_RAW_LEADS, 1):
        clean = transform_lead(lead)
        processed.append(clean)
        
        print(f"\n[Lead #{i}] Received from Webhook:")
        print(f"  • Raw Input: Name='{lead['name']}', Phone='{lead['phone']}', Budget={lead['budget']}")
        print(f"  • Processed Lead ID: {clean['lead_id']}")
        print(f"  • Normalized Name:  {clean['name']}")
        print(f"  • Priority Rating:  {clean['priority']}")
        print(f"  • Direct WhatsApp:  {clean['whatsapp_one_click']}")
        print(f"  --> Action 1: Appended to Google Sheets ('Leads' tab)")
        print(f"  --> Action 2: Sent Telegram Alert with 1-Click WhatsApp Button")
        
    with open("processed_leads_output.json", "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 65)
    print("✅ All leads processed and saved to 'processed_leads_output.json'")
    print("=" * 65)

if __name__ == "__main__":
    run_simulation()
