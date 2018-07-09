# language: pt

Funcionalidade: Acessar Paginas Internas
    Cenario: acessar home
        Quando acessar a pagina "http://127.0.0.1:3000"
        Entao deve aparecer na pagina a string "Enviar"

    Cenario: acessar about
        Quando acessar a pagina "http://127.0.0.1:3000/about"
        Entao deve aparecer na pagina a string "About Marina Project"
    
    