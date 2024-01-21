

document.addEventListener("DOMContentLoaded", function() {
	const uploadFile = (e) => {
		const inputTarget = e.target;
		const inputData = inputTarget.getAttribute("data-input-id");
		const imgSpan = document.getElementById(`prev-${inputData}`);
		const file = inputTarget.files[0];
	
		if (file) {
			const reader = new FileReader();
	
			reader.addEventListener("load", function (e) {
			const readerTarget = e.target;
	
			const img = document.createElement("img");
			img.src = readerTarget.result;
			img.classList.add("picture__img");
	
			imgSpan.innerHTML = "";
			imgSpan.appendChild(img);
			});
	
			reader.readAsDataURL(file);
		} else {
			imgSpan.innerHTML = pictureImageTxt;
		}
	}	

	const img1 = document.getElementById("picture__input1");
	const img2 = document.getElementById("picture__input2");
	const img3 = document.getElementById("picture__input3");
	const img4 = document.getElementById("picture__input4");
	const img5 = document.getElementById("picture__input5");
	const img6 = document.getElementById("picture__input6");
	const img7 = document.getElementById("picture__input7");
	const img8 = document.getElementById("picture__input8");
	const img9 = document.getElementById("picture__input9");
	const img10 = document.getElementById("picture__input10");


	img1.addEventListener("change", uploadFile);
	img2.addEventListener("change", uploadFile);
	img3.addEventListener("change", uploadFile);
	img4.addEventListener("change", uploadFile);
	img5.addEventListener("change", uploadFile);
	img6.addEventListener("change", uploadFile);
	img7.addEventListener("change", uploadFile);
	img8.addEventListener("change", uploadFile);
	img9.addEventListener("change", uploadFile);
	img10.addEventListener("change", uploadFile);

	const pictureImage = document.getElementsByClassName("picture__image");
	const pictureImageTxt = "Choose an image";

	// HTMLCollection'i diziye dönüştürme
	const imageArray = Array.from(pictureImage);

	// Diziyi forEach ile döngüye alarak her bir elemanın içeriğini değiştirme
	imageArray.forEach(element => {
		element.innerHTML = pictureImageTxt; // Örnek olarak alt özelliğine metin atama
	});

	
});

