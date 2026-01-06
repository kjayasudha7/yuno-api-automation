# yuno-api-automation
## Yuno API Automation Framework

### Tech Stack

* Python 3.10+
* Behave (BDD)
* Requests

### Installation

bash
pip install -r requirements.txt

# Yuno API Automation – Framework Documentation
## This document describes the design, architecture, and execution flow of the Yuno API Automation framework.
### Architecture
• Feature Layer – Gherkin scenarios
• Step Definition Layer – Python implementation
• Utility Layer – API client, headers, payloads
• Validation Layer – centralized assertions


### Environment Variables

bash
export PUBLIC_API_KEY=xxxxx
export PRIVATE_SECRET_KEY=xxxxx
export ACCOUNT_ID=xxxxx


### Execute Tests

bash
behave


### Run Specific Feature

bash
behave features/purchase.feature


# Yuno API Automation — Test Data Design & CI Guide

## 📌 Overview
This repository contains the **Yuno API Automation Framework**, built using **Python + Behave (BDD)** for validating payment, authorization, refund, and capture flows.

This README documents:
- Test data design strategy  
- Governance & best practices  
- Negative testing approach  
- Utilities (data loader, dynamic data, Excel→JSON)  
- CI/CD integration with **GitHub Actions**

---

# Test Data Design Goals

| Goal | Description |
|------|-------------|
| Reusability | Same data across scenarios |
| Maintainability | Centralized data changes |
| Traceability | Data maps to business flows |
| Security | No secrets or PII |
| Automation-ready | CI/CD compatible |

---

# 2. Folder Structure


