%rebase('base.tpl')
<h1>Lista de Mercados</h1>
<div class="conteudo">
    <a href="/mercado/novo" >Incluir novo mercado</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for mercado in mercados:
                <tr>
                    <td>{{mercado['id']}}</td>
                    <td>{{mercado['nome']}}</td>
                    <td>
                        <a href="/mercado/editar/{{mercado['id']}}">Editar</a>
                        <a href="/mercado/confirmaExclusao/{{mercado['id']}}">Excluir</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>
