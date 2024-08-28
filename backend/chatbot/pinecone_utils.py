from pinecone import Pinecone
from legal_chatbot.settings import PINECONE_API_KEY


# Set your Pinecone API key
api_key = PINECONE_API_KEY

# Create an instance of the Pinecone class
pc = Pinecone(
    api_key=api_key
)
def query_legal_cases(query_vector, index_name='my-index'):
    """
    Queries the Pinecone index with the given query vector.

    :param query_vector: The vector representation of the query text.
    :param index_name: The name of the Pinecone index to query.
    :return: The top 5 results from the Pinecone index.
    """
    # Ensure the index exists
    if index_name not in [index.name for index in pc.list_indexes()]:
        raise ValueError(f"Index '{index_name}' does not exist.")

    # Connect to the index
    index = pc.index(index_name)

    # Perform the query
    results = index.query(vector=query_vector, top_k=5)

    return results