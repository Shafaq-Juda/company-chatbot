from pathlib import Path
import math

from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load company policies
policy_file = Path(__file__).parent / "policies.txt"
policy_text = policy_file.read_text(encoding="utf-8")

# 2. Split policies into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=30
)

documents = splitter.split_documents([
    Document(page_content=policy_text)
])

# 3. Set up the embedding model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# 4. Create embeddings for policy documents
print("Preparing policy search...")
document_vectors = embeddings.embed_documents(
    [doc.page_content for doc in documents]
)
print("Policy search is ready!")

# 5. Connect to the answer-generation model
llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0
)

# Calculate cosine similarity between two vectors
def cosine_similarity(a, b):
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


# 6. Retrieve the most relevant policy
def retrieve_policy(question):
    question_vector = embeddings.embed_query(question)

    scores = [
        cosine_similarity(question_vector, vector)
        for vector in document_vectors
    ]

    best_index = max(range(len(scores)), key=lambda i: scores[i])
    best_score = scores[best_index]

    print(f"[Retrieval similarity: {best_score:.3f}]")

    # Basic relevance threshold; needs testing on real questions
    if best_score < 0.35:
        return None

    return documents[best_index].page_content


# 7. Chat with the RAG assistant
print("================================")
print("   COMPANY POLICY CHATBOT - RAG")
print("================================")
print("Ask me about company policies.")
print("Type 'exit' to quit.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    if not question:
        continue

    relevant_policy = retrieve_policy(question)

    if relevant_policy is None:
        print("\nAssistant: I don't know based on the available policies.")
        continue

    messages = [
        SystemMessage(
            content=(
                "You are a company policy assistant. "
                "Answer using only the retrieved policy below. "
                "If the policy does not contain the answer, "
                "say you don't know. Never invent company policies.\n\n"
                "Retrieved policy:\n"
                + relevant_policy
            )
        ),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)
    print("\nAssistant:", response.content)