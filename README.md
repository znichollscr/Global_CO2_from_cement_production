# Title

Notes from exploring:

- Having set up venv in dodo.py is cool, but super hard to maintain. I'd just skip that/move to a Makefile to make life simpler, then we can also just install doit into the venv
    - if forgetting to set up your venv often bites though, could be worth keeping, I'm on the fence (we don't have a good venv maintenance routine in other repos, you just have to know that forgetting to upgrade your venv is a possible reason for failures)
