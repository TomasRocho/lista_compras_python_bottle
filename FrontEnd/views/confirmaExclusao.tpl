<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirmar Exclusão</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>Confirmar Exclusão</h1>

    <div class="conteudo">
        <p>Tem certeza de que deseja excluir o {{nomeObjeto}} <strong>"{{descricaoObjeto}}"</strong>?</p>
    </div>
    <div class="conteudo">
        <form action="/{{nomeObjeto}}/excluir/{{id}}">
            <button type="submit">Sim, excluir</button>
            <a href="/{{nomeObjeto}}">Cancelar</a>
        </form>
    </div>

</body>
</html>