DELAY 5000

REM Open Run and launch Command Prompt
GUI R
DELAY 1000
STRING cmd
ENTER
DELAY 4000

REM Download and open the resume PDF
STRING curl.exe -fL -o "%TEMP%\Trevor_Markevicz_Resume_2026.pdf" "https://github.com/tgmarkevicz1/Steves-LinkedIn-BadUSB/blob/6794b5214ee55e0f3a137ca52c6c85893985d561/Trevor_Markevicz_Resume_2026.pdf" && start "" msedge.exe --new-window "%TEMP%\Trevor_Markevicz_Resume_2026.pdf" && exit
ENTER

REM Wait for Command Prompt to close and the PDF to open
DELAY 5000

REM Open Run and navigate to LinkedIn
GUI R
DELAY 1000
STRING https://www.linkedin.com/in/trevor-markevicz/
ENTER
