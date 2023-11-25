function show() {
    document.querySelector(".background").classList.add("show");
}

function close() {
    document.querySelector(".background").classList.remove("show");
}

document.querySelector("#show").addEventListener('click', show);
document.querySelector("#close").addEventListener('click', close);
