from behave import given
from behave import when
from behave import then
from pageobjects.contact_page import ContactPage

@given(u'que estoy en la pagina de contacto')
@given(u'I am on the contact page')
def step_impl(context):
    context.contact_page = ContactPage(context.driver)
    context.contact_page.open()

@when(u'lleno el campo de nombre con "{name}')
@when(u'I fill the name field with "{name}"')
def step_impl(context, name):
    context.contact_page.set_name(name)

@when(u'lleno el campo de correo electronico con "{email}"')
@when(u'I fill the email field with "{email}"')
def step_impl(context, email):
    context.contact_page.set_email(email)

@when(u'lleno el campo de mensaje con "{message}"')
@when(u'I fill the message field with "{message}"')
def step_impl(context, message):
    context.contact_page.set_message(message)

@then(u'el campo de nombre no debe estar vacio')
@then(u'the field name should not be empty')
def step_impl(context):
    assert context.contact_page.get_name()

@then(u'el campo de correo electronico no debe estar vacio')
@then(u'the field email should not be empty')
def step_impl(context):
    assert context.contact_page.get_email()

@then(u'el campo de mensaje no debe estar vacio')
@then(u'the field message should not be empty')
def step_impl(context):
    assert context.contact_page.get_message()
