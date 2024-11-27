import openai
from myapp.search import search_documents, call_large_model
import logging
from config import OPENAI_INSTRUCTIONS_IN_GERMAN

def get_ai_result(query):
    search_results = search_documents(query)
    logging.info(f'Search Results: {search_results}')
    if not search_results:
        return "No documents found"
    instructions = f"Bitte nennen Sie mir relevante Kandidaten gemäß dieser Frage und stellen Sie sicher, dass Sie Kandidaten aufgrund ihrer Berufserfahrung auswählen, die sich auf Folgendes bezieht"
    query_context = ''
    for result in search_results:
        content = result['content']
        query_context += f"Question: {query}\n```\nCANDIDATE Addres_Id: {result['Adress_Id']}\nRELATED CONTENT CANDIDATE: {content}\n```\n"
    # Prepare messages for OpenAI API
    messages = [
        {"role": "system", "content": f"INSTRUCTIONS:\n{instructions}\nEND OF INSTRUCTIONS\nCONTENT:\n{query_context}\nEND OF CONTENT\FORMAT INSTRUCTION: {OPENAI_INSTRUCTIONS_IN_GERMAN}\nEND OF FORMAT INSTRUCTION"},
    ] 
    try:
        result = call_large_model(messages)
    except openai.OpenAIError as e:
        return "Error communicating with OpenAI"
    return result
