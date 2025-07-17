from art import text2art
from InquirerPy import inquirer
from file_utils import setupProjectFolder, createFile, addMetadata
from github_utils import doGitStuff
from llm import getProject
import subprocess

def main():
    print(text2art("Genisys", font="tarty1"))
    llmChoice = inquirer.select(
        "What AI would you like to use?",
        choices=[
            'OpenAI',
            'Codellama',
            'StarCoder2',
            'Qwen2.5-Coder'
        ],
        default="Qwen2.5-Coder"
    ).execute()

    setupProjectFolder()

    userChoice = inquirer.select(
        "Would you like to explain the project?",
    choices=[
        "Yes",
        "No, let ai decide."
    ],
    default="No, let ai decide."
    ).execute()

    if userChoice == "Yes":
        descriptionByUser = inquirer.text(
            "Give the description here: "
        ).execute()
    else:
        descriptionByUser = "Generate a python script that prints first 100 prime numbers using the Sieve of Eratosthenes algorithm"
    
    (title, description, repoName, files, scriptToRun, libraries)  = getProject(llmChoice, descriptionByUser)

    if not files:
        raise Exception("No files found.")

    for file in files:
        createFile(file, llmChoice)
    addMetadata(title, description, scriptToRun, llmChoice)

    if (llmChoice == "OpenAI"):
        command = scriptToRun.command
        flags = scriptToRun.flags
        file = scriptToRun.file
    else:
        command = scriptToRun["command"]
        flags = scriptToRun["flags"]
        file = scriptToRun["file"]

    askToRunScript = inquirer.select(
        "Would you like to run this script?\n"+command+" "+flags+" "+file,
        choices=[
            "Yes",
            "No"
        ],
        default="No"
    ).execute()

    if askToRunScript == "Yes":
        if flags:
            scriptResult = subprocess.run([command.replace("python","python3"), flags, file], cwd="project", capture_output=True, text=True)
        else:
            scriptResult = subprocess.run([command.replace("python","python3"), file], cwd="project", capture_output=True, text=True)
        print("This was the result of script:\n"+scriptResult.stdout)

    wantGithub = inquirer.select(
        "Would you like to connect to GitHub?",
        choices=[
            "Yes, Connect to GitHub",
            "No"
        ],
        # default="Yes, Connect to GitHub"
        default="No"
    ).execute()

    if wantGithub == "Yes, Connect to GitHub":
        print("Genisys would like to create this repo: ", title)
        doGitStuff(title, repoName, description)



if __name__ == "__main__":
    main()