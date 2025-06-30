%rebase('base.tpl')

<h1>Confirmar Exclusão</h1>

<div class="conteudo">
    <p>Tem certeza de que deseja excluir o {{nomeObjeto}} <strong>"{{descricaoObjeto}}"</strong>?</p>
</div>
<div class="conteudo">
    <form action="/{{nomeObjeto}}/excluir/{{id}}">
        <button type="submit">Sim, excluir</button>
        <a href='{{rotaRetorno}}'>Cancelar</a>
    </form>
</div>
