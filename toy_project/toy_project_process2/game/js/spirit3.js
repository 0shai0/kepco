    const content = document.querySelector('.hidden');


    function ImageSound(imgSoundId, delay) {
        setTimeout(() => {
            const imgSound = document.getElementById(imgSoundId);
            imgSound.classList.remove('hidden');
            imgSound.play();
        }, delay);
    }

    // 페이지가 로드될 때 해당 시간에 맞춰 사진과 소리가 나옴
    window.addEventListener("load", () => {
        ImageSound('sacrifice1', 0);
        ImageSound('heartbeat2', 2500);
        ImageSound('sacrifice2', 3000);
        ImageSound('heartbeat3', 5500);
        ImageSound('sacrifice3', 6000);
        content.style.opacity = 1;
    });
