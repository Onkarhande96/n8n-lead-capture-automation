# ⚡ Instant Lead Capture & Multi-Channel Alert Automation (n8n)

## 📌 Project Overview
An end-to-end automation workflow built using **n8n** that intercepts inbound customer leads from web forms or landing pages via Webhooks, normalizes and cleans user contact information, calculates lead qualification scores, logs the record to Google Sheets, and triggers instant alerts to Telegram with one-click WhatsApp response buttons.

---

## 🎯 Business Problem
For service agencies, real estate firms, and coaches:
- **Slow Response Times:** 78% of customers buy from the company that responds first. Delays of 2–3 hours drastically reduce conversion rates.
- **Manual Data Entry:** Sales teams waste time manually copying details from email notifications into spreadsheets.
- **Unqualified Leads:** Sales reps don't know who has a high budget versus who needs basic consultation.

---

## 🛠️ Workflow Architecture
```text
[ Website Form / Webhook ]
           │
           ▼
[ Transform & Score Lead (n8n Code Node) ]
   ├── Clean & Capitalize Name
   ├── Format Phone to Country Code (+91)
   ├── Evaluate Budget & Assign Priority (High 🔥 / Medium ⚡ / Standard 📌)
   └── Generate 1-Click WhatsApp Direct Chat Link
           │
           ├──────────────────────────────┐
           ▼                              ▼
[ Google Sheets: Append Row ]   [ Telegram / Slack: Instant Alert ]
  (Permanent CRM Database)       (Notification with 1-Click Action)
```

---

## 💡 Key Features & Logic
1. **Intelligent Normalization:**
   - Strips erratic whitespace from customer names and applies Title Case (`vikas jadhav` ➔ `Vikas Jadhav`).
   - Normalizes phone numbers by removing spaces/hyphens and guaranteeing the `+91` country prefix.
2. **Dynamic Lead Scoring:**
   - **High Priority 🔥:** Budgets $\ge$ ₹30,000 / $500
   - **Medium Priority ⚡:** Budgets between ₹15,000 and ₹29,999
   - **Standard Lead 📌:** Budgets $<$ ₹15,000
3. **Frictionless Sales Outreach:**
   - Generates a pre-filled `https://wa.me/` link inside the Telegram alert. The salesperson can tap one button on their phone and immediately open a chat with the lead without manually saving their contact number!

---

## 📁 Repository Structure
```text
├── workflow.json                  # Importable n8n workflow file
├── simulate_workflow.py           # Offline execution & testing script
├── processed_leads_output.json    # JSON results of processed sample leads
└── README.md                      # Detailed technical & business case study
```

---

## 🚀 How to Import into n8n
1. Open your n8n workspace (cloud or local self-hosted `n8n start`).
2. Click **Add Workflow** ➔ **Import from File...**
3. Select `workflow.json`.
4. Connect your Google Sheets credential and Telegram Bot Token.
5. Toggle **Active** to start receiving live leads!
