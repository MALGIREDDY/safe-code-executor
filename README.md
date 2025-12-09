<h1>🚀 Safe Code Executor</h1>
<p>A secure sandbox system that runs <strong>Python</strong> and <strong>JavaScript (Node.js)</strong> inside Docker containers with:</p>

<ul>
    <li>Timeout protection</li>
    <li>Memory limit</li>
    <li>No network access</li>
    <li>Read-only filesystem</li>
    <li>Clean UI with code editor & history</li>
</ul>

<hr>

<div class="section">
<h2>🛠 1. Installation & Running the Server</h2>

<h3>1️⃣ Clone repository</h3>
<pre>git clone https://github.com/MALGIREDDY/safe-code-executor.git
cd safe-code-executor</pre>

<h3>2️⃣ Create virtual environment</h3>
<pre>python -m venv venv
.\venv\Scripts\activate</pre>

<h3>3️⃣ Install Flask</h3>
<pre>pip install flask</pre>

<h3>4️⃣ Run the server</h3>
<pre>python app.py</pre>

<h3>Expected server output:</h3>
<pre>* Running on http://127.0.0.1:5000</pre>
</div>

<hr>

<div class="section">
<h2>🧪 2. Testing Normal Code Execution (with real outputs)</h2>

<h3>✔ Test 1 — Hello World</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST -ContentType "application/json" `
-Body '{"language":"python","code":"print(\"Hello World\")"}').output</pre>

<b>Expected Output:</b>
<pre>Hello World</pre>

<h3>✔ Test 2 — Python Math</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST -ContentType "application/json" `
-Body '{"language":"python","code":"x=5+3\nprint(x)"}').output</pre>

<b>Expected Output:</b>
<pre>8</pre>

<h3>✔ Test 3 — Python Loop</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST -ContentType "application/json" `
-Body '{"language":"python","code":"for i in range(5):\n    print(i)"}').output</pre>

<b>Expected Output:</b>
<pre>0
1
2
3
4</pre>
</div>

<hr>

<div class="section">
<h2>🔥 3. Security Tests (with expected outputs)</h2>

<h3>❌ Infinite Loop Attack</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"while True:\n    pass"}').output</pre>

<b>Expected:</b>
<pre>Execution timed out after 10 seconds</pre>

<h3>❌ Memory Bomb Attack</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"x = \"a\" * 1000000000"}').output</pre>

<b>Expected:</b>
<pre>(No output — container killed due to memory limit)</pre>

<h3>❌ Network Access Block</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"import requests\nrequests.get(\"http://google.com\")"}').output</pre>

<b>Expected:</b>
<pre>ModuleNotFoundError: No module named 'requests'</pre>

<h3>❌ Reading /etc/passwd (allowed inside container)</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"with open(\"/etc/passwd\") as f:\n    print(f.read())"}').output</pre>

<b>Expected:</b>
<pre>root:x:0:0:root:/root:/bin/bash
...</pre>

<h3>❌ File Write Block (read-only filesystem)</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"python","code":"with open(\"/tmp/hack.txt\",\"w\") as f:\n    f.write(\"hello\")"}').output</pre>

<b>Expected:</b>
<pre>OSError: [Errno 30] Read-only file system: '/tmp/hack.txt'</pre>
</div>

<hr>

<div class="section">
<h2>📘 4. JavaScript Support</h2>

<h3>✔ Test — Node.js console.log</h3>
<pre>(irm http://127.0.0.1:5000/run -Method POST `
-ContentType "application/json" `
-Body '{"language":"javascript","code":"console.log(2+2);"}').output</pre>

<b>Expected:</b>
<pre>4</pre>
</div>

<hr>

<div class="section">
<h2>🎨 5. UI Overview</h2>
<p>Your UI includes:</p>
<ul>
    <li>CodeMirror editor (Python/JS highlight)</li>
    <li>Language dropdown</li>
    <li>Run button</li>
    <li>Output window</li>
    <li>Execution history (last 10 runs)</li>
</ul>

<h3>Opening the UI</h3>
<p>Just open <code>index.html</code> in any browser.</p>
</div>

<hr>

<div class="section">
<h2>🧠 6. What I Learned</h2>
<ul>
    <li>How to safely execute untrusted code</li>
    <li>How Docker prevents system damage</li>
    <li>How to limit CPU, memory, time, and I/O</li>
    <li>How real code runner platforms work</li>
    <li>How to build UI with CodeMirror</li>
</ul>
</div>

<hr>

<div class="section">
<h2>🚀 7. Future Enhancements</h2>
<ul>
    <li>More languages (C++, Java, Go, PHP)</li>
    <li>Run containers as non-root</li>
    <li>Zip upload for multi-file projects</li>
    <li>Dark theme / theme switcher</li>
    <li>Container pooling for faster execution</li>
</ul>
</div>

<hr>

<h2>👤 Author</h2>
<p><strong>Saideep Malgireddy</strong><br>
GitHub: <a href="https://github.com/MALGIREDDY">https://github.com/MALGIREDDY</a></p>

</body>
</html>