<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alterar Senha</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>Alterar Senha de {{usuario['nome']}}</h1>

    <div class="conteudo">
        <form action="/usuario/salvarNovaSenha" method="post">
            <input type="hidden" name="id" value="{{usuario['id']}}">
            <label for="senha">Senha Antiga:</label>
            <input type="password" name="senhaAntiga" >
            <label for="senha">Senha Nova:</label>
            <input type="password" name="senhaNova" >
            <button type="submit">Salvar</button>
        </form>
    </div>
    <div class="conteudo">
        <p><a href="/usuario">Voltar para a lista</a></p>
    </div>

</body>
</html>
