#!/usr/bin/env bash
# Rebuild the BluePrint site: assemble pages, then compile Tailwind.
set -e
cd "$(dirname "$0")"
python3 build.py
npx tailwindcss -c tailwind.config.js -i tailwind.input.css -o ../site/css/tailwind.css --minify
