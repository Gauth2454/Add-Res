const allInputs = document.querySelectorAll('.myInp');
const allButtons = document.querySelectorAll('.btnCopy');

allButtons.forEach((button, index) => {
    button.onclick = function () {
        const input = allInputs[index]
        input.select();
        input.setSelectionRange(0, 99999); // For mobile devices
        navigator.clipboard.writeText(input.value);
    }
});

// Here's how it works:

// We use querySelectorAll('.myInp') to get all the elements with the class "myInp". This gives us a list of all your input boxes.
// We do the same for the buttons with the class "btnCopy".
// The forEach loop goes through each button, one by one. The index tells us which number button we're on (0 for the first, 1 for the second, and so on).
// Inside the loop, allInputs[index] gets the input box that matches the current button's number. So, the first button will highlight the first input, the second button will highlight the second input, and so on.
// This way, no matter which button you click, it will highlight the text in the right input box!