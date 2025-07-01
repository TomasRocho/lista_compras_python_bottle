%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/itemCompra.png" alt="Ícone de Itens da Compra">
    <h1>Itens da Compra</h1>
</div>
<h1>{{listaCompra['nome']}} no mercado {{listaCompra['mercado']['nome']}}</h1>
<h2>Valor total da compra: {{valorTotal}}</h2>
<div class="conteudo">
    <a href="/itemCompra/novo/{{idListaCompras}}" >Incluir novo item</a>
    <p/>
    <table>
        <thead>
            <tr>
                <th>Produto</th>
                <th>Valor Unitário</th>
                <th>Quantidade</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for item in itens:
                <tr>
                    <td>{{item['produto']['nome']}}</td>
                    <td>{{item['valorUnitario']}}</td>
                    <td>{{item['quantidade']}}</td>
                    <td>
                        <a href="/itemCompra/editar/{{item['id']}}">Editar</a>
                        <a href="/itemCompra/confirmaExclusao/{{item['id']}}">Excluir</a>
                        <button onclick="mostrarValorMedio({{item['produto']['id']}}, '{{item['produto']['nome']}}')">Valor Médio</button>
                    </td>
                </tr>
            % end
        </tbody>
    </table>
</div>
<div class="conteudo">
    <p><a href="/listaCompras">Voltar para as listas de compras</a></p>
</div>
<script>
function mostrarValorMedio(idProduto,nomeProduto) {
    fetch(`http://localhost:8080/itemCompra/valorMedio/${idProduto}`)
        .then(response => response.json())
        .then(data => {
            valorMedio = 0
            if (data){
                valorMedio = data.valorMedio
            }
            const totalFormatado = valorMedio.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
            //alert(`Valor médio do ${nomeProduto}: ${totalFormatado}`);
            Swal.fire({
                title: 'Valor Médio',
                text: `Valor médio do ${nomeProduto}: ${totalFormatado}`,
                icon: 'info',
                confirmButtonText: 'OK'
                });
        })
        .catch(error => {
            console.error("Erro ao chamar a API:", error);
            alert("Erro ao calcular o valor médio.");
        });
}
</script>

