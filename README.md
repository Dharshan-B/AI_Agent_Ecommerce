
# AI-Agent SQL Agent with API 

This project is an AI agent that can intelligently respond to natural language questions about your business data. It processes your SQL database, understands questions, generates SQL queries, fetches data, and responds in a human-readable format — optionally visualized with charts.

---

##  Objective

- Create an AI Agent that:
  - Accepts natural language queries through an API.
  - Converts them to SQL queries.
  - Returns answers in a human-readable format.
  - Bonus: Visualize the results using charts.
---

##  Tech Stack

| Component     | Technology Used             |
|---------------|-----------------------------|
| Backend API   | python           |
| Database      | SQLite                      |
| AI/LLM        | Open-source model via `transformers` |
| Visualization | Matplotlib / Seaborn        |
---

## Run it 
uvicorn app:app --reload
---
## Test it 
Using the fastAPI UI Swagger


