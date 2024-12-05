
from transformers import MarianMTModel, MarianTokenizer
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class TranslationService:
    _instance = None

    def __new__(cls):
        """Singleton pattern to ensure only one instance of the model is loaded"""
        if cls._instance is None:
            cls._instance = super(TranslationService, cls).__new__(cls)
            try:
                cls._instance.model_name = 'Helsinki-NLP/opus-mt-en-fr'
                cls._instance.tokenizer = MarianTokenizer.from_pretrained(
                    cls._instance.model_name)
                cls._instance.model = MarianMTModel.from_pretrained(
                    cls._instance.model_name)
                logger.info(f"Translation service initialized with model: {
                            cls._instance.model_name}")
            except Exception as e:
                logger.error(
                    f"Failed to initialize translation service: {str(e)}")
                raise
        return cls._instance

    def translate_to_french(self, text: str) -> dict:
        """
        Translate given text to French

        Args:
            text (str): Text to translate

        Returns:
            dict: Dictionary containing status and either translated text or error message
        """
        if not text:
            return {
                'success': False,
                'error': 'No text provided for translation'
            }

        try:
            inputs = self.tokenizer(text, return_tensors="pt", padding=True)
            outputs = self.model.generate(**inputs)
            translated_text = self.tokenizer.decode(
                outputs[0], skip_special_tokens=True)

            return {
                'success': True,
                'translated_text': translated_text
            }

        except Exception as e:
            logger.error(f"Translation error: {str(e)}")
            return {
                'success': False,
                'error': f'Translation failed: {str(e)}'
            }

    def is_healthy(self) -> bool:
        """Check if the translation service is functioning properly"""
        try:
            test_translation = self.translate_to_french("Hello")
            return test_translation.get('success', False)
        except Exception:
            return False
