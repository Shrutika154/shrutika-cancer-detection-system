async function predict() {
    const features = [
        parseFloat(document.getElementById("f1").value),
        parseFloat(document.getElementById("f2").value),
        parseFloat(document.getElementById("f3").value),
        parseFloat(document.getElementById("f4").value),
        parseFloat(document.getElementById("f5").value),
        parseFloat(document.getElementById("f6").value),
        parseFloat(document.getElementById("f7").value)
    ];

    let response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({features: features})
    });

    let result = await response.json();

    document.getElementById("result").innerHTML = 
        "Prediction: " + result.prediction;
}
