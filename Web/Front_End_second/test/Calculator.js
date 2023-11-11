const result = document.getElementById("result");
const num = document.querySelectorAll(".num");
const zero = document.getElementById("zero");
const calculate = document.querySelectorAll(".calculate");
const reset = document.getElementById("reset");
const equal = document.getElementById("equal");



// 숫자 클릭 시 result에 숫자가 들어가는 코드, result 값이 없을 때 0을 누를 시 0이 추가되지 않는 코드,

for (let i = 0; i < num.length; i++) {
    num[i].addEventListener("click", (e) => {
        const clickNumber = e.target.innerHTML;
        if (result.textContent === "" && clickNumber === "0"){

        } else {
            result.textContent += clickNumber;
        } 
    });
}



// calculate 클릭 시 result에 값이 들어가는 코드, 연속으로 calculate를 누를 시 처음에 누른 것만 적용
// 숫자를 아무것도 누르지 않고 calculate 누를 시 적용되지 않는 코드

for (let i = 0; i < calculate.length; i++) {
    calculate[i].addEventListener("click", (e) => {
        const clickCalculate = e.target.innerHTML;
        if (result.textContent === "" || result.textContent.endsWith("+") || result.textContent.endsWith("-")
            || result.textContent.endsWith("x") || result.textContent.endsWith("/")) {
            
        } else {
            result.textContent += clickCalculate;
        }
    });
}



// C를 누를 시 result가 공백이 되는 코드

reset.addEventListener("click", (e) => {
    result.textContent = "";
})



// "=" 클릭 시 result에 연산자가 포함되어 있고 연산자 양 쪽에 숫자가 있을 경우 계산하는 코드

equal.addEventListener("click", (e) => {
    const outcome = result.textContent;

    // 각 연산자를 개별적으로 찾기 위해 연산자에 변수 선언
    const plusIdx = outcome.indexOf("+");
    const minusIdx = outcome.indexOf("-");
    const multiplyIdx = outcome.indexOf("x");
    const divisionIdx = outcome.indexOf("/");

    // 연산자가 있는지 확인하는 변수 선언
    const check = plusIdx !== -1 || minusIdx !== -1 || multiplyIdx !== -1 || divisionIdx !== -1;

    // 연산자가 있으면서 연산자가 처음에 있지 않을 시
    if (check && check > 0 && check < outcome.length-1) {
        let leftOutcome, rightOutcome, finalResult;

        // 연산자에 따라 해당 연산 수행
        if (plusIdx !== -1) {
            leftOutcome = outcome.substring(0, plusIdx);
            rightOutcome = outcome.substring(plusIdx + 1);
            finalResult = parseFloat(leftOutcome) + parseFloat(rightOutcome);
        } else if (minusIdx !== -1) {
            leftOutcome = outcome.substring(0, minusIdx);
            rightOutcome = outcome.substring(minusIdx + 1);
            finalResult = parseFloat(leftOutcome) - parseFloat(rightOutcome);
        } else if (multiplyIdx !== -1) {
            leftOutcome = outcome.substring(0, multiplyIdx);
            rightOutcome = outcome.substring(multiplyIdx + 1);
            finalResult = parseFloat(leftOutcome) * parseFloat(rightOutcome);
        } else if (divisionIdx !== -1) {
            leftOutcome = outcome.substring(0, divisionIdx);
            rightOutcome = outcome.substring(divisionIdx + 1);
            finalResult = parseFloat(leftOutcome) / parseFloat(rightOutcome);
        }

        result.textContent = finalResult;

    } else if (check === 0) {
        result.textContent = outcome.substring(1);
    } else {
        result.textContent = outcome.slice(0,- 1);
    }
});

