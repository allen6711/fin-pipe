let csvPath = "";
let payees = [];

async function uploadCSV() {
    const fileInput = document.getElementById("csvFile");
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const res = await fetch("http://localhost:5050/upload_csv", {
        method: "POST",
        body: formData
    });
    const data = await res.json();
    csvPath = data.csv_path;
    payees = data.payees;

    const container = document.getElementById("payeeContainer");
    container.innerHTML = "<h2>Categorize Payees</h2>";

    payees.forEach(p => {
        const div = document.createElement("div");
        div.className = "payee-row";  // ✅ 加上 class，讓後續 JS 能抓到

        div.innerHTML = `
            <span class="payee-name">${p}</span>
            <select>
                <option value="01_Dining">Dining</option>
                <option value="02_Clothing">Clothing</option>
                <option value="03_Housing">Housing</option>
                <option value="04_Furniture">Furniture</option>
                <option value="05_Transportation">Transportation</option>
                <option value="06_Vehicles">Vehicles</option>
                <option value="07_Daily Necessities">Daily Necessities</option>
                <option value="08_Gift">Gift</option>
                <option value="09_Health">Health</option>
                <option value="10_Education">Education</option>
                <option value="11_Entertainment">Entertainment</option>
                <option value="12_Travel">Travel</option>
                <option value="13_Service">Service</option>
                <option value="14_Others">Others</option>
            </select>
        `;
        container.appendChild(div);
    });
}

document.getElementById("submit-categories").addEventListener("click", async () => {
    const mapping = {};
    const rows = document.querySelectorAll(".payee-row");

    rows.forEach(row => {
        const payee = row.querySelector(".payee-name").textContent.trim().toUpperCase();
        const category = row.querySelector("select").value;
        mapping[payee] = category;
    });

    console.log("🔍 Mapping sent to backend:", mapping);

    const res = await fetch("http://localhost:5050/submit_categories", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            mapping: mapping,
            csv_path: csvPath
        })
    });

    const data = await res.json();
    alert("✅ 已成功寫入 Google Sheet！");
});
