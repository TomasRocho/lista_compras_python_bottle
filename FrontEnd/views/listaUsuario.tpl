<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Usuarios</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>Lista de Usuarios</h1>
    <div class="conteudo">
        <a href="/usuario/novo" >Incluir novo usuario</a>
        <p/>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>e-mail</th>
                    <th>Data Nascimento</th>
                    <th>Administrador</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                % for usuario in usuarios:
                    <tr>
                        <td>{{usuario['id']}}</td>
                        <td>{{usuario['nome']}}</td>
                        <td>{{usuario['email']}}</td>
                        <td>{{usuario['dataNascimento']}}</td>
                        <td>{{ "Sim" if usuario['administrador'] == 1 else "Não" }}</td>
                        <td>
                            <a href="/usuario/editar/{{usuario['id']}}">Editar</a>
                            <a href="/usuario/confirmaExclusao/{{usuario['id']}}">Excluir</a>
                            <a href="/usuario/alterarSenha/{{usuario['id']}}">Alterar senha</a>
                        </td>
                    </tr>
                % end
            </tbody>
        </table>
    </div>
</body>
</html>
