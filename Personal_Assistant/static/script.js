function updateCurrencyValues() {
  fetch("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5")
    .then(response => response.json())
    .then(data => {
      for (let item of data) {
        if (item.ccy === "USD") {
          document.getElementById("usd-buy-value").textContent = item.buy;
          document.getElementById("usd-sale-value").textContent = item.sale;
        } else if (item.ccy === "EUR") {
          document.getElementById("eur-buy-value").textContent = item.buy;
          document.getElementById("eur-sale-value").textContent = item.sale;
        }
      }
    })
    .catch(error => console.log(error));
}

updateCurrencyValues();
setInterval(updateCurrencyValues, 60000);
