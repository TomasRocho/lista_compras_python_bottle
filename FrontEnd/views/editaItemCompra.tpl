%rebase('base.tpl')

<h1>{{'Editar' if itemCompra else 'Incluir Nova'}} Item de Compra</h1>

<div class="conteudo">
    <form action="/itemCompra/salvar" method="post">
        <label for="idProduto">idProduto:</label>
        <input type="text" name="idProduto" required value="{{itemCompra['produto']['id'] if itemCompra else ''}}">
        <input type="hidden" name="id" value="{{itemCompra['id'] if itemCompra else ''}}">
        <input type="hidden" name="idListaCompras" value="{{idListaCompras}}">
        <label for="valorUnitario">Valor Unitário:</label>
        <input type="text" name="valorUnitario"  required value="{{itemCompra['valorUnitario'] if itemCompra else ''}}" >
        <label for="quantidade">Quantidade:</label>
        <input type="text" name="quantidade"  required value="{{itemCompra['quantidade'] if itemCompra else ''}}" >
        <br/>
        <button type="submit">Salvar</button>
    </form>
</div>
<div class="conteudo">
    <p><a href="/itemCompra/{{idListaCompras}}">Voltar para a lista</a></p>
</div>
