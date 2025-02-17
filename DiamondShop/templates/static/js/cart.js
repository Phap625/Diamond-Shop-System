let updateBtns = document.querySelectorAll('.update-cart');

updateBtns.forEach((btn) => {
    btn.addEventListener('click', function () {
        if (user==="AnonymousUser"){
            alert("Vui lòng đăng nhập!")
        }else{
            let productId = this.dataset.product
            let action = this.dataset.action
            var url = '/cart/add_to_cart/'
            fetch(url , {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify({'productId': productId, 'action': action})
            })
            .then(response => {
                return response.json()
            })
            .then(data => {
                location.reload();
            });
        }
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function toggleDescription(productId) {
        var desc = document.getElementById("desc_" + productId);
        if (desc.classList.contains("text-truncate")) {
            desc.classList.remove("text-truncate");
            event.target.innerText = "Thu gọn";
        } else {
            desc.classList.add("text-truncate");
            event.target.innerText = "Đọc tiếp";
        }
    }