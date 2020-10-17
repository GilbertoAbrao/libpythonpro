from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_qtd_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'ggafbr@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )

def test_parametros_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'ggafbr@gmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
