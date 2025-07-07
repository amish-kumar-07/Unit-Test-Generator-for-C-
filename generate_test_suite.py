import os
import subprocess
import threading
import itertools
import sys
import time

# File paths
yaml_path = "prompts/generate_tests.yaml"
cpp_path = "src/main.cpp"
output_path = "tests/test_main.cpp"

# Read YAML
with open(yaml_path, 'r') as yfile:
    yaml_content = yfile.read()

# Read C++ source
with open(cpp_path, 'r') as cppfile:
    cpp_code = cppfile.read()

# Final prompt
prompt = f"""You are a professional C++ unit test generator.

Below is the YAML file containing test generation rules.
After that is the C++ source file.

Use the rules strictly to generate GoogleTest-based unit tests.

---
YAML:
{yaml_content}

---
C++ Source:
{cpp_code}

Generate clean, readable tests. Avoid duplicate tests and only output valid C++ code using Google Test.
"""

# Spinner function
def spinner_task(stop_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_event.is_set():
            break
        sys.stdout.write(f'\r🧠 Generating with LLM... {c}')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r✅ Done generating tests!     \n')

# Run Ollama and show spinner while it runs
print("🔄 Running Ollama...")

stop_spinner = threading.Event()
spinner_thread = threading.Thread(target=spinner_task, args=(stop_spinner,))
spinner_thread.start()

try:
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True
    )
    stop_spinner.set()
    spinner_thread.join()
except subprocess.CalledProcessError as e:
    stop_spinner.set()
    spinner_thread.join()
    print("❌ Ollama failed:")
    print(e.stderr)
    exit(1)

# Ensure output folder exists
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save output
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result.stdout)

print("📄 Test file saved to:", output_path)