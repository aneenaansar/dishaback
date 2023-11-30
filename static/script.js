// menu bar js

const menuIcon = document.getElementById('menuicon')
const closeIcon = document.getElementById('closeicon')
const slideMenu = document.getElementById('slidemenu')

menuIcon.addEventListener('click', ()=> {
   slideMenu.classList.toggle('show')
})

closeIcon.addEventListener('click', ()=> {
   slideMenu.classList.remove('show')
})


//  first popup

// const popup = document.getElementById('pop');
// const button = document.getElementById('up');
// const button2 = document.getElementById('uping');
// const button3 = document.getElementById("respo")
// const cancelbutton = document.getElementById("cancelbutton")
// let isLeft = true;

// button.addEventListener('click', () => {
//     if (isLeft) {
//         popup.style.left = '50%';
//     }else {
//         popup.style.left = '-300px';
//     }
//     isLeft = !isLeft;
// });

// button2.addEventListener('click', () => {
//     if (isLeft) {
//         popup.style.left = '50%';
//     }else {
//         popup.style.left = '-300px';
//     }
//     isLeft = !isLeft;
// });
// button3.addEventListener('click', () => {
//     if (isLeft) {
//         popup.style.left = '50%';
//     }else {
//         popup.style.left = '-300px';
//     }
//     isLeft = !isLeft;
// });
// cancelbutton.addEventListener('click', () => {
//     if (isLeft) {
//         popup.style.left = '50%';
//     }else {
//         popup.style.left = '-300px';
//     }
//     isLeft = !isLeft;
// });




