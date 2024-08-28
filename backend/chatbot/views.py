
from rest_framework.decorators import api_view
from rest_framework.response import Response
from langchain.llms import HuggingFaceLLM
import pinecone
from .llm_utils import process_legal_query
from .pinecone_utils import query_legal_cases
from legal_chatbot.settings import PINECONE_API_KEY, PINECONE_ENV



# Initialize Pinecone and LangChain
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pinecone.Index("legal-knowledge")

# Define LLaMA model via HuggingFace (you can replace this with your model)
llm = HuggingFaceLLM(model_name="lisa/legal-bert-squad-law")

@api_view(['POST'])
def legal_query(request):
    user_query = request.data.get("query", "")
    
    # Process the query using LLaMA via LangChain
    llm_response = process_legal_query(user_query)
    
    # Query Pinecone for related legal cases
    pinecone_results = query_legal_cases(user_query)
    
    return Response({
        "llm_response": llm_response,
        "pinecone_results": pinecone_results
    })
