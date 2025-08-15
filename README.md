# 🛠️ Product Feedback Analyzer  
** ⚠️ Project currently under development**

Product Feedback Analyzer is a project that automates the **scraping of negative reviews** (1–2 stars) from e-commerce platforms, then leverages **OpenAI's GPT-4o** to **analyze recurring issues** and suggest **concrete product improvements**.

This project simulates an **automated market study**, identifying what customers dislike about a product to help design a better version.

---

## ✨ Features

* **🔐 Automated Amazon login** using Playwright (with saved session).
* 🔍 Multi-platform search – retrieves a product reference from Cdiscount, then automatically searches for the same product on Amazon.
* **📄 Smart scraping** of 1-star reviews across multiple Amazon and Cdiscount pages.
* 📦 Structured storage – saves reviews in a hashmap for fast processing.
* **🔎 Text extraction** from negative user feedback.
* **📊 AI-powered review analysis** via GPT-4o.
* **💡 Auto-generated product improvement suggestions** based on common complaints.
* **✅ Automated testing** of the scraper with Pytest.

---

## 🛠 Tech Stack

Feedback Analyzer is powered by a modern Python stack focused on AI and automation:

### Back-end (Scraping + AI Analysis)

* **Playwright (async)**: Browser automation and dynamic scraping.
* **Pytest**: Unit and functional testing for the scraping logic.
* **OpenAI GPT-4o**: Interprets customer feedback and proposes improvements.
* **Python-dotenv**: Secures API keys via `.env` file.
* **AsyncIO**: Ensures high-performance asynchronous scraping.

---

### (Current) Workflow:

1. The user provides a Cdiscount product URL.
2. The scraper:
   * Retrieves the product reference from Cdiscount.
   * Collects negative reviews from Cdiscount.
3. The scraper opens Amazon:
   * Pastes the product reference into the search bar.
   * Selects the matching product.
   * Scrapes negative reviews from Amazon.
4. All reviews (Cdiscount + Amazon) are stored in a hashmap.
5. Reviews are sent to GPT-4o for:
   * Identifying recurring issues.
   * Generating improvement suggestions.
6. Results are displayed to the user.

---

## 🧠 Project goal

### This project was created to:

1. Learn how to scrape real-world dynamic web content  
2. Combine automation + AI to solve a practical problem  
3. Build a portfolio project simulating an automated market research tool  
4. Experiment with sentiment analysis and AI-powered summarization  
