// board
let board;
let boardWidth = 750;
let boardHeight = 250;
let context;

// dino
let dinoWidth = 88;
let dinoHeight = 94;
let dinoX = 50;
let dinoY = boardHeight - dinoHeight;
let dinoImg;

let dino = {
    x: dinoX,
    y: dinoY,
    width: dinoWidth,
    height: dinoHeight
}

window.onload = function() {
    board = document.getElementById("board");
    board.height = boardHeight;
    board.width = boardWidth;

    context = board.getContext("2d"); // used for drawing on the board

    // draw inttal dinosaur
    //context.fillstyle = "green";
    //context.fillRect(dino.x, dinoY, dino.width, dino.height);

    
}
