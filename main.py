from langchain.llms import Ollama
from  dotenv import load_dotenv
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()

def generate_pet_name():
    llm = Ollama(
        model="mistral",
        num_gpu=120,
        temperature=0,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        verbose=False
        )

    name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")
    
    return name

if __name__ == "__main__":
    print(generate_pet_name())