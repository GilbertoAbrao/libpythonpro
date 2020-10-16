import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario', ['ggafbr@gmail.com', 'foo@bar.com.br'])
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'gggafbr@gmail.com',
        'Curso Python Pro',
        'Qq mensagem corpo do email'
    )
    assert destinatario in resultado


@pytest.mark.parametrize('destinatario', ['', 'foobar.com.br'])
def test_remetente_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            destinatario,
            'gggafbr@gmail.com',
            'Curso Python Pro',
            'Qq mensagem corpo do email'
        )
