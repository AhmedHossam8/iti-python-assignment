import os
FILE_PATH = './logs.txt'

errors = []
warnings = []
infos = []


if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w', newline='') as file:
        file.write('')

with open(FILE_PATH, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        if '[ERROR]' in line:
            errors.append(line)
        elif '[WARNING]' in line:
            warnings.append(line)
        elif '[INFO]' in line:
            infos.append(line)

print("Log File Analysis")
print("-----------------")
print(f"Total entries: {len(errors) + len(warnings) + len(infos)}")
print(f"INFO: {len(infos)}")
print(f"WARNING: {len(warnings)}")
print(f"Error: {len(errors)}")

print("ERROR messages:")
for i, error in enumerate(errors):
    print(f"{i+1}. {error}")
    

if len(infos) >= len(warnings) and len(infos) >= len(errors):
    most = "INFO"
elif len(warnings) >= len(errors):
    most = "WARNING"
else:
    most = "ERROR"
    
print(f"Most common level: {most}")

with open('errors.log', 'w', encoding='utf-8') as file:
    for error in errors:
        file.write(error + '\n')