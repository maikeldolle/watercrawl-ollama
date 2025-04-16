from .plugins import OllamaPlugin

__all__ = [
    'OllamaPlugin'
]

__version__ = OllamaPlugin.get_version()
__title__ = OllamaPlugin.get_name()
__description__ = OllamaPlugin.get_description()
__author__ = OllamaPlugin.get_author()
__url__ = "https://github.com/watercrawl/watercrawl-ollama"
