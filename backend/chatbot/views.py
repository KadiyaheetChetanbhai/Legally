from django.http import JsonResponse
from rest_framework.decorators import api_view
from .pinecone_utils import query_legal_cases  # This is your custom utility to query Pinecone
from .llm_utils import embed_text_to_vector  # Function to embed text into vector
from pinecone import Pinecone
from legal_chatbot.settings import PINECONE_API_KEY
import os
# Initialize Pinecone
pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index_name = 'legal-cases'  # Ensure this matches your index

@api_view(['POST'])
def query_legal_info(request):
    """
    Handle a POST request with a legal query and return relevant legal information.
    """
    try:
        # Extract the query text from the request
        query_text = request.data.get('query')
        if not query_text:
            return JsonResponse({'error': 'Query text is required'}, status=400)

        # Embed the query text into a vector
        query_vector = embed_text_to_vector(query_text)

        # Query Pinecone index for similar cases
        response = query_legal_cases(pc, index_name, query_vector)

        # Return the response
        return JsonResponse({'result': response}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
