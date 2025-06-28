<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link rel="stylesheet" href="/static/css/estiloLogin.css">
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form method="POST" action="/usuario/login">
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required>

            <label for="senha">Senha:</label>
            <input type="password" name="senha" id="senha" required>

            <input type="submit" value="Entrar">
        </form>
    </div>
</body>
</html>
