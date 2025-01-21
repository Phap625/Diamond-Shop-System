// Sản phẩm mẫu
const products = [
    { id: 1, name: "Nhẫn Kim Cương", price: 10000000 },
    { id: 2, name: "Dây Chuyền Kim Cương", price: 15000000 },
    { id: 3, name: "Bông Tai Kim Cương", price: 8000000 }
];


// Giỏ hàng
let cart = [];

// Hiển thị sản phẩm mới cập nhật
function displayProducts() {
  const productList = document.getElementById("san-pham-list");
  productList.innerHTML = "";
  products.forEach((product) => {
    const productItem = document.createElement("div");
    productItem.innerHTML = `
            ${product.name} - ${product.price.toLocaleString()} VND
            <button onclick="addToCart(${product.id})">Thêm vào giỏ</button>
        `;
    productList.appendChild(productItem);
  });
}

// Thêm sản phẩm vào giỏ hàng
function addToCart(productId) {
  const product = products.find((p) => p.id === productId);
  const cartItem = cart.find((item) => item.id === productId);
  if (cartItem) {
    cartItem.quantity++;
  } else {
    cart.push({ ...product, quantity: 1 });
  }
  updateCart();
}

// Xóa sản phẩm khỏi giỏ hàng
function removeFromCart(productId) {
  cart = cart.filter((item) => item.id !== productId);
  updateCart();
}

// Cập nhật hiển thị giỏ hàng
function updateCart() {
  const cartDetails = document.getElementById("gio-hang-chi-tiet");
  const totalItems = document.getElementById("tong-so");
  const totalPrice = document.getElementById("tong-tien");

  cartDetails.innerHTML = "";
  let total = 0;
  let count = 0;

  cart.forEach((item) => {
    total += item.price * item.quantity;
    count += item.quantity;

    const cartItem = document.createElement("div");
    cartItem.innerHTML = `
            ${item.name} - ${item.price.toLocaleString()} VND x ${item.quantity}
            <button onclick="removeFromCart(${item.id})">Xóa</button>
        `;
    cartDetails.appendChild(cartItem);
  });

  totalItems.textContent = count;
  totalPrice.textContent = total.toLocaleString();
}


// Tìm kiếm sản phẩm
document.getElementById("search-button").addEventListener("click", () => {
  const searchInput = document
    .getElementById("search-input")
    .value.toLowerCase();
  const results = products.filter((product) =>
    product.name.toLowerCase().includes(searchInput)
  );
  const resultsDiv = document.getElementById("search-results");
  resultsDiv.innerHTML = "";

  if (results.length > 0) {
    results.forEach((product) => {
      const resultItem = document.createElement("div");
      resultItem.textContent = `${product.name} - ${product.price}`;
      resultsDiv.appendChild(resultItem);
    });
  } else {
    resultsDiv.textContent = "Không tìm thấy sản phẩm nào.";
  }
});

// Chạy khi tải trang
document.addEventListener("DOMContentLoaded", () => {
    displayProducts(); // Hiển thị danh sách sản phẩm
    updateCart(); // Cập nhật giỏ hàng ban đầu
});