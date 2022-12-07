// class Queue{
//     constructor(){
//         this.arr=[]

//     }
//     adding(element){
//         this.arr.push(element)
//     }
//     removing(element){
//         this.arr.shift()
//     }
// }
// queue= new Queue
class stack{
    constructor(){
        this.arr=[]

    }
    adding(element){
        this.arr.pop(element)

    }removing(element){
        this.arr.unshift()
    }
}console.log(10)
stack.adding(20)
stack.adding(30)
console.log(stack)
