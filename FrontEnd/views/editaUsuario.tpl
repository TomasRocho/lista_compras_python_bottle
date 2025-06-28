%rebase('base.tpl')

<h1>{{'Editar' if usr else 'Incluir Novo'}} Usuario</h1>

<div class="conteudo">
    <form action="/usuario/salvar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" name="nome" required value="{{usr['nome'] if usr else ''}}">
        <input type="hidden" name="id" value="{{usr['id'] if usr else ''}}">
        <label for="dataNascimento">Data de Nascimento:</label>
        <input type="text" name="dataNascimento" value="{{usr['dataNascimento'] if usr else ''}}" placeholder="dd/mm/aaaa" pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}" title="Formato inválido. Use dd/mm/aaaa">
        <label for="email">e-mail:</label>
        <input type="text" name="email" value="{{usr['email'] if usr else ''}}">
        <div style="{{ 'display:none' if not exibeAdministrador else '' }}">
            <label for="administrador">Administrador:</label>
            <input type="checkbox" name="administrador" value="1" {{'checked' if usr and usr['administrador'] == 1 else ''}}>
        </div>
        <div style="{{ 'display:none' if not exibeSenha else '' }}">
            <label for="senha">Senha:</label>
            <input type="text" name="senha" value="{{usr['senha'] if usr else ''}}">
        </div>
        <br/>
        
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/usuario">Voltar para a lista</a></p>
</div>
