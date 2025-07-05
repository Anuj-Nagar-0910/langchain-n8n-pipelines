# 🔗 LangChain + n8n Pipelines

This project demonstrates a real-world automation workflow using **LangChain + n8n** to extract text from documents and generate questions from it using OpenAI.

---

## 🚀 Use Case

Automatically process files (PDF, TXT, CSV, MD, HTML) using `n8n`, extract their content, and send it to a **LangChain question generator pipeline**.

---

## 🔄 Workflow Steps

1. Upload a document to `n8n`
2. Use file parser (e.g., `Read Binary File`)
3. Clean and structure the text
4. Send the content to LangChain via `HTTP Request`
5. Get a list of generated questions

---

## 📁 Files

- `langchain_blocks/` – Contains reusable LangChain chains
- `workflows/` – Contains `n8n` workflow JSON for importing

---

## 🛠️ Setup

1. Set your API key in `.env`
2. Run LangChain server or script (optional)
3. Import `gpt-question-generator.json` into `n8n`
4. Test with a text file input

---

## 📬 Contact

Questions? Ideas? Reach out on GitHub!
