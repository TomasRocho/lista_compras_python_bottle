<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Produtos</title>
    <link rel="stylesheet" href="/static/css/estilos.css">
</head>
<body>

    <h1>Lista de Produtos</h1>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
            </tr>
        </thead>
        <tbody>
            % for produto in produtos:
                <tr>
                    <td>{{produto['id']}}</td>
                    <td>{{produto['nome']}}</td>
                </tr>
            % end
        </tbody>
    </table>

</body>
</html>
