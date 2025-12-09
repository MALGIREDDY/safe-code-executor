# Safe Code Executor

A simple, sandboxed web-based code executor that lets users run Python or JavaScript (Node.js) code safely inside Docker containers.

##  Features

- Run **Python** and **JavaScript (Node.js)** code via a single API.  
- Sandbox using Docker with these security limits:
  -  Execution timeout (10 seconds)  
  -  Memory limit (128 MB)  
  -  CPU limit (0.5 vCPU)  
  -  No network access (`--network none`)  
  -  Read-only filesystem inside the container  
- Web UI (browser) with:
  - Code editor powered by **CodeMirror** (syntax highlighting, line numbers)  
  - Language selector (Python / JavaScript)  
  - Output display  
  - Execution history (last 10 runs stored in browser)  

## How to Run Locally

1. Clone the repo  
   ```bash
   git clone https://github.com/MALGIREDDY/safe-code-executor.git
   cd safe-code-executor
(Recommended) Create and activate a Python virtual environment

python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
# or
source venv/bin/activate      # Linux / macOS


Install requirements

pip install flask


Make sure Docker Desktop (or Docker Engine) is running.

Start the server

python app.py


Open index.html in your browser (double-click or open file).

Write your Python or JavaScript code in the editor.

Select the language.

Click RUN.

See output and check history of previous runs.

 Example API Calls (using PowerShell)

Python example

irm http://127.0.0.1:5000/run -Method POST -ContentType "application/json" `
-Body '{"language":"python","code":"print(\"Hello, world!\")"}'


JavaScript example

irm http://127.0.0.1:5000/run -Method POST -ContentType "application/json" `
-Body '{"language":"javascript","code":"console.log(2+2);"}'

 Security Measures Implemented
Feature	Reason / Benefit
10-second timeout	Prevent infinite loops / hanging scripts
128 MB memory limit	Prevent memory bombs / excessive memory usage
0.5 CPU limit (optional)	Prevent CPU hogging by heavy calculations
No network (--network none)	Block external HTTP, DNS, network-based attacks
Read-only filesystem	Prevent malicious file writes inside container
Temporary script dir (user’s home)	Easy Docker volume mount on Windows + Linux
Code-length limit (≤5000 chars)	Avoid extremely large payloads or abuse
 What Docker Protects From — and Its Limits

Protected

Access to host filesystem (only container FS accessible)

Infinite loops, memory bombs, network attacks

File writes inside container

 What Docker does not guarantee

Kernel-level vulnerabilities or container escape attacks

Resource exhaustion if many containers run concurrently

Persistence beyond container lifetime (all state is ephemeral)

 What I Learned

How to run untrusted code inside containers safely

Why and how to apply resource limits: CPU, memory, time, network, filesystem

Difference between sandbox-level security vs host-level security

How to integrate Docker sandbox + REST API + web UI for user code execution

 How to Use / Demo

Run normal code successfully (Python or JS).

Try malicious code — infinite loop, memory bomb, network call, file-writing — and observe it fails safely.

Switch language, run again.

Use the web UI; see execution history; review output.

 Future Improvements

Support for multiple files / project uploads (.zip)

Syntax highlighting themes / dark mode support

Rate limiting / user authentication

Container pooling / concurrency support

Running containers as non-root users / custom seccomp profile

 Author

Your Name  M SAIDEEP
Repository: safe-code-executor