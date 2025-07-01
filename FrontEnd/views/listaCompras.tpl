%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/listaCompra.png" alt="Ícone de Lista de Compras">
    <h1>Lista de Compras</h1>
</div>
<h1>Lista de Compras</h1>
<div class="conteudo">
    <a href="/listaCompras/novo" >Incluir nova lista</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>Mercado</th>
                <th>Data da Compra</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for lista in listas:
                <tr>
                    <td><a href="/itemCompra/{{lista['id']}}">{{lista['nome']}}</a></td>
                    <td>{{lista['mercado']['nome']}}</td>
                    <td>{{lista['dataCompra']}}</td>
                    <td>
                        <a href="/listaCompras/editar/{{lista['id']}}">Editar</a>
                        <a href="/listaCompras/confirmaExclusao/{{lista['id']}}">Excluir</a>
                        <a href="/itemCompra/{{lista['id']}}">Produtos</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>

