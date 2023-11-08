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
