function solve(year, month, day) {
    let today = new Date(year, month - 1, day);
    today.setDate(today.getDate()- 1);
    let curr_date = today.getDate();
    let curr_month = today.getMonth();
    let curr_year = today.getFullYear();
    console.log(`${curr_year}-${curr_month + 1}-${curr_date}`)
}