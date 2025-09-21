*** Settings ***
Documentation  This is some basic info about the whole suite
Resource  Resources/Common.robot  # for Setup & Teardown
Resource  Resources/Amazon.robot  # for lower level keywords in test cases
Test Setup  Common.Begin Web Test
Test Teardown  Common.End Web Test

*** Variables ***
${BROWSER} =  ie
${START_URL} =  https://www.amazon.com
${SEARCH_TERM} =  Ferrari 458

*** Test Cases ***
Logged out user can search for products
    [Tags]  Current
    Amazon.Search for Products

Logged out user can view a product
    Amazon.Search for Products
    Amazon.Select Product from Search Results

Logged out user can add product to cart
    Amazon.Search for Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart

Logged out user must sign in to check out
    Amazon.Search for Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart
    Amazon.Begin Checkout
