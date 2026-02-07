"""
LLM Factory for OpenAI Models

MODEL CONFIGURATION:
-------------------
Default: gpt-4o-mini (recommended for production)
- Fast, cost-efficient model from OpenAI
- Excellent for structured output & function calling
- Perfect for well-defined layout generation tasks

Alternative Models (set via OPENAI_MODEL env var):
- gpt-4o-mini    : Default - best balance (recommended)
- gpt-4o         : Most capable, 4x cost (use for complex queries)
- gpt-4-turbo    : Legacy high-performance model
- gpt-3.5-turbo  : Fastest, cheapest (basic queries only)

Environment Variables:
- OPENAI_API_KEY  : Required for API access
- OPENAI_MODEL    : Optional model override (default: gpt-4o-mini)

Example:
    export OPENAI_MODEL=gpt-3.5-turbo  # Use fastest model
    export OPENAI_MODEL=gpt-4o         # Use most capable model
"""
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.language_models.fake_chat_models import FakeListChatModel
import os
from loguru import logger
from langchain_core.output_parsers import JsonOutputParser


def get_mock_llm():
    """Get a LangChain-compatible mock LLM for testing."""
    # Mock responses for different node types
    responses = [
        # Normalized query response
        "show my notifications",
        
        # Query analysis response (JSON)
        """{
            "intent": "show_notifications",
            "components_needed": ["title", "description"],
            "data_type": "dynamic",
            "action_required": "display",
            "complexity": "simple",
            "confidence": 0.9
        }""",
        
        # Task planning response (JSON)
        """{
            "plan_summary": "Display notifications with title and description",
            "tasks": [
                {
                    "task_id": "task_1",
                    "task_type": "select_pattern",
                    "description": "Select title_description pattern",
                    "parameters": {"pattern": "title_description"},
                    "priority": 1
                },
                {
                    "task_id": "task_2",
                    "task_type": "extract_content",
                    "description": "Extract notification content",
                    "parameters": {},
                    "priority": 2
                },
                {
                    "task_id": "task_3",
                    "task_type": "generate_layout",
                    "description": "Generate layout using builder pattern",
                    "parameters": {},
                    "priority": 3
                },
                {
                    "task_id": "task_4",
                    "task_type": "validate_output",
                    "description": "Validate generated layout",
                    "parameters": {},
                    "priority": 4
                }
            ],
            "estimated_complexity": "simple"
        }"""
    ] * 10  # Repeat for multiple queries
    
    return FakeListChatModel(responses=responses)


class LLMFactory:
    @classmethod
    def open_ai(cls, max_tokens: int = 10000, model: str = None):
        """
        Create OpenAI LLM instance
        
        Args:
            max_tokens: Maximum tokens for completion (default 10000)
            model: Model name (default: gpt-4o-mini)
                   Options: gpt-4o-mini (recommended), gpt-4o (most capable), 
                           gpt-4-turbo, gpt-3.5-turbo (fastest)
        """
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "":
            logger.warning("OPENAI_API_KEY not set. Using mock LLM client.")
            return get_mock_llm()
        
        # Use environment variable for model selection, fallback to default
        default_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        model_name = model or default_model
        
        try:
            return ChatOpenAI(
                model=model_name,
                temperature=0,
                max_tokens=max_tokens,
                openai_api_key=api_key
            )
        except Exception as e:
            logger.error(f"Error creating OpenAI client with model {model_name}: {e}. Using mock client.")
            return get_mock_llm()

    @classmethod
    def open_ai_structured_llm(cls, structured_output=None, max_tokens: int = 10000, model: str = None):
        """
        Create OpenAI LLM instance with structured output using Pydantic model
        
        Args:
            structured_output: Pydantic model class for structured output
            max_tokens: Maximum tokens for completion (default 10000)
            model: Model name (default: gpt-4o-mini)
                   Options: gpt-4o-mini (recommended), gpt-4o (most capable), 
                           gpt-4-turbo, gpt-3.5-turbo (fastest)
        """
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "":
            logger.warning("OPENAI_API_KEY not set. Using mock LLM client.")
            return get_mock_llm()
        
        # Use environment variable for model selection, fallback to default
        default_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        model_name = model or default_model
        
        try:
            # Create base LLM
            base_llm = ChatOpenAI(
                model=model_name,
                temperature=0,
                max_tokens=max_tokens,
                openai_api_key=api_key
            )
            
            # Add structured output if provided
            if structured_output:
                return base_llm.with_structured_output(structured_output)
            
            return base_llm
            
        except Exception as e:
            logger.error(f"Error creating OpenAI structured client with model {model_name}: {e}. Using mock client.")
            return get_mock_llm()

    @classmethod
    def open_ai_embeddings(cls):
        return OpenAIEmbeddings(
            model="text-embedding-3-large",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    @classmethod
    def open_ai_pydantic_llm(cls, pydantic_model, max_tokens: int = 2048):
        """
        Create OpenAI LLM instance with Pydantic output parser
        Args:
            pydantic_model: Pydantic model class for structured output
            max_tokens: Maximum tokens for completion (default 2048)
        Returns:
            LLM chain with enforced Pydantic output
        """
        llm = cls.open_ai(max_tokens=max_tokens)
        parser = JsonOutputParser(pydantic_object=pydantic_model)
        return llm | parser

