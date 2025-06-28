%rebase('base.tpl')
<h1>{{'Editar' if mercado else 'Incluir Novo'}} Mercado</h1>

<div class="conteudo">
    <form action="/mercado/salvar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" id="nome" name="nome" required value="{{mercado['nome'] if mercado else ''}}">
        <input type="hidden" name="id" value="{{mercado['id'] if mercado else ''}}">
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/mercado">Voltar para a lista</a></p>
</div>
