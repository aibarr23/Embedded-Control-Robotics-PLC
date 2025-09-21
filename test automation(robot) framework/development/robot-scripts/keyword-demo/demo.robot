*** Settings ***

# copy/paste the command below into terminal to run
# robot demo.robot

*** Test Cases ***
Test case 1
    Do Something
    Do Something Else

Test case 2
    Do Another Thing
    Do Something Else

*** Keywords ***
Do Something
    Log  I am doing something...

Do Something Else
    Log  I am doing something else...

Do Another Thing
    Log  I am doing another thing...