// Função para manipular a exibição das janelas (escopo global)
function morphic_window(windowId) {
    console.log(`Abrindo janela com ID: ${windowId}`);
    alert(`Você clicou na janela: ${windowId}`); // Substitua esta linha pelo comportamento real desejado
}

document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("user_email");
    const searchButton = document.getElementById("submit_btn");
    const tabContainer = document.getElementById("tab2");

    // Função para buscar ONGs na API
    async function fetchOngs(query) {
        try {
            const response = await fetch(`http://127.0.0.1:5000/search?q=${encodeURIComponent(query)}`); // Porta correta
            if (!response.ok) {
                throw new Error("Erro ao buscar ONGs");
            }
            return await response.json();
        } catch (error) {
            console.error(error);
            return [];
        }
    }

    // Função para atualizar o conteúdo da aba de ONGs
    function updateOngTab(ongs) {
        tabContainer.innerHTML = ""; // Limpa o conteúdo existente

        if (ongs.length === 0) {
            const noResults = document.createElement("p");
            noResults.textContent = "Nenhuma ONG encontrada.";
            noResults.style.color = "red";
            tabContainer.appendChild(noResults);
            return;
        }

        ongs.forEach((ong, index) => {
            const ongDiv = document.createElement("div");
            ongDiv.className = "menu-price mr-0 mr-lg-5";

            // Adiciona o conteúdo do elemento
            ongDiv.innerHTML = `
                <div class="overlay"></div>
                <div class="d-flex justify-content-between pt-20">
                    <div class="position-relative food-menu-list">
                        <p class="text-capitalize menu-heading mb-10">${ong.name}</p>
                        <p class="mb-4">${ong.description}</p>
                    </div>
                    <div>
                        <div class="text-gradient price2 mr-2 mt-2">Categoria: ${ong.category}</div>
                    </div>
                </div>
                <span class="hr-line"></span>
            `;

            // Adiciona o evento de clique dinamicamente
            const morphicWindowId = `morphic-window-${index + 1}`; // Gera um ID único baseado no índice
            ongDiv.addEventListener("click", () => {
                morphic_window(morphicWindowId);
            });

            tabContainer.appendChild(ongDiv);
        });
    }

    // Adiciona evento de clique no botão "Pesquisar"
    searchButton.addEventListener("click", async () => {
        const query = searchInput.value.trim();
        console.log("Termo de pesquisa enviado:", query); // Log do termo
        if (query === "") {
            alert("Por favor, insira um termo de pesquisa.");
            return;
        }

        const ongs = await fetchOngs(query); // Busca as ONGs na API
        console.log("Resposta da API:", ongs); // Log da resposta da API
        updateOngTab(ongs); // Atualiza a aba com os resultados
    });
});
