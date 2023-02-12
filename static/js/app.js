async function submitGuess(guess) {
    const resp = await axios({
        method: 'GET',
        url: '/submit-word',
        params: { guess: guess }
    });
    return resp.data.result;
}

function updateScore(wordLen) {
    let score = parseInt($('#score').text());
    score += wordLen;
    $('#score').text(score);
}

async function endGame() {
    $('.feedback').remove()
    $('.scoreText').after("<h2 class='endgame'>Time's up!</h2>");
    $('form').off();
    $('form').on('submit', (e) => {
        e.preventDefault();
    })
    await updateStats();
}

async function updateStats() {
    let resp = await axios.post('/update-stats', { score: parseInt($('#score').text()) })
    $('#highest').text(resp.data.highscore)
    $('#numGames').text(resp.data.numgames)
}

// Add event listener for guess submission
$('form').on('submit', async (e) => {
    e.preventDefault();
    $('.feedback').text('')
    const $userGuess = $('.guess');
    const userGuess = $userGuess.val();
    $userGuess.val('')
    let resp = await submitGuess(userGuess)
    if (resp === 'not-word') {
        $('form').after(`<p class="feedback">${userGuess} is not a valid word!</p>`)
    } else if (resp === 'not-on-board') {
        $('form').after(`<p class="feedback">${userGuess} cannot be found on the board!</p>`)
    } else {
        $('form').after(`<p class="feedback">${userGuess} is a valid word on the board!</p>`);
        updateScore(userGuess.length);
    }
})

// Add timer
setTimeout(endGame, 60000)