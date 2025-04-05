from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str="TO be added later")

agent = project_client.agents.get_agent("String to be added later ")

thread = project_client.agents.get_thread("TO be added later")

message = project_client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="Hi tours&activities"
)

run = project_client.agents.create_and_process_run(
    thread_id=thread.id,
    assistant_id=agent.id)
messages = project_client.agents.list_messages(thread_id=thread.id)

for text_message in messages.text_messages:
    print(text_message.as_dict())
