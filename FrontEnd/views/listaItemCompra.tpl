%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/usuario.png" alt="Ícone de Itens da Compra">
    <h1>Itens da Compra</h1>
</div>
<h1>Itens da Compra</h1>
<div class="conteudo">
    <a href="/itemCompra/novo/{{idListaCompras}}" >Incluir novo item</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Produto</th>
                <th>Valor Unitário</th>
                <th>Quantidade</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for item in itens:
                <tr>
                    <td>{{item['id']}}</td>
                    <td>{{item['produto']['nome']}}</td>
                    <td>{{item['valorUnitario']}}</td>
                    <td>{{item['quantidade']}}</td>
                    <td>
                        <a href="/itemCompra/editar/{{item['id']}}">Editar</a>
                        <a href="/itemCompra/confirmaExclusao/{{item['id']}}">Excluir</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>
<div class="conteudo">
    <p><a href="/listaCompras">Voltar para as listas de compras</a></p>
</div>

