%rebase('base.tpl')
<h1>Alterar Senha de {{usuario['nome']}}</h1>
<div class="conteudo">
    <form action="/usuario/salvarNovaSenha" method="post">
        <input type="hidden" name="id" value="{{usuario['id']}}">
        <label for="senha">Senha Antiga:</label>
        <input type="password" name="senhaAntiga" required>
        <label for="senha">Senha Nova:</label>
        <input type="password" name="senhaNova"  required>
        <button type="submit">Salvar</button>
    </form>
</div>

