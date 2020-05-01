# AcornSc
### About
Allows the students of UofT (all 3 campuses) to access certain features of acorn through
the CMD commands

### Supported Platform
CMD (Windows 10) and maybe earlier versions of Windows

### Supported Features
1. Current Courses: Display current term's or available term's courses
2. Current Event: Display current day's events 
3. Recent Academic History: Display current term's or available term's course's
status or marks as well as the course average if available 

### Installation Guide
**Note**: The project is in early stage so the installation is not dummy proof.
Hence, this installation guide is only for people that are interested in the project
and would like to try it out

1. Install Python 3.XX **(Python 2.XX or earlier version would not work)**
2. Install Chrome browser at the default location (As long as you did not 
change the installation location, you're fine)
3. Add Python to the Path Environment Variable if it's not already added
4. Download/clone the project and add the downloaded folder to the Path
Environment Variable
5. Create a config.env inside the downloaded folder and add the following contents into it:
`UOFT_UTORID="your utorid"` <br />
`UOFT_PASSWORD="your acorn password"`
6. Refer to the next section on how to invoke the commands

### Commands
#### Current Courses
`test acorn cc`
#### Today's Events
`test acorn tt`
#### Recent Academic History
`test acorn rah`
