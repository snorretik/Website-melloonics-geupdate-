// Javascript file

let game = () => {
    // content game

    const btn = document.querySelector('#gameButton');
    btn.addEventListener('click', (e) => {
        // content game (further)
        let playerDecision = "";

        let formElemts = document.getElementsByName("game");
        for (let i = 0; i < formElemts.length; i++) {
            if (formElemts[i].checked) {
                playerDecision = formElemts[i].value;
            }
        }

        let pcDecision = Math.ceil((Math.random() * 3));

        // console.log(`playerDecision = ${playerDecision}`);
        // console.log(`pcDecision = ${pcDecision}`);

        gameLogic(playerDecision, pcDecision);

    });

    let gameLogic = (a, b) => {
        // game logic

        // console.log(a);
        // console.log(b);

        let pcDecisionOut = b;

        const outputPcDecision = document.querySelector("#computerOutput");
        switch(b) {
            case 1:
                outputPcDecision.textContent = "Computer koos: Steen";
                break;
            case 2:
                outputPcDecision.textContent = "Computer koos: Papier";
                break;
            case 3:
                outputPcDecision.textContent = "Computer koos: Schaar";
                break;
            default:
                outputPcDecision.textContent = "Error translating PC decision..."
        }

        const result = document.querySelector("#result");

        switch(a) {
            case 'steen':
                switch(b) {
                    case 1:
                        result.textContent = "Het is een gelijkspel.";
                        break;
                    case 2:
                        result.textContent = "Je hebt verloren.";
                        break;
                    case 3:
                        result.textContent = "Je hebt gewonnen!";
                        break;
                    default:
                        result.textContent = "Something went wrong...";
                }
                break;

            case 'papier':
                switch(b) {
                    case 1:
                        result.textContent = "Je hebt gewonnen!";
                        break;
                    case 2:
                        result.textContent = "Het is een gelijkspel.";
                        break;
                    case 3:
                        result.textContent = "Je hebt verloren.";
                        break;
                    default:
                        result.textContent = "Something went wrong...";
                }
                break;

            case 'schaar':
                switch(b) {
                    case 1:
                        result.textContent = "Je hebt verloren.";
                        break;
                    case 2:
                        result.textContent = "Je hebt gewonnen!";
                        break;
                    case 3:
                        result.textContent = "Het is een gelijkspel.";
                        break;
                    default:
                    result.textContent = "Something went wrong...";
                }
                break;
            default:
                result.textContent = "Something went in the first switch";
        }
    }    
}

game();

