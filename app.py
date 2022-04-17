from pathlib import Path
path = Path("package")
print(path.exists())
print(path.name)
print(path.is_file())
print(path.parent)
paths= [p for  p in path.iterdir()  if p.is_dir() ]
py_files = [p  for p in path.glob("*.py") ]
print(py_files)