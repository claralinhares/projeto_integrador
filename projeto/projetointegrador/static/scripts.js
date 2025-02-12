function abrirCamera() {
    // https://scanapp.org/html5-qrcode-docs/docs/intro
    let html5QrcodeScanner = new Html5QrcodeScanner(
        "reader",
        { fps: 10, qrbox: { width: 250, height: 250 } },
        /* verbose= */ false
    );

    console.log(html5QrcodeScanner);

    html5QrcodeScanner.render(async (decodedText, decodedResult) => {
        console.log(`Code matched = ${decodedText}`, decodedResult);

        const resposta = await fetch(
            "/api/inscricao/validar/?qrcode=" + decodedText
        );
        const data = await resposta.json();
        console.log(data);
        if (data.status === "success") {
            alert(
                `Inscrição encontrada!\nNome: ${data.nome}\nEmail: ${data.email}`
            );
        } else {
            alert("Inscrição não encontrada!");
        }

        console.log(resposta);
        //await html5QrcodeScanner.stop();
    });
}

// Função para rolar até o formulário
function scrollToForm() {
    document
        .getElementById("subscription-form")
        .scrollIntoView({ behavior: "smooth" });
}

// Validação em tempo real dos campos
function validateField(input) {
    const feedback = document.getElementById("feedback");
    const emailRegex = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;

    if (input.type === "email") {
        if (!emailRegex.test(input.value)) {
            feedback.style.display = "block";
            feedback.className = "feedback error";
            feedback.innerText = "Email inválido. Verifique o formato.";
        } else {
            feedback.style.display = "none";
        }
    }
}

// Função para lidar com o envio do formulário
function handleSubmit(event) {
    event.preventDefault(); // Evita o envio padrão do formulário

    // Desabilitar o botão de envio enquanto processa
    const button = document.getElementById("submit-button");
    button.disabled = true;
    button.innerHTML = "Enviando...";

    // Simula o envio do formulário com um tempo de espera (ex: AJAX)
    setTimeout(function () {
        const feedback = document.getElementById("feedback");
        const success = true; // Aqui você pode colocar sua lógica real de backend

        if (success) {
            feedback.className = "feedback success";
            feedback.innerHTML = "Você foi inscrito com sucesso!";
            feedback.style.display = "block";
        } else {
            feedback.className = "feedback error";
            feedback.innerHTML = "Ocorreu um erro. Tente novamente.";
            feedback.style.display = "block";
        }

        // Reabilitar o botão e resetar o texto
        button.innerHTML = "Inscrever Agora";
        button.disabled = false;
    }, 2000); // Simula um tempo de processamento
}
