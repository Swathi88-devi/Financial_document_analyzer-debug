import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import RagTool
from langchain_community.document_loaders import PyPDFLoader

class SearchTool(RagTool):
    name: str = "search_tool"
    description: str = "Placeholder search tool for future web search integration."

    def _run(self, query: str) -> str:
        return "Search functionality is not enabled in this environment."

    async def _arun(self, query: str) -> str:
        return self._run(query)

# Instantiate search tool
search_tool = SearchTool()

class ReadFinancialDocumentTool(RagTool):
    name: str = "read_financial_document"
    description: str = "Reads and returns the text content of a financial PDF document."

    def _run(self, path: str = "data/sample.pdf") -> str:
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for doc in docs:
            content = doc.page_content.strip()
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report

    async def _arun(self, path: str = "data/sample.pdf") -> str:
        return self._run(path)