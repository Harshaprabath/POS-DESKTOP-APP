document.getElementById("loginForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
 
    console.log(username);
    console.log(password);


    const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
    });

    const result = await response.json();
    const messageElement = document.getElementById("message");
    console.log(result);
    
    if (result.success) {
        messageElement.style.color = "green";
        messageElement.textContent = result.message;
        
        // Redirect to the empty page after success
        setTimeout(() => {
            window.location.href = "/dashboard"; // Replace with your next page
        }, 1000);
    } else {
        messageElement.style.color = "red";
        messageElement.textContent = result.message;
    }
});
