<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body  class="body_erro">

    <div class="container_erro">
        <h1 class="h1_erro">{{tipoErro}}</h1>
        <p>{{mensagem}}</p>
        <a href="javascript:history.back()">Voltar para a página anterior</a>
    </div>
</body>
</html>