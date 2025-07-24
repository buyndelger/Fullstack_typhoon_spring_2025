const display = document.getElementById("display");
const buttons = document.querySelectorAll(".btn");
const themeToggle = document.querySelector(".theme-toggle");

let currentInput = "";
let operator = "";
let firstNumber = "";

// Theme toggle
themeToggle.addEventListener("click", () => {
  document.body.classList.toggle("light");
  document.body.classList.toggle("dark");
});

// Button logic
buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const value = btn.textContent;

    if (value === "AC") {
      currentInput = "";
      operator = "";
      firstNumber = "";
      display.textContent = "0";
    } else if (value === "C") {
      currentInput = currentInput.slice(0, -1);
      display.textContent = currentInput || "0";
    } else if (value === "=") {
      if (firstNumber && operator && currentInput) {
        try {
          let result = eval(
            firstNumber +
              operator.replace("×", "*").replace("÷", "/").replace("−", "-") +
              currentInput
          );
          display.textContent = result;
          currentInput = result.toString();
          firstNumber = "";
          operator = "";
        } catch {
          display.textContent = "Error";
        }
      }
    } else if ("÷×−+".includes(value)) {
      if (currentInput) {
        firstNumber = currentInput;
        operator = value;
        currentInput = "";
      }
    } else {
      currentInput += value;
      display.textContent = currentInput;
    }
  });
});

