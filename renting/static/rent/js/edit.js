
const uploadFile = (e) => {
    const inputTarget = e.target;
    const inputData = inputTarget.getAttribute("data-input-id");
    const imgSpan = document.getElementById(`prev-${inputData}`);
    const imgInput = document.getElementById(`picture__input${inputData}`);
    const allInput = document.getElementsByClassName("picture__input");
    const file = inputTarget.files[0];

    for (let i = 0; i < allInput.length; i++) {
        console.log(allInput[i].value, 'VALUE');
    }

    if (file) {
        const reader = new FileReader();

        reader.addEventListener("load", function (e) {
        const readerTarget = e.target;

        imgSpan.innerHTML = "";

        // if (imgInput.value){
        //     imgInput.value = "";
        // }
        // console.log(imgInput.value, 'VALUE');

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


