let x = [11, 12, 20, 25,27, 30];
let y = [];
let qtd = 0;
for(let i = 0 ; i < x.length ; i++) {
    if (x[i] % 2 == 0) {
        qtd++;
        y.push(x[i]);
    }
}
document.write(y);
document.write("<br>");
document.write(qtd);

12,20,30<br>3