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
function statusbar() {
  var status = document.getElementById("status").innerText;
  console.log(status);
  var bar = document.getElementById("progressbar");
  if (status == "PROSSED") {
    for (i = 0; i < 1; i++) {
      var li = document.createElement("li");
      li.classList.add("active");
      li.classList.add("step0");
      bar.appendChild(li);
    }
    for (i = 0; i < 3; i++) {
      var li = document.createElement("li");
      li.classList.add("step0");
      bar.appendChild(li);
    }
  }
  if (status == "SHIPING") {
    for (i = 0; i < 2; i++) {
      var li = document.createElement("li");
      li.classList.add("active");
      li.classList.add("step0");
      bar.appendChild(li);
    }
    for (i = 0; i < 2; i++) {
      var li = document.createElement("li");
      li.classList.add("step0");
      bar.appendChild(li);
    }
  }
  if (status == "ONTHEWAY") {
    for (i = 0; i < 3; i++) {
      var li = document.createElement("li");
      li.classList.add("active");
      li.classList.add("step0");
      bar.appendChild(li);
    }
    for (i = 0; i < 1; i++) {
      var li = document.createElement("li");
      li.classList.add("step0");
      bar.appendChild(li);
    }
  }
  if (status == "RECIVED") {
    for (i = 0; i < 4; i++) {
      var li = document.createElement("li");
      li.classList.add("active");
      li.classList.add("step0");
      bar.appendChild(li);
    }
  }
}
