@echo off
set quercus=q.utoronto.ca
set acorn=https://acorn.utoronto.ca/sws/auth/login.do?verify.dispatch
set degree=https://degreeexplorer.utoronto.ca/degreeExplorer/

if  "%1%"=="quercus" (
    chrome %quercus%
)

if "%1%"=="acorn" (
    chrome %acorn%
)

if "%1%"=="degree" (
    chrome %degree%
)