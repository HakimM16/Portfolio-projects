var playerRed = "R";
var playerYellow = "Y";
var currPlayer = playerRed;

var gameOver = false;
var board;

var rows = 6;
var columns = 7;

window.onload = function() {
    setGame();
}

function setGame() {
    board = [];

    for (let r = 0; r < rows; r++) {
        let row = [];
        for (let c = 0; c < columns; c++) {
            // JS 
            row.push(' ');

            //HTML
            let tile = document.createElement("div");
            tile.id = r.toString() + "-" + c.toString();
            // The code above creates the index of each tile on the board
            // e.g. [2,7] or [0,1]
            tile.classList.add("tile")
            document.getElementById("Board").append(tile);
            // We create a tag like this: <div id="0-0" class="tile"></div>
            // and we append it into our div that contains the id "board"
        }
        board.push(row);
    }
}