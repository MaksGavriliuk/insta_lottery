let participants = [];

async function loadParticipants() {
    const response = await fetch('participants.json');
    const data = await response.json();
    participants = data.participants;
}

async function drawWinner() {
    if (participants.length === 0) {
        document.getElementById('winner').innerText = "Нет участников.";
        return;
    }

    let winner = "";
    const displayDuration = 3000;
    const intervalDuration = 150;

    const intervalId = setInterval(() => {
        winner = participants[Math.floor(Math.random() * participants.length)];
        document.getElementById('winner').innerText = winner;
    }, intervalDuration);

    setTimeout(() => {
        clearInterval(intervalId);
        const winnerElement = document.getElementById('winner');
        winnerElement.innerHTML = `<b>${winner}</b>`;

        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                confetti({
                    particleCount: 2000,
                    spread: 700,
                    origin: {
                        x: Math.random(),
                        y: Math.random() * 0.5
                    }
                });
            }, i * 200);
        }
    }, displayDuration);
}

loadParticipants();

document.getElementById('drawButton').addEventListener('click', drawWinner);