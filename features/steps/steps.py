from behave import given
from behave import when
from behave import then
from src.lista import ClaseLista

@given(u'que tengo una lista')
def step_impl(context):
    context.lista = ClaseLista()

@when(u'esta vacía')
def step_impl(context):
   context.lista = ClaseLista()

@when(u'agrego los pares')
def step_impl(context):
    for row in context.table:
        context.lista.add(row['clave'], row['elemento'])

@then(u'la lista no debe tener elementos')
def step_impl(context):
    assert context.lista.count_elementos() == 0

@then(u'la lista no debe tener claves')
def step_impl(context):
    assert context.lista.count_claves() == 0

@then(u'la lista debe tener "{n_elementos}" elementos')
def step_impl(context, n_elementos):
    assert context.lista.count_elementos() == int(n_elementos)

@then(u'la lista debe tener "{n_claves}" claves')
def step_impl(context, n_claves):
    assert context.lista.count_claves() == int(n_claves)


@then(u'el elemento asociado a "{clave}" debe ser "{elemento}"')
def step_impl(context,clave, elemento):
    assert context.lista.find(clave) == elemento

@then(u'la lista de claves estará ordenada según la siguiente lista')
def step_impl(context):
    import numpy as np
    keys = []
    for row in context.table:
        keys.append(row['clave'])
    keys = np.asarray(keys)
    assert (context.lista.claves == keys).all()
