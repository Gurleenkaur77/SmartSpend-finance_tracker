$(document).ready(function () {
    const tips = [
        "Track your spending weekly. Small changes = big savings!",
        "Cook at home instead of ordering out.",
        "Use public transport to save on fuel.",
        "Avoid impulse buying — wait 24 hours before a non-essential purchase.",
        "Plan a monthly budget and stick to it.",
        "Unsubscribe from unused subscriptions.",
        "Buy in bulk to save money over time.",
        "Use cash instead of cards for better awareness of spending.",
        "Compare prices online before making purchases.",
        "Set saving goals and reward yourself for achieving them!"
    ];

    $('#show-tip').click(function () {
        const randomIndex = Math.floor(Math.random() * tips.length);
        const selectedTip = tips[randomIndex];

        $('#tip').hide().text(selectedTip).slideDown(300);
    });
    $('#tagline').hover(
    function () {
      // On hover
      $(this).text('Helping u save ❤');
    },
    function () {
      // On hover out
      $(this).text('Helping u save :)');
    });
});
