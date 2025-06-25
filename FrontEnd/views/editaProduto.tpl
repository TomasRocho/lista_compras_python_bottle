<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{'Editar' if produto else 'Novo'}} Produto</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>{{'Editar' if produto else 'Incluir Novo'}} Produto</h1>

    <form action="/produto/salvar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required value="{{produto['nome'] if produto else ''}}">
        <input type="hidden" name="id" value="{{produto['id'] if produto else ''}}">
        <button type="submit">Salvar</button>
    </form>

    <p><a href="/produto">Voltar para a lista</a></p>

</body>
</html>
