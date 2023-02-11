async function submitGuess(guess) {
    const resp = await axios({
        method: 'GET',
        url: '/submit-word',
        params: { guess: guess }
    });
    return resp.data.result;
}

$('form').on('submit', async (e) => {
    e.preventDefault();
    const $userGuess = $('.guess');
    const userGuess = $userGuess.val();
    console.log(userGuess, 'first')
    let resp = await submitGuess(userGuess)
    console.log(userGuess, 'second')
    if (resp === 'not-word') {
        $('form').after(`<p>${userGuess} is not a valid word!</p>`)
    } else if (resp === 'not-on-board') {
        $('form').after(`<p>${userGuess} cannot be found on the board!</p>`)
    } else {
        $('form').after(`<p>${userGuess} is a valid word on the board!</p>`)
    }
})

// $('form').on('submit', async function (e) {
//     e.preventDefault();
//     const $userGuess = $('.guess');
//     const userGuess = $userGuess.val();
//     console.log(userGuess, 'first')
//     let resp = await axios({
//         method: 'GET',
//         url: '/submit-word',
//         params: { guess: userGuess }
//     });
//     console.log(userGuess, 'second')
//     if (resp.data.result === 'not-word') {
//         $('.form').after(`<p>${userGuess} is not a valid word!</p>`)
//     } else if (resp.data.result === 'not-on-board') {
//         $('.form').after(`<p>${userGuess} cannot be found on the board!</p>`)
//     } else {
//         $('.form').after(`<p>${userGuess} is a valid word on the board!</p>`)
//     }
// })