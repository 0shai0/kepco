const result = document.getElementById("result");
const num = document.querySelectorAll(".num");
const calculate = document.querySelectorAll(".calculate");
const reset = document.getElementById("reset");
const equal = document.getElementById("equal");



// 숫자 클릭 시 result에 값이 들어가는 코드, 값이 없을 때 0을 누를 시 숫자가 추가되지 않는 코드,
// 기본값 0으로 하고 숫자 누르면 0 사라지고 누른 숫자 나오기

for (let i = 0; i < num.length; i++) {
    num[i].addEventListener("click", (e) => {
        const clickNumber = e.target.innerHTML;
        result.textContent += clickNumber;
    });
}



// 사칙연산 클릭 시 result에 값이 들어가는 코드, 연속으로 사칙연산 누를 시 나중에 누른 것이 적용
// 숫자를 아무것도 누르지 않고 누를 시 적용되지 않게 하기

for (let i = 0; i < calculate.length; i++) {
    calculate[i].addEventListener("click", (e) => {
        const clickCalculate = e.target.innerHTML;
        result.textContent += clickCalculate;
      });
}



// C를 누를 시 result에 있던 것이 없어지는 코드

reset.addEventListener("click", (e) => {
    result.textContent = "";
})



// +를 누를 때 더하기 되기

equal.addEventListener("click", (e) => {
    const plus = result.textContent;
    const plusIndex = plus.indexOf("+");
    if (plusIndex !== -1 && plusIndex < plus.length - 1) {
        // '+'가 있고 오른쪽에 숫자가 있는 경우
        const leftplus = plus.substring(0, plusIndex);
        const rightplus = plus.substring(plusIndex + 1);
        const finalResult = parseInt(leftplus, 10) + parseInt(rightplus, 10);
        result.textContent = finalResult;
    } else {
        // '+'가 없거나 오른쪽에 숫자가 없는 경우
        result.textContent = parseInt(plus, 10);
    }
});


// -를 누를 때 빼기 되기

equal.addEventListener("click", (e) => {
    const minus = result.textContent;
    const minusIndex = minus.indexOf("-");
    if (minusIndex !== -1 && minusIndex < minus.length - 1) {
        // '-'가 있고 오른쪽에 숫자가 있는 경우
        const leftMinus = minus.substring(0, minusIndex);
        const rightMinus = minus.substring(minusIndex + 1);
        const finalResult = parseInt(leftMinus, 10) - parseInt(rightMinus, 10);
        result.textContent = finalResult;
    } else {
        // '-'가 없거나 오른쪽에 숫자가 없는 경우
        result.textContent = parseInt(minus, 10);
    }
});



// %를 누를 때 나누기 되기

equal.addEventListener("click", (e) => {
    const divide = result.textContent;
    const divideIndex = divide.indexOf("%");
    if (divideIndex !== -1 && divideIndex < divide.length - 1) {
        // '-'가 있고 오른쪽에 숫자가 있는 경우
        const leftdivide = divide.substring(0, divideIndex);
        const rightdivide = divide.substring(divideIndex + 1);
        const finalResult = parseInt(leftdivide, 10) % parseInt(rightdivide, 10);
        result.textContent = finalResult;
    } else {
        // '-'가 없거나 오른쪽에 숫자가 없는 경우
        result.textContent = parseInt(divide, 10);
    }
});



// x를 누를 때 곱하기 되기

equal.addEventListener("click", (e) => {
    const multiply = result.textContent;
    const minusIndex = multiply.indexOf("x");
    if (multiplyIndex !== -1 && multiplyIndex < multiply.length - 1) {
        // '-'가 있고 오른쪽에 숫자가 있는 경우
        const leftmultiply = multiply.substring(0, multiplyIndex);
        const rightmultiply = multiply.substring(multiplyIndex + 1);
        const finalResult = parseInt(leftmultiply, 10) * parseInt(rightmultiply, 10);
        result.textContent = finalResult;
    } else {
        // '-'가 없거나 오른쪽에 숫자가 없는 경우
        result.textContent = parseInt(multiply, 10);
    }
});