import React, { useState } from "react";
import axios from "axios";

function LegalChatbot() {
    const [query, setQuery] = useState("");
    const [response, setResponse] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const res = await axios.post("http://localhost:8000/api/query/", { query });
            setResponse(res.data);
        } catch (error) {
            console.error("Error fetching response", error);
        }
    };

    return (
        <div>
            <h1>Legal Chatbot</h1>
            <form onSubmit={handleSubmit}>
                <input 
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    placeholder="Ask your legal question"
                />
                <button type="submit">Submit</button>
            </form>
            {response && (
                <div>
                    <h2>Response</h2>
                    <p>{response.llm_response}</p>
                    <h3>Relevant Laws</h3>
                    <pre>{JSON.stringify(response.pinecone_results, null, 2)}</pre>
                </div>
            )}
        </div>
    );
}

export default LegalChatbot;
