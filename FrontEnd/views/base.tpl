<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Compras - UnB</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
</head>
<body>
    <header class="cabecalho_base">
        <div class="cabecalho-esquerda_base">
            <img src="/static/img/carrinho.png" alt="Carrinho de Compras" class="logo_base">
            <div class="info_base">
                <h1>Lista de Compras Web</h1>
                <p class="subtitulo_base">Trabalho final - OO | UnB</p>
                <p class="subtitulo_base">Desenvolvido em Python/Bottle</p>
                <p class="subtitulo_base">Aluno: Tomás Garcia Rocho - Matrícula: 242024988</p>
                <div style="{{ 'display:none' if not mostrarVoltarIndex else '' }}">
                    <p class="subtitulo_base"><a href="/index">Voltar a Tela Principal</a></p>
                </div>
            </div>
        </div>
        <div class="cabecalho-direita_base">
            <p>👤 {{usuario['nome']}}{{' - Admin' if usuario['administrador']==1 else ''}}</p>
            <form action="/usuario/logout" method="post">
                <button type="submit" class="botao-logout">Trocar de Usuário</button>
            </form>
        </div>
    </header>
    <main class="conteudo">
        {{!base}}
    </main>
</body>
</html>
