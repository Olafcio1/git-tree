import subprocess
import time
import os

path = os.getenv("USERPROFILE") + "/IdeaProjects"
projects = os.listdir(path)

skipped = 0

for project in projects:
  sub = path+"/"+project
  #print(project +"="+str(time.time() - os.stat(sub).st_mtime))
  if time.time() - os.stat(sub).st_mtime > (60 * 60 * 24 * 7 * 10):
    skipped += 1
    continue

  text = subprocess.run(["git", "status"], cwd=sub, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout

  if "not a git" in text:
    continue

  if "nothing to commit" in text and len(projects) > 7:
    continue

  print("Project %s = %s" % (project, "pushed" if "nothing to commit" in text else (str(len(text.split(":  "))-1) + " remaining changes")))

print("\n%d projects skipped" % skipped)
