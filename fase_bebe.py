from random import randint
from json_def import carregar_dados_player, guardar_dados_player


def fase_bebe():
    # Carrega os dados do jogador a partir de um arquivo JSON ou fonte de dados semelhante
    dados = carregar_dados_player()

    # Verifica se a fase criança já foi concluída
    # Isso é determinado verificando a chave "concluida" no dicionário aninhado em "fase_crianca"
    concluida = dados["fase_crianca"][0]["concluida"]
    if concluida:
        # Se a fase estiver concluída, uma exceção é levantada para evitar a reentrada nessa fase
        # Isso indica a necessidade de redefinir o jogo ou as configurações do jogador para o padrão para jogar novamente esta fase
        raise Exception('Config da fase criança precisa ser restaurado às definições de fábrica')

    # Pergunta ao jogador se ele quer ir com os pais
    # Esta é uma pergunta simples de sim/não que influencia a narrativa do jogo
    pais = input('Quer ir com os pais (s/n)? ').strip().lower()
    while pais not in ["s", "n"]:  # Valida a entrada para garantir que seja 's' (sim) ou 'n' (não)
        pais = input('Quer ir com os pais (s/n)? ').strip().lower()

    if pais == "s":  # Se o jogador escolher ir com os pais
        print('Foste com os pais')
        # Registra a escolha do jogador na estrutura de dados para influenciar as decisões ou narrativas do jogo posteriormente
        dados["fase_crianca"][0]["pais"] = "S"
    elif pais == "n":  # Se o jogador escolher não ir com os pais
        print('Foste sem os pais')
        # Da mesma forma, registra essa escolha para impacto potencial em futuras fases ou desfechos do jogo
        dados["fase_crianca"][0]["pais"] = "N"

    # Salva os dados do jogador atualizados de volta no armazenamento persistente após registrar a decisão
    guardar_dados_player(dados)

    # Atribui aleatoriamente o número de biberões entre 0 e 1
    # Isso pode fazer parte da mecânica do jogo que afeta os recursos ou a saúde do jogador
    biberao = randint(0, 1)
    # Atualiza os dados do jogador com o número de biberões determinado aleatoriamente
    dados["fase_crianca"][0]["biberoes"] = biberao

    # Salva os dados do jogador novamente após atualizá-los com as novas informações
    guardar_dados_player(dados)
