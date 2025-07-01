%rebase('base.tpl')

<h1>{{'Editar' if listaCompras else 'Incluir Nova'}} Lista de Compras</h1>

<div class="conteudo">
    <form action="/listaCompras/salvar" method="post">
        <label for="nome">Nome:</label>
        <input type="text" name="nome" required value="{{listaCompras['nome'] if listaCompras else ''}}">
        <input type="hidden" name="id" value="{{listaCompras['id'] if listaCompras else ''}}">
        <input type="hidden" name="idUsuario" value="{{usuario['id']}}">
        <label for="dataCompra">Data da Compra:</label>
        <input type="text" name="dataCompra"  required value="{{listaCompras['dataCompra'] if listaCompras else dataHoje}}" placeholder="dd/mm/aaaa" pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}" title="Formato inválido. Use dd/mm/aaaa">
        <label for="mercado">Mercado:</label>
        <select name="mercado" id="mercado">
            % for mercado in mercados:
                <option value={{mercado['id']}}{{ ' selected' if (listaCompras and listaCompras['mercado']['id']==mercado['id']) else '' }}>{{mercado['nome']}}</option>
            % end
        </select>
        <br/>
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/listaCompras">Voltar para a lista</a></p>
</div>
