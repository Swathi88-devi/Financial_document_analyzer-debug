# Financial Document Analyzer – Debug Assignment

## Project Overview

I worked on a **Financial Document Analyzer** that processes corporate reports, financial statements, and investment documents using **AI-powered analysis agents built with CrewAI and FastAPI**.

The original codebase was intentionally buggy and incomplete.  
My task was to **identify deterministic bugs, fix them, improve inefficient prompts, and make the system fully functional**.

---

##  Assignment Objective

- Debug the existing codebase  
- Fix all deterministic bugs  
- Improve inefficient prompts  
- Ensure the application runs correctly  
- Provide clear documentation  

---

## Bugs Found and How I Fixed Them

### 1.Incorrect CrewAI Imports
**Bug:**  
The project imported `Agent` from `crewai.agents`, which caused an `ImportError`.

**Fix:**  
I corrected the import to use `Agent` and `LLM` directly from `crewai`.

---

### 2️. Invalid Tool Implementations
**Bug:**  
Tools were implemented as raw Python functions, which caused **Pydantic validation errors** in CrewAI.

**Fix:**  
I rewrote all tools using `BaseTool` from `crewai_tools`, making them compatible with CrewAI.

---

### 3️. Library Version Mismatch
**Bug:**  
The code referenced unsupported components such as `SerperDevTool` and decorators not available in the installed versions.

**Fix:**  
I replaced unsupported components with version-compatible implementations while keeping the add-on structure intact.

---

### 4️. PDF Reading Failure
**Bug:**  
The application could not properly read PDF documents.

**Fix:**  
I integrated `PyPDFLoader` from `langchain-community` to reliably extract text from financial documents.

---

### 5️. HTTP 405 Method Not Allowed Error
**Bug:**  
Accessing `/analyze` using a browser returned `405 Method Not Allowed`.

**Reason:**  
The endpoint is intentionally designed to accept **POST requests only**.

**Fix:**  
No code change was required. I documented this behavior clearly and used Swagger UI for correct usage.

---

### 6️.Missing API Key Configuration
**Bug:**  
CrewAI requires an external LLM API key, but no key was provided.

**Fix:**  
I configured the project to load the API key securely using environment variables and documented this dependency.

---

### 7️. Dependency Installation Issue
**Bug:**  
Some dependencies failed to install correctly using `requirements.txt` alone.

**Reason:**  
Version conflicts and platform-specific binaries (especially `onnxruntime`).

**Fix:**  
I installed critical packages separately to ensure a stable environment.

---

## Prompt Improvements

**Problem:**  
The original prompts allowed speculation and hallucinated financial data.

**Changes Made:**  
- Enforced document-only analysis  
- Removed speculative instructions  
- Required structured and factual outputs  

This improved reliability and accuracy.

---

##  Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt

# Install required packages separately
pip install onnxruntime==1.20.0
pip install fastapi uvicorn
pip install crewai-tools
pip install langchain-community
```
How to Run the Application

Start the FastAPI server using:
```bash
uvicorn main:app --reload
```
The application will run at:
```url
http://127.0.0.1:8000
```
