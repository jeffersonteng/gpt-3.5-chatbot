# Python

class Obnoxious_Agent:
    def __init__(self, client) -> None:
        print('init obnoxious')
        return
        # TODO: Initialize the client and prompt for the Obnoxious_Agent

    def set_prompt(self, prompt):
        return
        # TODO: Set the prompt for the Obnoxious_Agent

    def extract_action(self, response) -> bool:
        return true
        # TODO: Extract the action from the response

    def check_query(self, query):
        return true
        # TODO: Check if the query is obnoxious or not


# class Query_Agent:
#     def __init__(self, pinecone_index, openai_client, embeddings) -> None:
#         # TODO: Initialize the Query_Agent agent

#     def query_vector_store(self, query, k=5):
#         # TODO: Query the Pinecone vector store

#     def set_prompt(self, prompt):
#         # TODO: Set the prompt for the Query_Agent agent

#     def extract_action(self, response, query = None):
#         # TODO: Extract the action from the response


# class Answering_Agent:
#     def __init__(self, openai_client) -> None:
#         # TODO: Initialize the Answering_Agent

#     def generate_response(self, query, docs, conv_history, k=5):
#         # TODO: Generate a response to the user's query


# class Relevant_Documents_Agent:
#     def __init__(self, openai_client) -> None:
#         # TODO: Initialize the Relevant_Documents_Agent

#     def get_relevance(self, conversation) -> str:
#         # TODO: Get if the returned documents are relevant


# class Head_Agent:
#     def __init__(self, openai_key, pinecone_key, pinecone_index_name) -> None:
#         # TODO: Initialize the Head_Agent

#     def setup_sub_agents(self):
#         # TODO: Setup the sub-agents

#     def main_loop(self):
#         # TODO: Run the main loop for the chatbot