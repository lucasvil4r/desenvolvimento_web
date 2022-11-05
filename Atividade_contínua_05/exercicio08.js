function funcao(vetor, x) {
    let i = 0;
    for (i = 0 ; i < vetor.length && vetor[i] != x ; i = i + 1) {}
        if (i < vetor.length) {
            return true;
        } else {
            return false;
        }
}

let pessoas = ['Ana', 'Beatriz', 'Carlos', 'Daniel', 'Eduardo'];
let a = funcao(pessoas, 'Ana');
let b = funcao(pessoas, 'Joao');
let c = funcao(pessoas, 'Eduardo');
let d = funcao(pessoas, 'Fabiana');

console.log(a);
console.log(b);
console.log(c);
console.log(d);