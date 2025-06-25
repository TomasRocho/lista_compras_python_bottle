<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erro</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 2em;
            background-color: #fef2f2;
            color: #b91c1c;
        }
        .container {
            max-width: 600px;
            margin: auto;
            border: 1px solid #fecaca;
            background-color: #fff;
            padding: 1.5em;
            border-radius: 8px;
            box-shadow: 0 0 10px #fca5a5;
        }
        h1 {
            color: #b91c1c;
        }
        a {
            display: inline-block;
            margin-top: 1em;
            text-decoration: none;
            color: #2563eb;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Erro na Requisição</h1>
        <p>{{mensagem}}</p>
        <a href="javascript:history.back()">Voltar para a página anterior</a>
    </div>

</body>
</html>