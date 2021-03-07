function struct(A) {    
    return {value: function() {
        return A;
    }}
}

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    var list = []
    A.forEach(element => {
        list.push(new struct(element));
    });
    return list;
}
A = [4, 3, 5];
t = solution(A);
console.log(t[0].value() === A[0]);
console.log(t[1].value() === A[1]);
console.log(!t[0].hasOwnProperty('value'));
console.log(!t[1].hasOwnProperty('value'));