function ImageSound(imgSoundId, delay) {
    setTimeout(() => {
        const imgSound = document.getElementById(imgSoundId);
        imgSound.classList.remove('hidden');
        imgSound.play();
    }, delay);
}

window.addEventListener('load', () => {
    ImageSound('sacrifice1', 0);
    ImageSound('heartbeat2', 2500);
    ImageSound('sacrifice2', 3000);
    ImageSound('heartbeat3', 5500);
    ImageSound('sacrifice3', 6000);
});
