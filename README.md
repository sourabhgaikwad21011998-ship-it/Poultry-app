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
