let nota = 4;
let func;
if (nota >= 6) {
    func = function() {
        return 'Aprovado';
    }
} else if (nota >= 3 && !(nota >= 6)) {
    func = function() {
        return 'Recuperação';
    }
} else {
    func = function() {
        return 'Repovado';
    }
}

var teste = (nota >= 3 && !nota >= 6) ? true : false;
var teste1 = (!nota >= 6) ? true : false;
var teste2 = (nota <= 6) ? true : false;
console.log(func);
console.log(typeof(func));
console.log(teste);
console.log(teste1);
console.log(teste2);