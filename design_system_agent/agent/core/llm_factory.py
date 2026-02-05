from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.language_models.fake_chat_models import FakeListChatModel
import os
from loguru import logger


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
    def open_ai(cls):
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key or api_key == "":
            logger.warning("OPENAI_API_KEY not set. Using mock LLM client.")
            return get_mock_llm()
        
        try:
            return ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0,
                max_tokens=1024,
                openai_api_key=api_key
            )
        except Exception as e:
            logger.error(f"Error creating OpenAI client: {e}. Using mock client.")
            return get_mock_llm()

    @classmethod
    def open_ai_structured_llm(cls, structured_output=None):
        return ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0,
            max_tokens=1024,
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            structured_output=structured_output
        )

    @classmethod
    def open_ai_embeddings(cls):
        return OpenAIEmbeddings(
            model="text-embedding-3-large",
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        
        