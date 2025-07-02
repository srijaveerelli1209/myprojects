let arr=[1,2,3,4,5,6,7,8,9,10];
console.log(arr);
for(let val of arr){
    console.log(val);
    if(val%2==0){
        console.log(val);
    }
}
arr.push(30);
console.log(arr);
arr.pop();
console.log(arr);