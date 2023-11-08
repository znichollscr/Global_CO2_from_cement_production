- datalad clone not git clone
- if you muck up the above, if you try and run e.g. download on an old version, you'll get a slightly cryptic error message about a file not existing (this is because datalad is trying to follow a link to something that doesn't exist, you can follow the link and see it points to annex which won't exist)
- datalad status seems to still run anyway, but it can't actually do the fetch..

- install datalad first
    - if you fork a repo but not the annex branch, could cause problems
    - have to do pull requests on gin if you are changing data
- clone from Johannes' gin (may work from other sources, something to try another day)

- datalad is a wrapper around git (so always try to use datalad first for stuff).
    - probably should have read the datalad docs before I started

- if `datalad get file` behaves, you should be ok

- branching gets a bit weird with datalad but you only have one annex branch so the idea of branching is more of an illusion than reality


Attempt number two notes:

1. Brew install datalad
1. Fork Johannes' Gin repo
1. Add ssh key to my gin account
1. Clone using ssh (may have to help with ssh/config)
1. run `datalad siblings`, there should be a + in each line
    - might have to run `git annex enableremote gin-src` to have this be properly set up
1. `python3 -m venv venv`
1. `pip install --upgrade pip wheel`
1. `pip install doit`
1. `head extracted_data/v220516/Robbie_Andrew_Cement_Production_CO2_220516.csv` should say 'file not found', that's how you know it hasn't been pulled yet (which is what we want"
1. `datalad get extracted_data/v220516/Robbie_Andrew_Cement_Production_CO2_220516.csv`
1. `head extracted_data/v220516/Robbie_Andrew_Cement_Production_CO2_220516.csv` should now show data as we just fetched
1. `doit list` to see tasks
1. `doit download_version version=v230913` should then behave (i.e. run without error)...
    - If it doesn't, we'll debug together
    - As notes: I had to tweak gitignore and some src to make it work
1. `doit read_version version=v230913` should then also behave (i.e. run without error)...
1. All set up :)


1. Then can add metadata for new version
1. Then run download
1. Then read
1. Then `datalad save`
1. Then `datalad push`
1. Done
