import base64
import io
import urllib

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('Agg')


def informacao_utilizadores(objetos):
    dados = {}
    for quizz in objetos:
        dados[quizz.nome] = QuizPontuacao(quizz)

    return dados


def cria_grafico(objetos):
    dados = informacao_utilizadores(objetos)

    dados = dict(sorted(dados.items(), key=lambda item: item[1], reverse=False))

    pessoa = list(dados.keys())
    pontuacao = list(dados.values())
    plt.figure(figsize=(10, 5))
    plt.barh(pessoa, pontuacao)
    plt.title("Pontuação dos participantes!")
    plt.ylabel("Nome dos participantes")
    plt.xlabel("Pontuação")
    plt.autoscale()

    fig = plt.gcf()
    plt.close()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')

    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri


def QuizPontuacao(input):
    pontuacao = 2

    if input.pergunta1 == '10789':
        pontuacao += 1

    if input.pergunta2 == 'Wild':
        pontuacao +=1

    if input.pergunta3 == 2005:
        pontuacao += 1

    if input.pergunta4 == 1991:
        pontuacao += 1

    if input.pergunta5 == 'Tigre':
        pontuacao += 1

    return pontuacao
