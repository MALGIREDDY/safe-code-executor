from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <h1>Safe Code Executor<h1>
    <h2>server is running....</h2>
    """

@app.post("/run")
def run_code():
    data = request.get_json()
    code = data.get("code", "")
    language = data.get("language", "python")  # default Python

    if len(code) > 5000:
        return jsonify({"output": "Error: Code too long (max 5000 characters)."}), 400

    # Safe temp directory
    temp_dir = os.path.join(os.path.expanduser("~"), "safe-executor-temp")
    os.makedirs(temp_dir, exist_ok=True)

    file_id = str(uuid.uuid4())

    # Select file extension + Docker image + run command
    if language == "javascript":
        filename = os.path.join(temp_dir, f"{file_id}.js")
        docker_image = "node:18-slim"
        run_cmd = ["node", "/script.js"]
        container_script_path = "/script.js"
    else:
        filename = os.path.join(temp_dir, f"{file_id}.py")
        docker_image = "python:3.11-slim"
        run_cmd = ["python", "/script.py"]
        container_script_path = "/script.py"

    # Write code into temp file
    with open(filename, "w") as f:
        f.write(code)

    # Convert Windows path to Docker path
    docker_path = filename.replace("\\", "/")

    # Build docker command
    cmd = [
        "docker", "run",
        "--rm",
        "--network", "none",
        "--memory=128m",
        "--cpus=0.5",
        "--read-only",
        "-v", f"{docker_path}:{container_script_path}:ro",
        docker_image
    ] + run_cmd

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        output = result.stdout or result.stderr
    except subprocess.TimeoutExpired:
        output = "Execution timed out after 10 seconds"
    finally:
        os.remove(filename)

    return jsonify({"output": output})

if __name__ == "__main__":
    app.run(port=5000)
