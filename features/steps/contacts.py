from behave import given, when, then
from behave_django.decorators import fixtures
from contact.models import ContactList


@given('I go to home page')
def step_imp(context):
    br = context.browser
    br.get(context.base_url + '/contact/')


@given('I see the list page of contacts app')
def step_imp(context):
    br = context.browser
    br.get(context.base_url + '/contact/')


@when('I click on the Adil Malik contact')
def step_impl(context):
    br = context.browser
    br.find_element_by_link_text("Adil Malik").click()


@then('I should be redirect to its detail page.')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_tag_name('h1')
    assert br.find_element_by_id('name')


@when('I click on the Shuja Ahmad contact')
def step_impl(context):
    br = context.browser
    br.find_element_by_link_text("Shuja Ahmad").click()


@when('I click on the Adnan contact')
def step_impl(context):
    br = context.browser
    br.find_element_by_link_text("Adnan").click()


@given(u'I see following contacts shown')
def step_imp(context):
    br = context.browser
    for row in context.table:
        ContactList(name=row['name'], email=['email'], phone=row['phone'], address=row['address'])
    br.quit()


@given('I am at home page')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/contact/')


@given('I goto contacts detail page')
def step_impl(context):
    br = context.browser
    br.find_element_by_link_text("Adil Malik").click()


@given('I see the details of specific page')
def step_impl(context):
    br = context.browser
    assert br.find_element_by_tag_name('h1')
    assert br.find_element_by_id('name')


@given('I am at home page for add contact')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/contact/')


@when('I goto add contact page')
def step_impl(context):
    br = context.browser
    br.find_element_by_link_text("Add").click()


@then('Add new contact with details')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('name').send_keys('Khan')
    br.find_element_by_name('email').send_keys('khan@gmail.com')
    br.find_element_by_name('phone').send_keys('123123')
    br.find_element_by_name('address').send_keys('asdasdasd')
    br.find_element_by_name('submit').click()