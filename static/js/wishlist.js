function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// const addCart = {
//   addProductCart(ProductID, Quantity) {
//       return fetch(`${location.origin}/api/basket/`, {
//           method: 'POST',
//           headers: {
//               'Content-type': 'application/json',
//               'X-CSRFToken': csrftoken,
//               'Authorization': `Bearer ${localStorage.getItem('token')}`
//           },
//           body: JSON.stringify({
//               'product': ProductID,
//               'quantity': Quantity
//           })
//       }).then(response => response.json()).then(data => {
//           document.getElementById('cart-sidebar').innerHTML = '';
//               for (let i in data) {
//                           if (data[i]['product']['product']['in_sale'] == true) {
//                               document.getElementById('cart-sidebar').innerHTML += `
//                               <li class="item first">
//                                   <div class="item-inner"><a class="product-image" title="${data[i]['product']['product']['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i]['product']['product']['name']}" src="${data[i]['product']['cover_image']}"></a>
//                                   <div class="product-details">
//                                       <strong>${data[i]['quantity']}</strong> x <span class="price">${data[i]['product']['product']['new_price'].toFixed(2)}</span>
//                                       <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i]['product']['product']['name']}</a></p>
//                                   </div>
//                                   </div>
//                               </li>`
//                               document.getElementById('top-cart').style.display = 'block'
//                           }
//                           else {
//                               document.getElementsByClassName('mini-products-list')[0].innerHTML += `
//                               <li class="item first">
//                                   <div class="item-inner"><a class="product-image" title="${data[i]['product']['product']['name']}" href="{% url 'product_detail' pk=item.pk %}"><img alt="${data[i]['product']['product']['name']}" src="${data[i]['product']['cover_image']}"></a>
//                                   <div class="product-details">
//                                       <strong>${data[i]['quantity']}</strong> x <span class="price">${data[i]['product']['product']['price'].toFixed(2)}</span>
//                                       <p class="product-name"><a href="{% url 'product_detail' pk=item.pk %}">${data[i]['product']['product']['name']}</a></p>
//                                   </div>
//                                   </div>
//                               </li>`
//                               document.getElementById('top-cart').style.display = 'block'

//                           }
//               }
//       })
//   }
// }

const addProduct = {
  addProductWishlist(ProductID) {
      return fetch(`${location.origin}/api/wishlist/`, {
          method: 'POST',
          headers: {
              'Content-type': 'application/json',
              'X-CSRFToken': csrftoken,
              'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify({
              'item': ProductID
          })
      }).then(response => response.json()).then(data => {
          if (data.success) {
              window.alert(data.message);
          }
      })
  }
}

const deleteProduct = {
  deleteProductWishlist(ProductID) {
      return fetch(`${location.origin}/api/wishlist`, {
          method: 'DELETE',
          headers: {
              'Content-type': 'application/json',
              'X-CSRFToken': csrftoken,
              'Authorization': `Bearer ${localStorage.getItem('token')}`
          },
          body: JSON.stringify({
              'item': ProductID
          })
      });
  }
}


function functionAddToWishlist(ProductID) {
  addProduct.addProductWishlist(ProductID);
}

function removeWishlist(ProductID) {
  deleteProduct.deleteProductWishlist(ProductID)
}

// const deleteProduct_Basket = {
//   deleteProductBasket(ProductID) {
//       return fetch(`${location.origin}/api/basket/`, {
//           method: 'DELETE',
//           headers: {
//               'Content-type': 'application/json',
//               'X-CSRFToken': csrftoken,
//               'Authorization': `Bearer ${localStorage.getItem('token')}`
//           },
//           body: JSON.stringify({
//               'product': ProductID
//           })
//       });
//   }
// }


// function functionAddToBasket(ProductID) {
//   const quantity = 1;
//   addCart.addProductCart(ProductID, quantity);
// }

// function AddToBasketInDetail(ProductID) {
//   const quantity = parseInt(document.getElementById('qty').value);
//   addCart.addProductCart(ProductID, quantity);
// }

// function removeBasket(ProductID) {
//   deleteProduct_Basket.deleteProductBasket(ProductID)
// }


// function updateUserWishlist(productID,action){
//     console.log('user:',user,' is Authenticated, sending data')
//     let url= '/api/update_wishlist/'
//     fetch(url,{
//         method:'PUT',
//         headers:{
//             'Content-Type':'application/json',
//             'X-CSRFToken':csrftoken,
//         },
//         body:JSON.stringify({'productID':productID, 'action':action})
//     }).then((response)=>
//         response.json()
//     ).then(function (data){
//             console.log('data:',data)
//             if (data['deleted'] === true){
//                 itemDeleted(productID,data)
//             } else {
//                 itemAddedToCart(productID, data)
//             }
//             if (data['wishlistItemQuantity']===0){
//                 document.getElementById('wishlist').innerHTML = 'Wishlist'
//             }
//         })
// }


// document.getElementById('wislistBtnss').addEventListener('click', (e) => {
//   postData('http://localhost:8000/API/wishlist/', { product_id: 1 })
//     .then((data) => {
//       console.log(data); // JSON data parsed by `data.json()` call
//     });


// })


// async function postData(url = '', data = {}) {
//   const token = document.cookie.split('; ')
//    console.log(token)
//     const response = await fetch(url, {
//       method: 'POST', // *GET, POST, PUT, DELETE, etc.
//       headers: {
//         'Content-Type': 'application/json',
         
//         'X-CSRFToken': token.toString().substring(10, 42)
//       },
//       body: JSON.stringify(data) // body data type must match "Content-Type" header
//     });
//     return response.json(); // parses JSON response into native JavaScript objects
//   }