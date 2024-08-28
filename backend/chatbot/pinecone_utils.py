import pinecone
from legal_chatbot.settings import PINECONE_API_KEY, PINECONE_ENV
from langchain.embeddings import HuggingFaceEmbeddings

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
index = pinecone.Index("legal-knowledge")

# Embeddings model (use the same one for querying and storing)
embeddings_model = HuggingFaceEmbeddings(model_name="lisa/legal-bert-squad-law")

# Store legal cases in Pinecone
def store_legal_case(case_text, case_id):
    embedding = embeddings_model(case_text)
    index.upsert(vectors=[{"id": case_id, "values": embedding}])

# Query Pinecone for relevant legal cases
def query_legal_cases(query_text):
    query_embedding = embeddings_model(query_text)
    results = index.query(queries=[query_embedding], top_k=5)
    return results
