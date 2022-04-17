import subprocess

completed  = subprocess.run(["python", "sqlite.py"] ,capture_output=True , text=True)
print("args :" ,completed.args)
print("stderr:" , completed.stderr)