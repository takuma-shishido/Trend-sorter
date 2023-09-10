"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from .models import Repository
from .trend import find_trend

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backendAPP.settings')

application = get_wsgi_application()


# Init DB

RunInit = False

if RunInit == True: 
  LangList = [
    "1C Enterprise",
    "C",
    # "C#", Error
    "C++",
    "CSS",
    "Clojure",
    "Common Lisp",
    "Crystal",
    "D",
    "Dart",
    "Elixir",
    "Elm",
    "Emacs Lisp",
    "Erlang",
    "F#",
    "Fortran",
    "GDScript",
    "Go",
    "Haskell",
    "Haxe",
    "Java",
    "JavaScript",
    "Julia",
    "Jupyter Notebook",
    "Kotlin",
    "Lua",
    "MQL4",
    "MQL5",
    "Nim",
    "Nix",
    "OCaml",
    "Objective-C",
    "PHP",
    "Pascal",
    "Perl",
    "PowerShell",
    "Prolog",
    "PureScript",
    "Python",
    "R",
    "Racket",
    "Ruby",
    "Rust",
    "Scala",
    "Shell",
    "Solidity",
    "Svelte",
    "Swift",
    "TypeScript",
    "Vala",
    "Verilog",
    "Vim script",
    "Vue",
    "Zig",
  ]
  print("Init DB")
  Repository.objects.all().delete()
  for lang in LangList:
    todays = find_trend("daily",lang)
    for today in todays:
      if 'Name' in today:
        Repository.objects.create(
          span = "daily",
          name = today["Name"],
          url = today["URL"],
          description = today["Description"],
          lang = today["Lang"],
          star = today["Star"],
          star_by_span = today["StarBySpan"],
          fork = today["Fork"],
        )
    weeks = find_trend("weekly",lang)
    for week in weeks:
      if 'Name' in week:
        Repository.objects.create(
          span = "weekly",
          name = week["Name"],
          url = week["URL"],
          description = week["Description"],
          lang = week["Lang"],
          star = week["Star"],
          star_by_span = week["StarBySpan"],
          fork = week["Fork"],
        )
    months = find_trend("monthly",lang)
    for month in months:
      if 'Name' in month:
        Repository.objects.create(
          span = "monthly",
          name = month["Name"],
          url = month["URL"],
          description = month["Description"],
          lang = month["Lang"],
          star = month["Star"],
          star_by_span = month["StarBySpan"],
          fork = month["Fork"],
        )
    print(f"done {lang}")
  print("Init DB done")