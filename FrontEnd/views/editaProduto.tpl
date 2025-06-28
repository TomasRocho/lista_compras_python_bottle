%rebase('base.tpl')

<h1>{{'Editar' if produto else 'Incluir Novo'}} Produto</h1>

<div class="conteudo">
    <form action="/produto/salvar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required value="{{produto['nome'] if produto else ''}}">
        <input type="hidden" name="id" value="{{produto['id'] if produto else ''}}">
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/produto">Voltar para a lista</a></p>
</div>
