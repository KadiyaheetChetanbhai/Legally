from transformers import AutoTokenizer, AutoModel
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

def embed_text_to_vector(text):
    """
    Converts text to a vector using a pre-trained transformer model.

    :param text: A string of text to embed.
    :return: A tensor representing the embedded text.
    """
    # Encode text
    encoded_input = tokenizer(text, padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform mean pooling to get sentence vector
    embeddings = model_output.last_hidden_state
    attention_mask = encoded_input['attention_mask']
    mask_expanded = attention_mask.unsqueeze(-1).expand(embeddings.size()).float()
    sum_embeddings = torch.sum(embeddings * mask_expanded, 1)
    sum_mask = torch.clamp(mask_expanded.sum(1), min=1e-9)
    mean_pooled_embeddings = sum_embeddings / sum_mask

    return mean_pooled_embeddings[0].numpy()  # Return as numpy array for compatibility with Pinecone
