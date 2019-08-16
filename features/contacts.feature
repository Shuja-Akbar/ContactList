Feature: Test listing of contacts

    Background:
        Given I go to home page
        And I see the list page of contacts app

    Scenario Outline: Test Detail Page Links working
        When I click on the <name> contact
        Then I should be redirect to its detail page.

        Examples:
            | name        |
            | Adil Malik  |
            | Shuja Ahmad |
            | Adnan |


    Scenario: Test listing of feature
        Given I see following contacts shown:
            | name        | email               | phone     | address |
            | Adil Malik  | adilmalik@gmail.com | 123131123 | asdasd  |
            | Shuja Ahmed | shuja@gmail.com     | 123131231 | asdasd  |
            | Adnan | shuja@gmail.com     | 123131231 | asdasd  |