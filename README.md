# EduChain MCP Server (Claude Desktop Integration)

This project is a Python-based MCP-compatible server that integrates the [EduChain](https://github.com/satvik314/educhain) educational content generation library with Claude Desktop.

It exposes the following tools via HTTP endpoints:

- `/generate_mcqs` – Generate multiple-choice questions
- `/generate_lesson_plan` – Generate a detailed lesson plan
- `/generate_flashcards` – Generate topic-specific flashcards (bonus)

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/abanindra3/educhain-mcp.git
cd educhain-mcp
