from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

load_dotenv()


def run():
    """ The Initializer for this application.
    """
    generate_pet_name("cat", "black")

def generate_pet_name(animal_type, pet_color):
    """Generates a pet name based on Mistral 7B

    Args:
        animal_type (str): The animal type. ie, cat, dog, cow
        pet_color (str): The color of your animal

    Returns:
        str: List of names for your pet.
    """

    llm = Ollama(
        model="mistral",
        num_gpu=120,
        temperature=0,
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        verbose=False
        )

    prompt_template_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color}. Suggest me five cool names for my pet."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name)
    
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return response

# Main
if __name__ == "__main__":
    run()