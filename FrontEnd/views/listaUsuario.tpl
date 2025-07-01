%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/usuario.png" alt="Ícone de Usuario">
    <h1>Lista de Usuários</h1>
</div>
<h1>Lista de Usuarios</h1>
<div class="conteudo">
    <a href="/usuario/novo" >Incluir novo usuario</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>Nome</th>
                <th>e-mail</th>
                <th>Data Nascimento</th>
                <th>Administrador</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for usr in usuarios:
                <tr>
                    <td>{{usr['nome']}}</td>
                    <td>{{usr['email']}}</td>
                    <td>{{usr['dataNascimento']}}</td>
                    <td>{{ "Sim" if usr['administrador'] == 1 else "Não" }}</td>
                    <td>
                        <a href="/usuario/editar/{{usuario['id']}}">Editar</a>
                        <a href="/usuario/confirmaExclusao/{{usuario['id']}}">Excluir</a>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>

