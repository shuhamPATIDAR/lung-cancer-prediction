document.addEventListener("DOMContentLoaded", function() {
    // Function to set the result, shapes, and button color dynamically
    const riskLevel = "{{ risk_level }}"; // Ensure this variable is correctly passed from the server
    const resultDiv = document.getElementById('prediction-result');
    const homeBtn = document.getElementById('home-btn');
    const shapeOne = document.getElementById('shape-one');
    const shapeTwo = document.getElementById('shape-two');

    // Update the content and styling based on the risk level
    if (riskLevel === 'low') {
        resultDiv.textContent = 'Low Risk';
        resultDiv.classList.add('low-risk');
        shapeOne.classList.add('low-risk-shape');
        shapeTwo.classList.add('low-risk-shape');
        homeBtn.classList.add('low-risk-btn');
    } else if (riskLevel === 'medium') { // Added medium case
        resultDiv.textContent = 'Medium Risk';
        resultDiv.classList.add('medium-risk');
        shapeOne.classList.add('medium-risk-shape');
        shapeTwo.classList.add('medium-risk-shape');
        homeBtn.classList.add('medium-risk-btn');
    } else if (riskLevel === 'high') {
        resultDiv.textContent = 'High Risk';
        resultDiv.classList.add('high-risk');
        shapeOne.classList.add('high-risk-shape');
        shapeTwo.classList.add('high-risk-shape');
        homeBtn.classList.add('high-risk-btn');
    }
});
