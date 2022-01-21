var updatebtns = document.getElementsByClassName("update-cart");

for (var i = 0; i < updatebtns.length; i++) {
  updatebtns[i].addEventListener("click", function () {
    var productid = this.dataset.productid;
    var action = this.dataset.action;
    if (user === "AnonymousUser") {
      console.log("Not the authenticated user");
    } else {
      updateUserOrder(productid, action);
    }
  });
}

function updateUserOrder(productid, action) {
  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productid, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}

var updatebtns = document.getElementsByClassName("update-fav");

for (var i = 0; i < updatebtns.length; i++) {
  updatebtns[i].addEventListener("click", function () {
    var productid = this.dataset.productid;
    var action = this.dataset.action;
    if (user === "AnonymousUser") {
      console.log("Not the authenticated user");
    } else {
      updateUserfav(productid, action);
    }
  });
}

function updateUserfav(productid, action) {
  var url = "/update_fav/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productid, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}
