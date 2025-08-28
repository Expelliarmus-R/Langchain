from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import GOOGLE_API_KEY
import os


os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1 → Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.NOT ANYTHING OTHER THAN ONE NAME ONLY JUST ONE NAME"
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2 → Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['restaurant_name'],
        template="Suggest 5 popular menu items for {restaurant_name}. Return them as a comma-separated list."
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    # Sequential Chain
    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'menu_items']
    )

    # Run chain
    response = chain({'cuisine': cuisine})

    # Convert menu items to list
    response["menu_items"] = [item.strip() for item in response["menu_items"].split(",")]
    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
