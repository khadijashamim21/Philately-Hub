let signUpBtn = document.queryselector('.signupbtn');
let signInBtn = document.queryselector('.signinbtn');
let nameField = document.queryselector('.namefield');
let title = document.queryselector('.title');
let underline = document.queryselector('.underline');


signInBtn.addEventListener('click',()=> {
    nameField.style.maxHeight = '0';
    title.innerHTML = 'sign In';
    signUpBtn.classlist.add('disable');
    signUpBtn.classlist.remove('disable');
    underline.style.transform = 'translate(35px)'
    


});