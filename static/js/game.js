let player = "X"
let ai = "O"
let gameOver = false
let playerScore = 0
let aiScore = 0

const cells = document.querySelectorAll(".cell")
const difficulty = document.getElementById("difficulty")

const moveSound = new Audio("/static/sounds/move.mp3")
const winSound = new Audio("/static/sounds/win.mp3")
const drawSound = new Audio("/static/sounds/draw.mp3")

const playerScoreEl = document.getElementById("player-score")
const aiScoreEl = document.getElementById("ai-score")

cells.forEach(cell=>{
cell.addEventListener("click", playMove)
})

function playMove(e){

if(gameOver) return

let index = e.target.dataset.index

fetch("/move",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({
move:parseInt(index),
difficulty: difficulty.value
})
})
.then(res=>res.json())
.then(data=>{

setTimeout(()=>{

data.board.forEach((val,i)=>{
cells[i].textContent = val
})

moveSound.play()

if(data.result !== "continue"){

if(data.combo){
data.combo.forEach(i=>{
cells[i].classList.add("win")
})
}

endGame(data.result)

}

}, 500)

})

}

function endGame(result){

gameOver = true

document.getElementById("board").style.display = "none"
document.getElementById("winner-screen").style.display = "block"

if(result === "X"){
playerScore++
playerScoreEl.innerText = playerScore
winSound.play()
document.getElementById("winner-symbol").innerText = "X"
document.getElementById("winner-text").innerText = "Player Wins!"
}

else if(result === "O"){
aiScore++
aiScoreEl.innerText = aiScore
winSound.play()
document.getElementById("winner-symbol").innerText = "O"
document.getElementById("winner-text").innerText = "AI Wins!"
}

else{
drawSound.play()
document.getElementById("winner-symbol").innerText = "🤝"
document.getElementById("winner-text").innerText = "Draw!"
}

}

function restartGame(){

fetch("/reset")
.then(res=>res.json())
.then(data=>{

cells.forEach(cell=>{
cell.textContent=""
})

document.getElementById("board").style.display = "grid"
document.getElementById("winner-screen").style.display = "none"

gameOver = false

})

}