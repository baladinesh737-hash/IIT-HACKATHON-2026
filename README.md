                                                                                 **IIT Hackathon 2026 – AI-Driven DCA Management System**
 
 # Problem Statement
Debt Collection Agencies (DCAs) handle thousands of overdue cases daily.  
Manual prioritization is inefficient, time-consuming, and often leads to poor recovery rates.

This project introduces an **AI-Driven Debt Collection Management System** that intelligently prioritizes cases so agents can focus on high-impact recoveries first.

# Solution Overview
Our system uses an **AI engine** to automatically analyze overdue cases and classify them into:
- **HIGH Priority**
- **MEDIUM Priority**
- **LOW Priority**
The prioritization is based on intelligent reasoning instead of manual rules, improving operational efficiency and decision-making.

# AI Component
- Uses a **Local Large Language Model (LLM)** for reasoning-based prioritization  
- Generates both:
  - Priority level
  - Human-readable explanation
- Privacy-first design (no external data sharing)

# System Architecture
**Frontend**
- HTML, CSS, JavaScript
- Login interface and case management dashboard

**Backend**
- Python-based APIs
- Modular architecture:
  - Authentication
  - Case management
  - AI prioritization
  - Database handling
    
# Project Structure
├── backend
│ ├── ai_engine.py # AI prioritization logic
│ ├── app.py # Backend API routes
│ ├── auth.py # Authentication module
│ ├── database.py # Database handling
│ └── requirement.txt # Backend dependencies
│
├── frontend
│ ├── index.html # Main dashboard UI
│ ├── lock.html # Login page
│ └── server.js # Frontend logic
│
└── .gitignore

# Key Features
- AI-based intelligent case prioritization
- Clean and user-friendly interface
- Modular and scalable backend
- Privacy-focused local AI processing
- Real-world applicability for financial institutions

# Impact
- Reduces manual workload for agents
- Improves recovery efficiency
- Enables faster decision-making
- Scalable for enterprise-level deployment

# Usage (Conceptual)
1. Agent logs into the system  
2. Overdue case details are submitted  
3. AI engine evaluates the case  
4. Priority and reasoning are generated instantly  

# Hackathon Submission
This project was developed as part of **IIT Hackathon 2026**, focusing on applying AI to solve real-world financial operations challenges.

# Author
**Dinesh Balan**
**Bragalya yazhini**
**Ananda krishnan**
IIT Hackathon 2026 Participant
