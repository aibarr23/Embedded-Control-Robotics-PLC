*** Settings ***
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Begin Web Test
    Open Browser  about:blank  ie
    # Maximize Browser Window

End Web Test
    Close Browser