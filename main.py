def main():
    print("Hello from genai!")

import os
from getpass import getpass

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_PROJECT"] = "learning"

if __name__ == "__main__":
    main()
