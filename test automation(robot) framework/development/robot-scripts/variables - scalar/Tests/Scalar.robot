*** Settings ***

*** Variables ***
${MY_VARIABLE} =  Hello there

*** Test Cases ***
Set a variable in the test case
    [Tags]  Current
    ${my_new_variable} =  Set Variable  Something else
    Log  ${my_new_variable}

Variable demonstration
    Log  ${MY_VARIABLE}

Variable demonstration 2
    Log  ${MY_VARIABLE}


*** Keywords ***
