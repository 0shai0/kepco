let persons = null;
document.querySelector('#projector').addEventListener('click', () => {
    if(confirm('재배치')) {
        persons = [
            '김태영', '김건우', '김담향', '김나영', '이재빈', '명하영', '강다솜', '조가영',
                '이윤주', '조정아', '김동일', '윤여록', '김수호', '이승찬', '임태환', '박정현', '장성호', '강건희', '유준하'
        ];
        persons.sort(() => Math.random() - 0.5);
        for(let i = 1; i <= persons.length; i++) {
            document.querySelector(
            `.wrapper > div:nth-child(${i})`).innerHTML = persons[i-1];
        }
    }
});