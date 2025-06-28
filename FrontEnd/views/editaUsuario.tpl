<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{'Editar' if usuario else 'Novo'}} Usuario</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>{{'Editar' if usuario else 'Incluir Novo'}} Usuario</h1>

    <div class="conteudo">
        <form action="/usuario/salvar" method="post">
            <label for="nome">Nome:</label>
            <input type="text" name="nome" required value="{{usuario['nome'] if usuario else ''}}">
            <input type="hidden" name="id" value="{{usuario['id'] if usuario else ''}}">
            <label for="dataNascimento">Data de Nascimento:</label>
            <input type="text" name="dataNascimento" value="{{usuario['dataNascimento'] if usuario else ''}}" placeholder="dd/mm/aaaa" pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}" title="Formato inválido. Use dd/mm/aaaa">
            <label for="email">e-mail:</label>
            <input type="text" name="email" value="{{usuario['email'] if usuario else ''}}">
            <div style="{{ 'display:none' if not exibeAdministrador else '' }}">
                <label for="administrador">Administrador:</label>
                <input type="checkbox" name="administrador" value="1" {{'checked' if usuario and usuario['administrador'] == 1 else ''}}>
            </div>
            <div style="{{ 'display:none' if not exibeSenha else '' }}">
                <label for="senha">Senha:</label>
                <input type="text" name="senha" value="{{usuario['senha'] if usuario else ''}}">
            </div>
            <br/>
            
            <button type="submit">Salvar</button>
        </form>
    </div>
    <div class="conteudo">
        <p><a href="/usuario">Voltar para a lista</a></p>
    </div>

</body>
</html>
