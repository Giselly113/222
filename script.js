async function carregarPromocoes(termoBusca) {
  try {
      const response = await axios.get(`http://127.0.0.1:5000/buscar?termo=${encodeURIComponent(termoBusca)}`);
      const produtos = response.data;

      const grid = document.querySelector('.grid-promocoes');
      grid.innerHTML = "";

      produtos.forEach(promo => {
          const promoElement = `
              <div class="promocao">
                  <img src="${promo.image}" alt="${promo.title}">
                  <h3>${promo.title}</h3>
                  <p class="preco">
                      <a href="${promo.link}" target="_blank" class="btn-comprar">${promo.price}</a>
                  </p>
              </div>
          `;
          grid.innerHTML += promoElement;
      });
  } catch (error) {
      console.error("Erro ao carregar promoções:", error);
  }
}

document.getElementById("searchButton").addEventListener("click", () => {
  const termoBusca = document.getElementById("searchInput").value;
  carregarPromocoes(termoBusca);
});
