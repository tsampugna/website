---
title: Notes on upload process
Modified: 2025-02-07T01:15:34-06:00
tags:
  - notes
---

Sync posts from Obsidian to Hugo content folder using Robocopy
```copy
robocopy "D:\Obsidian\Posts" "C:\Users\Tony\Documents\sampugnablog\content\posts" *.md /mir
```


Process Markdown files with Python script to handle image links
```copy
python .\images.py
```

Build the Hugo site
```copy
hugo
```

Add changes to Git
```copy
git add .
```

Commit changes with a dynamic message
```copy
git commit -m "New Blog Post on + $(get-date -Format 'yyyy-MM-dd HH:mm:ss')"
```

Push the public folder to the hostinger branch using subtree split and force push
```copy
git subtree split --prefix public -b blog-deploy
git push origin blog-deploy:blog --force
git branch -D blog-deploy
```