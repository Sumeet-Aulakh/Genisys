import os
import subprocess
import shutil
from pydantic_models import FileType, ScriptType

def setupProjectFolder():
    if (os.path.exists("project")):
        shutil.rmtree("project");
    print("Making the git project repository")
    os.mkdir("project")
    subprocess.run(["git", "init"], cwd="project", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["ls", "-alt"], cwd="project", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def addMetadata(title: str, description: str, scriptToRun: ScriptType, llmChoice: str):
    if (llmChoice == "OpenAI"):
        command = scriptToRun.command
        flags = scriptToRun.flags
        file = scriptToRun.file
    else:
        command = scriptToRun["command"]
        flags = scriptToRun["flags"]
        file = scriptToRun["file"]
    with open("project/readme.md", "w") as f:
        f.write(f"""# 🚀 {title}

<div align="center">

![Genisys](https://img.shields.io/badge/Generated%20by-Genisys%20AI-blue?style=for-the-badge&logo=robot)
![Status](https://img.shields.io/badge/Status-Ready%20to%20Use-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

## 📖 Description

{description}

## ⚡ Quick Start

Run the following command to get started:

```bash
{command} {flags} {file}
```

## 🛠️ Prerequisites

Make sure you have the required dependencies installed before running the project.

## 📁 Project Structure

```
📦 {title.lower().replace(' ', '-')}
├── 📄 README.md (this file)
├── 🐍 main scripts
└── 📚 dependencies
```

## 🤖 About Genisys

> **Genisys** is an AI-powered project generator that creates complete projects with code, structure, and documentation based on your requirements.

### ✨ Features
- 🎯 **Intelligent Generation**: Creates projects tailored to your needs
- 📝 **Auto Documentation**: Generates comprehensive README files
- 🔧 **Ready-to-Run**: Projects work out of the box
- 🎨 **Multiple AI Models**: Choose from OpenAI, Codellama, StarCoder2, or Qwen2.5-Coder

### 🔗 Links
- **Repository**: [Genisys on GitHub](https://github.com/Sumeet-Aulakh/Genisys)
- **Documentation**: Check the main repo for detailed usage instructions

## 🚀 Getting Started

1. **Clone or download** this generated project
2. **Install dependencies** (if any)
3. **Run the main script** using the command above
4. **Customize** as needed for your specific requirements

## 📝 Notes

- ✅ This project was **automatically generated** by Genisys AI
- 🔄 You can **regenerate** this project anytime with Genisys
- ✏️ Feel free to **modify and extend** the code as needed
- 🐛 If you encounter issues, try regenerating with more specific requirements

## 🤝 Contributing

This is a generated project, but feel free to:
- 🐛 Report issues
- 💡 Suggest improvements  
- 🔧 Submit pull requests
- ⭐ Star the [Genisys repository](https://github.com/Sumeet-Aulakh/Genisys)

---

<div align="center">

**Made with ❤️ by [Genisys AI](https://github.com/Sumeet-Aulakh/Genisys)**

*Happy Coding! ��*

</div>
""")

def createFile(file: FileType, llmChoice: str):
    if (llmChoice == "OpenAI"):
        location = "project/" + file.name
        if not str(file.name.find(".")):
            location = "project/" + file.name+ "." + file.extension
        with open(location, "w") as f:
            f.write(file.content)
    else:
        location = "project/"+file["name"]
        if not str(file["name"]).find("."):
            location = "project/"+file["name"]+"."+file["extension"]
        with open(location,"w") as f:
            f.write(file["content"])
