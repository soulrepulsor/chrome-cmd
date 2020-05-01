@echo off
set script="C:\Users\stche\Documents\Personal\Project\CMD\Chrome CMD\login.py"

if  "%1%"=="acorn" (
    if "%2%"=="cc" (
        goto navigation
    )
    if "%2%"=="rah" (
        goto navigation
    )
)

if "%1%"=="acorn" (
    goto navigation
)


:navigation
python %script% %1 %2