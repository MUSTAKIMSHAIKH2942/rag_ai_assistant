# from transformers import pipeline

# def get_generator():
#     # Using a more recent model that's suitable for Q&A
#     return pipeline(
#         "text2text-generation",
#         model="google/flan-t5-small",
#         device=-1  # Use CPU (-1), change to 0 for GPU if available
#     )

# def generate_answer(retrieved_text, query):
#     generator = get_generator()
#     prompt = f"Question: {query}\nContext: {retrieved_text}\nAnswer:"
#     generated_text = generator(
#         prompt,
#         max_length=200,
#         num_return_sequences=1,
#         temperature=0.7
#     )
#     return generated_text[0]['generated_text']


# generate_answer.py
from transformers import pipeline

def get_generator():
    # Using distilBERT model for faster Q&A
    return pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad",
        tokenizer="distilbert-base-cased-distilled-squad",
        device=-1  # Running on CPU
    )

def generate_answer(context, query):
    generator = get_generator()
    result = generator(question=query, context=context)
    return result['answer']
