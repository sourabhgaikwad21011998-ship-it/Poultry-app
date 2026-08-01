<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>पोल्ट्री विक्री व हिशोब व्यवस्थापन</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f9; }
        .container { max-width: 500px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: auto; }
        h2 { text-align: center; color: #333; }
        label { font-weight: bold; display: block; margin-top: 10px; }
        input, select { width: 100%; padding: 8px; margin-top: 5px; box-sizing: border-box; }
        .result { background: #e8f5e9; padding: 10px; margin-top: 15px; border-radius: 5px; }
    </style>
</head>
<body>

<div class="container">
    <h2>🐔 चिकन विक्री नोंद (Billing)</h2>
    
    <label>ग्राहकाचे नाव (Customer Name):</label>
    <input type="text" id="custName" placeholder="नाव टाका">

    <label>चिकनचा प्रकार (Chicken Type):</label>
    <select id="chickenType">
        <option>Broiler</option>
        <option>Desi</option>
        <option>Parent</option>
        <option>Layer</option>
    </select>

    <label>पक्ष्यांची संख्या (Bird Qty):</label>
    <input type="number" id="birdQty" oninput="calculate()">

    <label>एकूण वजन (Total Weight in kg):</label>
    <input type="number" id="totalWeight" oninput="calculate()">

    <label>दर प्रति किलो (Rate / Kg):</label>
    <input type="number" id="rate" oninput="calculate()">

    <label>जमा रक्कम (Credit Amount):</label>
    <input type="number" id="credit" oninput="calculate()">

    <div class="result">
        <p><strong>प्रति पक्षी वजन:</strong> <span id="weightPerBird">0</span> kg</p>
        <p><strong>एकूण रक्कम:</strong> ₹<span id="totalAmount">0</span></p>
        <p><strong>उर्वरित बाकी (Balance):</strong> ₹<span id="balance">0</span></p>
    </div>
</div>

<script>
    function calculate() {
        let birdQty = parseFloat(document.getElementById('birdQty').value) || 0;
        let totalWeight = parseFloat(document.getElementById('totalWeight').value) || 0;
        let rate = parseFloat(document.getElementById('rate').value) || 0;
        let credit = parseFloat(document.getElementById('credit').value) || 0;

        let weightPerBird = birdQty > 0 ? (totalWeight / birdQty).toFixed(2) : 0;
        let totalAmount = totalWeight * rate;
        let balance = totalAmount - credit;

        document.getElementById('weightPerBird').innerText = weightPerBird;
        document.getElementById('totalAmount').innerText = totalAmount.toFixed(2);
        document.getElementById('balance').innerText = balance.toFixed(2);
    }
</script>

</body>
</html>
