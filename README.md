# Lightweight Zero Trust Architecture (ZTA) Prototype for SMEs

## Overview
This repository contains the proof-of-concept (PoC) implementation of a **lightweight, modular Zero Trust Architecture (ZTA)** framework designed for **small and medium-sized enterprises (SMEs)** operating in resource-constrained environments.  

The prototype integrates:
- **Context-aware access control**
- **Dynamic risk scoring**
- **Policy decision and enforcement using Open Policy Agent (OPA)**

The system is built for **testing and demonstration purposes only**, using synthetic data to avoid exposure of real-world systems or sensitive information.

---

## Objectives
This PoC supports the research goal of evaluating whether simplified ZTA principles can be adapted for SMEs by:
1. Implementing a modular architecture compatible with existing IAM systems.
2. Reducing complexity and overhead compared to traditional ZTA.
3. Testing feasibility via latency, rule enforcement accuracy, and system load metrics.

---

## System Architecture
The prototype consists of the following components:

1. **Flask API Backend**  
   Receives access requests, triggers risk scoring, queries OPA, and returns policy decisions.

2. **Context-Aware Risk Scoring Engine (`risk_engine.py`)**  
   Evaluates access context (user, device, location, behavior) and returns a numerical risk score.

3. **Open Policy Agent (OPA)**  
   Hosts Rego policies that define access control rules based on risk thresholds.

4. **Policy Enforcement Point (PEP)**  
   Integrated into Flask, enforces OPA decisions (`allow`, `deny`, `step_up_auth`).

5. **Synthetic Data Generator / Postman Scripts**  
   Sends simulated access requests for testing.

---

## Requirements
- Python 3.9+
- Flask 2.x
- `requests` library
- Open Policy Agent (OPA) 0.56+
- Postman (optional, for manual testing)

Install Python dependencies:
```bash
pip install -r requirements.txt
