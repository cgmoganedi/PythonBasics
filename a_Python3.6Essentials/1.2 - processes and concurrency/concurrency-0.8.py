import subprocess
results = subprocess.run(['ls','-l'], stdout=subprocess.PIPE)
print(results.stdout)
