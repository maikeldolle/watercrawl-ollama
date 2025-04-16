from watercrawl_plugin import get_settings

OLLAMA_BASE_URL = get_settings('OLLAMA_BASE_URL', 'http://localhost:11434')
EXTRACT_SYSTEM_PROMPT = get_settings('EXTRACT_SYSTEM_PROMPT', None)
