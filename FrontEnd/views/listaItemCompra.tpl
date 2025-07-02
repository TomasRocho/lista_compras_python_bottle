%rebase('base.tpl')
<div class="titulo-com-imagem">
    <img src="/static/img/itemCompra.png" alt="Ícone de Itens da Compra">
    <h1>Itens da Compra</h1>
</div>
<h1>{{listaCompras['nome']}} no mercado {{listaCompras['mercado']['nome']}}</h1>
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
    HOST_API = "localhost"
    PORTA_API = "8080"
    fetch(`http://${HOST_API}:${PORTA_API}/itemCompra/valorMedio/${idProduto}`)
        .then(response => response.json())
        .then(data => {
            valorMedio = 0
            totalFormatado = " não possui histórico"
            if (data && data.valorMedio!=0){
                valorMedio = data.valorMedio
                totalFormatado = valorMedio.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
            }
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

