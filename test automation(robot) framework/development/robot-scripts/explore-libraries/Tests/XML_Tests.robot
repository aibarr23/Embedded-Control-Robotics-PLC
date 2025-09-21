*** Settings ***
Documentation  These are some XML tests
Resource  ../Resources/XML/Breakfast_Menu.robot

# Many ways to run:
# robot -d results/xml tests/XML_Tests.robot
# robot -d results/xml -i XML tests
# robot -d results tests

*** Variables ***


*** Test Cases ***
Verify Menu Count
    [Tags]  XML
    Breakfast_Menu.Should be one menu in the file

Verify Root
    [Tags]  XML
    Breakfast_Menu.Verify Menu Name

Verify Food Count
    [Tags]  XML
    Breakfast_Menu.Verify Food Count

Verify First Food
    [Tags]  XML
    Breakfast_Menu.Verify First Food Name
    Breakfast_Menu.Verify First Food Price
    Breakfast_Menu.Verify First Food Calories

Add a Food
    [Tags]  XML
    Breakfast_Menu.Add New Food

Verify New Food Was Added
    [Tags]  XML
    Breakfast_Menu.Verify New Food Exists