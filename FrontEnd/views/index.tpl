%rebase('base.tpl')

<h1 class="titulo-opcoes">Painel de Navegação</h1>

<div class="grid-opcoes">
    <a href="/listaCompras" class="card-opcao">
        <img src="/static/img/listaCompra.png" alt="Listas de Compras">
        <span>Listas de Compras</span>
    </a>
    <a href="/produto" class="card-opcao">
        <img src="/static/img/produto.png" alt="Produtos">
        <span>Produtos</span>
    </a>
    <a href="/mercado" class="card-opcao">
        <img src="/static/img/mercado.png" alt="Mercados">
        <span>Mercados</span>
    </a>
    <a href="/usuario" class="card-opcao">
        <img src="/static/img/usuario.png" alt="Usuários">
        <span>Usuários</span>
    </a>
    <a href="/usuario/alterarSenha" class="card-opcao">
        <img src="/static/img/senha.png" alt="Usuários">
        <span>Alterar Senha</span>
    </a>
    <form action="/usuario/logout" method="post" class="card-opcao  card-logout">
        <button type="submit">
            <img src="/static/img/logout.png" alt="Logout">
            <span>Logout</span>
        </button>
    </form>
</div>