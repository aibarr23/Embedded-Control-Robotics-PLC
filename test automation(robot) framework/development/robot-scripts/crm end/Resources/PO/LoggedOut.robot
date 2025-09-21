*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${LOGGEDOUT_HEADER_LABEL} =         Signed Out

*** Keywords ***
Verify Page Loaded
    wait until page contains        ${LOGGEDOUT_HEADER_LABEL}