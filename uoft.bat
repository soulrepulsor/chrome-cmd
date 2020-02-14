@echo off
set quercus=q.utoronto.ca
set acorn=https://acorn.utoronto.ca/sws/auth/login.do?verify.dispatch
set degree=https://degreeexplorer.utoronto.ca/degreeExplorer/
set navigation=""

if  "%1%"=="quercus" (
    set navigation=%quercus%
)

if "%1%"=="acorn" (
    set navigation=%acorn%
)

if "%1%"=="degree" (
    set navigation=%degree%
)

if [%2] == [] (
    chrome %navigation%
    goto exit
)

if "%2%"=="-t" (
    goto navigation-true 
)

if "%2%"=="-f" (
    goto navigation-false
)


:navigation-true
chrome %navigation% --incognito
goto exit


:navigation-false
echo %navigation%
chrome %navigation%
goto exit

:exit