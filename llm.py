from dotenv import dotenv_values, load_dotenv
from openai import OpenAI
from pydantic_models import ResponseType
from ollama import chat
import json


def printFormat(data: str):
    print(("-"*15) + (data) + ("-"*15))

def useOpenAI(descriptionByUser):
    printFormat("Using OpenAI")
    load_dotenv()
    openai_api_key = dotenv_values().get("OPENAI_API_KEY")
    client = OpenAI(api_key=openai_api_key)

    response = client.responses.parse(
        model="gpt-4o-mini",
        input=[
                {
                    "role": "system",
                    "content": "You are an expert front-end and back-end engineer."
                },
                {
                    "role": "user",
                    "content": "Give me the code for this <userDescription>"+descriptionByUser+"</userDescription> If the desciption is vague, generate own description and then generate code. ScriptToRun should be returned like \"command\": \"python\", \"flags\": \"\", \"file\":\"fileName\" "
                 }
        ],
        text_format=ResponseType
    )
    return response.output[0].content[0].parsed

def useLocalModel(llm, descriptionByUser):
    printFormat("Using ollama")

    response = chat(
        messages=[
            {
                "role": "system",
                "content": "You are an expert backend engineer."
            },
            {
                    "role": "user",
                    "content": "Give me the code for this <userDescription>"+descriptionByUser+"</userDescription> If the desciption is vague, generate own description and then generate code. ScriptToRun should be returned like \"command\": \"python\", \"flags\": \"\", \"file\":\"fileName\" "
            }
        ],
        model=llm,
        format=ResponseType.model_json_schema()
    )

    if (response.message.content != None    ):
        answer = json.loads(response.message.content)
        return answer
    else:
        print("No response from the model")
        return None

def getProject(llmChoice, descriptionByUser):
    if llmChoice == "OpenAI":
        result = useOpenAI(descriptionByUser)

        print (result)
        title = result.title
        description = result.description
        repoName = result.repoName
        files = result.files
        scriptToRun = result.scriptToRun
        libraries = result.libraries
        return title, description, repoName, files, scriptToRun, libraries

    else:
        if (llmChoice == "Codellama"):
            llm = "codellama:latest"
        elif llmChoice == "Qwen2.5-Coder":
            llm = "qwen2.5-coder:latest"
        elif llmChoice == "Starcoder2":
            llm = "starcoder2:15b"
        result = useLocalModel(llm, descriptionByUser)
        title = result["title"]
        description = result["description"]
        repoName = result["repoName"]
        files = result["files"]
        scriptToRun = result["scriptToRun"]
        libraries = result["libraries"]
        return title, description, repoName, files, scriptToRun, libraries
