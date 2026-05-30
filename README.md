# DevAssist: AI-Powered Developer Assistant

A lightweight, extensible CLI tool to automate developer workflows with natural language commands.

## Features
- **Error Explanation:** Analyze terminal errors and suggest fixes.
- **Documentation Lookup:** Fetch docs for libraries/frameworks.
- **Code Search:** Search local codebases for functions, variables, or patterns.
- **Web Search:** Query Stack Overflow, GitHub issues, or official docs.
- **Plugin System:** Extend with custom commands (e.g., Docker, Kubernetes).

## Installation
```bash
pip install devassist
```

## Usage
```bash
devassist "Explain this Python error: NameError: name 'requests' is not defined"
devassist "Find docs for Python's `asyncio`"
devassist "Search my codebase for 'def authenticate'"
```

## Roadmap
- [ ] Core CLI with natural language processing.
- [ ] Local codebase search (ripgrep/ast).
- [ ] Web search integration (Stack Overflow, GitHub).
- [ ] Plugin system for extensibility.

## License
MIT