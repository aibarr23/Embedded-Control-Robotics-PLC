*** Settings ***
Library  Selenium2Library

*** Variables ***


*** Test Cases ***
User can search for products
    # Here we pass variable input data to a user-defined keyword
    # Try it: Change the URL and/or browser input values (ie, chrome, firefox, etc.)
    @{url_and_browser} =  Set Variable  http://www.amazon.com  ie
    Begin Web Test  @{url_and_browser}

*** Keywords ***
Begin Web Test
    [Arguments]  @{url_and_browser}
    Open Browser  @{url_and_browser}[0]  @{url_and_browser}[1]
    Close Browser

