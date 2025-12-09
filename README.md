#  Safe Code Executor

A secure sandbox system that runs **Python** and **JavaScript (Node.js)** inside Docker containers with:

- Timeout protection  
- Memory limit  
- No network access  
- Read-only filesystem  
- Clean UI with code editor & history  

---

##  1. Installation & Running the Server

### 1 Clone repository
```bash
git clone https://github.com/MALGIREDDY/safe-code-executor.git
cd safe-code-executor
2) Create virtual environment
bash
Copy code
python -m venv venv
.\venv\Scripts\activate
3) Install Flask
bash
Copy code
pip install flask
4) Run the server
bash
Copy code
python app.py
Expected output:

nginx
Copy code
Running on http://127.0.0.1:5000
 2. Testing Normal Code Execution
 Hello World
powershell
Copy code
(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"print(\"Hello World\")"}').output
Output:

nginx
Copy code
Hello World
 Python Math
powershell
Copy code
(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"x=5+3\nprint(x)"}').output
Output:

Copy code
8
 Python Loop
powershell
Copy code
(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"for i in range(5):\n    print(i)"}').output
Output:

Copy code
0
1
2
3
4
 3. Security Tests (Expected Behavior)
 Infinite Loop
python
Copy code
while True:
    pass
Output:

pgsql
Copy code
Execution timed out after 10 seconds
 Memory Bomb
python
Copy code
x = "a" * 1000000000
Output:

css
Copy code
(no output, container killed)
 Network Access Block
python
Copy code
import requests
requests.get("http://google.com")
Output:

vbnet
Copy code
ModuleNotFoundError: No module named 'requests'
 Reading /etc/passwd (Allowed inside container)
python
Copy code
with open("/etc/passwd") as f:
    print(f.read())
Output example:

ruby
Copy code
root:x:0:0:root:/root:/bin/bash
...
 File Write Block (because of --read-only)
python
Copy code
with open("/tmp/hack.txt", "w") as f:
    f.write("hello")
Output:

pgsql
Copy code
OSError: [Errno 30] Read-only file system
 JavaScript Test
 console.log Test
powershell
Copy code
(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"javascript","code":"console.log(2+2);"}').output
Output:

Copy code
4
 UI Info
CodeMirror editor

Python/JS dropdown

Output section

History of last 10 runs

Open UI:

arduino
Copy code
double-click index.html
 Author
Saideep Malgireddy
GitHub: https://github.com/MALGIREDDY