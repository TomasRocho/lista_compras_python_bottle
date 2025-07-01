%rebase('base.tpl')

<h1>{{'Editar' if itemCompra else 'Incluir Novo'}} Item de Compra</h1>

<div class="conteudo">
    <form action="/itemCompra/salvar" method="post">
        <!--
        <label for="idProduto">idProduto:</label>
        <input type="text" name="idProduto" required value="{{itemCompra['produto']['id'] if itemCompra else ''}}">
        --!>
        <select name="produto" id="produto">
            % for produto in produtos:
                <option value={{produto['id']}}{{ ' selected' if (itemCompra and itemCompra['produto']['id']==produto['id']) else '' }}>{{produto['nome']}}</option>
            % end
        </select>
        <input type="hidden" name="id" value="{{itemCompra['id'] if itemCompra else ''}}">
        <input type="hidden" name="idListaCompras" value="{{idListaCompras}}">
        <label for="valorUnitario">Valor Unitário:</label>
        <input type="text" name="valorUnitario"  required value="{{itemCompra['valorUnitario'] if itemCompra else 0}}" >
        <label for="quantidade">Quantidade:</label>
        <input type="text" name="quantidade"  required value="{{itemCompra['quantidade'] if itemCompra else 0}}" >
        <br/>
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/itemCompra/{{idListaCompras}}">Voltar para a lista</a></p>
</div>
