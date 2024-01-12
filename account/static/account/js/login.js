const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	window.location.href = "/account/register/";
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});