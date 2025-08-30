async function searchProduct() {
  const query = document.getElementById('searchBox').value;
  const res = await fetch(`/search?q=${encodeURIComponent(query)}`);
  const data = await res.json();

  const resultsDiv = document.getElementById('results');
  resultsDiv.innerHTML = '';

  if (data.length === 0) {
    resultsDiv.innerHTML = '<p>No products found.</p>';
    return;
  }

  data.forEach(product => {
    const div = document.createElement('div');
    div.className = 'product';
    div.innerHTML = `
      <h3>${product.name}</h3>
      <p><strong>Vendor:</strong> ${product.vendor}</p>
      <p><strong>Price:</strong> ₹${product.price}</p>
      <a href="${product.link}" target="_blank">View Product</a>
    `;
    resultsDiv.appendChild(div);
  });
}


let sidenav = document.querySelector(".side-navbar");
function shownavbar(){
    sidenav.style.left = "0";
}
function closenavbar(){
    sidenav.style.left = "-50%";
}