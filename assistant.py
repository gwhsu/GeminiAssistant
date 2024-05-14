# assistant.py

import google.generativeai as genai
import config


class Assistant:
    def __init__(self):
        genai.configure(api_key=config.Gemini_api_key)

        # Set up the model
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                           generation_config=generation_config,
                                           safety_settings=safety_settings)

        self.convo = self.model.start_chat(history=[])

    def ask_question(self, question):
        self.convo.send_message(question)
        return self.convo.last.text
