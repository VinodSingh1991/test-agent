"""Setup script for design-system-agent."""
from setuptools import setup, find_packages

setup(
    name="design-system-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.115.0",
        "uvicorn[standard]>=0.32.0",
        "pydantic>=2.9.2",
        "pydantic-settings>=2.6.1",
        "openai>=1.54.4",
        "anthropic>=0.39.0",
        "langchain>=0.3.7",
        "langchain-openai>=0.2.8",
        "langchain-anthropic>=0.3.0",
        "faiss-cpu>=1.9.0",
        "chromadb>=0.5.20",
        "sentence-transformers>=3.3.1",
        "numpy>=2.1.3",
        "pandas>=2.2.3",
        "python-dotenv>=1.0.1",
        "pyyaml>=6.0.2",
        "requests>=2.32.3",
        "loguru>=0.7.3",
    ],
    extras_require={
        "dev": [
            "pytest>=8.3.4",
            "pytest-asyncio>=0.24.0",
            "black>=24.10.0",
            "flake8>=7.1.1",
            "mypy>=1.13.0",
        ]
    },
    python_requires=">=3.11",
)
