*** Settings ***
Documentation  Talk about what this suite of tests does
Resource  ../Resources/FrontOfficeApp.robot
Resource  ../Resources/CommonWeb.robot
Test Setup  Begin Web Test
Test Teardown  End Web Test

# robot -d results tests/Front_Office.robot

*** Variables ***
${BROWSER} =  edge
${URL} =  http://www.robotframeworktutorial.com/front-office

*** Test Cases ***
Should be able to access "Team" page
    [Documentation]  This is test 1
    [Tags]  test1
    log  Executing test 1
    Sleep  2s

"Team" page should match requirements
    [Documentation]  This is test 2
    [Tags]  test2
    log  Executing test 2
    Sleep  2s