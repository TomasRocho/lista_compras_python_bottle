%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/produto.png" alt="Ícone de Produto">
    <h1>Lista de Produtos</h1>
</div>
<div class="conteudo">
    <a href="/produto/novo" >Incluir novo produto</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for produto in produtos:
                <tr>
                    <td>{{produto['nome']}}</td>
                    <td>
                        <a href="/produto/editar/{{produto['id']}}">Editar</a>
                        <a href="/produto/confirmaExclusao/{{produto['id']}}">Excluir</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>