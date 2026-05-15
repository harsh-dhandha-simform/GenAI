from langchain.chat_models import init_chat_model

model = init_chat_model(
    "google_genai:gemini-2.5-flash",
    max_retries=10,  # Increase for unreliable networks (default: 6)
    timeout=120,  # Seconds; increase for slow connections
)
response = model.invoke("Why do parrots talk?")
print(response.content)