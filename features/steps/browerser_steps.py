from behave import given, when, then, step

@when('acessar a pagina "{page}"')
def acess_page(context, page):
    context.ff.get(page)

@then('deve aparecer na pagina a string "{string}"')
def test_html(context, string):
    assert string in context.ff.page_source, \
        'O texto não foi encontrado na página'