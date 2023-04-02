const buttons = document.getElementsByName('rootSelect');
// const show1 = document.getElementsByName('showdivs');

buttons.forEach(button => {
    button.addEventListener('click', handleClick, false);
});
// show1.forEach(button => {
//     button.addEventListener('click', handleClick, true);
// });

function handleClick() {
    document.getElementById('root_Select').style.display = "block";
    // document.getElementById('root_Select').style.display = "block".e.preventDefault();
    // document.getElementById('rootblock').style.display = "block".e.preventDefault();

}









// function handleClick() {
//   let key_Disp = document.createElement("p");
//   key_Disp.className = 'keyDisp'
//   var parent = document.getElementById('keyIs');
//   key_Disp.id = this.getAttribute('value');
//     if (parent.children.length === 0) { 
//     document.getElementById('keyIs').appendChild(key_Disp);
//     key_Disp.textContent = this.getAttribute('value') 
//     } 
//     else  {
//       let oldKey = parent.childNodes[1];
//       document.getElementById('keyIs').removeChild(oldKey);
//       document.getElementById('keyIs').appendChild(key_Disp);
//       key_Disp.textContent = this.getAttribute('value')
//     }

//   }