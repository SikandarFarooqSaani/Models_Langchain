# LangChain Learning Journey 🚀

> **Note:** This README was generated via a custom AI prompt to easily and clearly document my learning progress for myself and any future readers.

Welcome to my LangChain learning repository! This project documents my initial steps into the world of Large Language Models (LLMs), embeddings, and vector similarity using the LangChain framework. I focused primarily on open-source and free-tier models to build a solid foundational understanding.

## 📋 Table of Contents
1. [Prerequisites & Setup](#-prerequisites--setup)
2. [Module 1: Chat Models (Google Gemini)](#module-1-chat-models-google-gemini)
3. [Module 2: Chat Models (Hugging Face)](#module-2-chat-models-hugging-face)
4. [Module 3: Embedding Models](#module-3-embedding-models)
5. [Mini-Project: Document Similarity App](#mini-project-document-similarity-app)

---

## 🛠 Prerequisites & Setup

To run the scripts in this project, you need to set up your environment variables. We use `python-dotenv` to keep API keys secure. 

Create a `.env` file in the root directory of the project and add your API keys. **The variable names must exactly match the following:**


## Module 1: Chat Models (Google Gemini)
**File:** `llmdemo.py`

My journey started with exploring text generation models. While there are many closed-source and open-source models, I utilized Google's Generative AI for an accessible, high-quality starting point.

*   **Implementation:** I imported `ChatGoogleGenerativeAI` and initialized the `gemini-2.5-flash` model.
*   **The Temperature Variable:** I experimented with the `temperature` parameter, setting it to `0.7`.
*   **Concept:** Temperature controls the model's creativity. It ranges from `0` to `2`. A value of `0` makes the output deterministic and highly predictable, while a value closer to `2` makes it highly creative and random.
*   **Result:** Successfully invoked the LLM and printed the generated content.

---

## Module 2: Chat Models (Hugging Face)
**File:** *(Hugging Face implementation)*

To explore alternative free-to-use models, I integrated Hugging Face's powerful open-source ecosystem.

*   **Implementation:** Used `ChatHuggingFace` and `HuggingFaceEndpoint`.
*   **Model:** Configured the endpoint using the repository ID for a DeepSeek model.
*   **Task:** Set the execution task specifically to `text-generation`.
*   **Result:** Invoked the model and successfully printed the results. This proved to be a fantastic, cost-effective alternative to paid APIs.

---

## Module 3: Embedding Models
Embeddings translate text into numerical vectors, which is crucial for AI to understand semantic meaning. I experimented with both paid and free embedding models.

### 1. OpenAI Embeddings (Paid)
**File:** `docs.py`

*   Imported `OpenAIEmbeddings`.
*   Configured the model with a specific dimension size of `32` to optimize the vector size.
*   Successfully embedded documents to view their vector representations.

### 2. Hugging Face Embeddings (Free)
**File:** `huggingface.py`

*   Imported `HuggingFaceEmbeddings`.
*   Declared the embedding model and utilized the `embedding.embed_query(text)` method.
*   Printed the resulting embedding vector, proving that high-quality embeddings can be generated locally/freely.

---

## 🎯 Mini-Project: Document Similarity App
To tie everything together, I built a small application to find semantic similarities between different texts. This uses the math of vectors to see how "close" two pieces of text are in meaning.

**Workflow:**

1.  **Importing Tools:** Imported `cosine_similarity` from `sklearn.metrics.pairwise`.
2.  **Generating Vectors:** Declared the embedding model and generated:
    *   Document Embeddings (a list of texts to search through).
    *   A Query Embedding (the text I want to find matches for).
3.  **Calculating Similarity:** Passed the query vector and document vectors into the `cosine_similarity` function to generate a score for each document.
4.  **Sorting & Output:**
    *   Used a combination of `enumerate` to keep track of the document indices.
    *   Sorted the results using a lambda function (`key=lambda x: x[1]`) based on the highest similarity scores.
    *   Printed the original document index alongside its similarity score to cleanly display which document was the closest match to the query.

*Happy Coding! 🚀*

```env
