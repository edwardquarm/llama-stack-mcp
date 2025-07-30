from llama_stack_client import LlamaStackClient

PROMPT = "Say Hello"

client = LlamaStackClient(base_url="http://localhost:8321")

response = client.inference.chat_completion(
    messages = [{"role": "user", "content": PROMPT}],
    model_id=client.models.list()[0].identifier, # NOTE: this is the first model (and currently only model as per the run.yml) that the server can access
)

print(response.completion_message.content)