#!/bin/bash
git add .
read -p "Commit descirption:" desc
git commit -m "$desc"
git push origin main
