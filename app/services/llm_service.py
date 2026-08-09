import ollama


class LLMService:

    def __init__(self):
        self.model_name = "llama3.2:3b"

    def generate_answer(
        self,
        question: str,
        context: str
    ) -> str:

        prompt = f"""
You are an AI knowledge assistant.

Answer ONLY using the supplied context.

If the answer is not available in the context,
reply:

"I cannot answer this from the supplied documents."

Context:
---------------------
{context}

Question:
---------------------
{question}

Answer:
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]