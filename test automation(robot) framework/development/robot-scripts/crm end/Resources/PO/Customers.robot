*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${CUSTOMERS_HEADER_LABEL} =                     Our Happy Customers
${CUSTOMERS_ADD_CUSTOMER_LINK} =                id=new-customer
${CUSTOMERS_CUSTOMER_SUCCESS_LABEL} =           Success! New customer added.

*** Keywords ***
Verify Page Loaded
    wait until page contains    ${CUSTOMERS_HEADER_LABEL}

Click Add Customer Link
    click link                  ${CUSTOMERS_ADD_CUSTOMER_LINK}

Verify Customer Added Successfully
    wait until page contains    ${CUSTOMERS_CUSTOMER_SUCCESS_LABEL}