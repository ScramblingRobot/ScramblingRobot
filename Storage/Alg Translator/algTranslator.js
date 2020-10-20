document.querySelector("#file-input").addEventListener('change', function() {
	// files that user has chosen
	var all_files = this.files;
	if(all_files.length == 0) {
		alert('Error : No file selected');
		return;
	}

	// first file selected by user
    var text = "";
    let families = ["R", "L", "U", "D", "F", "B"]

    for (var i = 0; i < all_files.length; i++) {
        var file = all_files[i];

        // files types allowed
        var allowed_types = [ 'text/plain' ];
        if(allowed_types.indexOf(file.type) == -1) {
            alert('Error : Incorrect file type');
            return;
        }

        // file validation is successful
        // we will now read the file

        var reader = new FileReader();

        // file reading started
        reader.addEventListener('loadstart', function() {
            document.querySelector("#file-input-label").style.display = 'none'; 
        });

        // file reading finished successfully
        reader.addEventListener('load', function(e) {
            text = text + "<br><br><b>" + e.target.fileName + "</b><br><br>" + e.target.result;
            text = text.replace(/\r\n?/g, '<br><br>');
            newText = ""
            var scrambles = text.split("<br><br>");
            for (var i = 0; i < scrambles.length; i++) {
                var scramble = scrambles[i];

                // if it is a scramble
                if (families.includes(scramble.charAt(0))) {
                    scrambles[i] = transformToRobot(scramble)
                }
                
                newText = newText + scrambles[i] + "<br><br>"
            }

            // contents of the file
            document.querySelector("#contents").innerHTML = newText;
        });

        // file reading failed
        reader.addEventListener('error', function() {
            alert('Error : Failed to read file');
        });

        // read as text file
        reader.fileName = file.name
        reader.readAsText(file);
    }
});

function transformToRobot(scramble) {
    var moves = scramble.split(" ");
    var newScramble = "";
    var length = moves.length
    for (var i = 0; i < length; i++) {
        if (moves[i].charAt(0) == "F") {
            for (var j = moves.length; j > i; j--) {
                moves[j] = moves[j-1]
            }
            
            moves[i] = "y"
            length += 1;
            for (var k = i; k < moves.length; k++) {
                switch (moves[k].charAt(0)) {
                    case 'R':
                        moves[k] = moves[k].replaceAt(0, 'F')
                        break;
                    case 'B':
                        moves[k] = moves[k].replaceAt(0, 'R')
                        break;
                    case 'L':
                        moves[k] = moves[k].replaceAt(0, 'B')
                        break;
                    case 'F':
                        moves[k] = moves[k].replaceAt(0, 'L')
                        break;
                    default:
                        break;
                }
            }
        } else if (moves[i].charAt(0) == "B") {
            for (var j = moves.length; j > i; j--) {
                moves[j] = moves[j-1]
            }
            
            moves[i] = "y'"
            length += 1
            for (var k = i; k < moves.length; k++) {
                switch (moves[k].charAt(0)) {
                    case 'R':
                        moves[k] = moves[k].replaceAt(0, 'B')
                        break;
                    case 'B':
                        moves[k] = moves[k].replaceAt(0, 'L')
                        break;
                    case 'L':
                        moves[k] = moves[k].replaceAt(0, 'F')
                        break;
                    case 'F':
                        moves[k] = moves[k].replaceAt(0, 'R')
                        break;
                    default:
                        break;
                }
            }
        }
        
        newScramble = newScramble + moves[i] + " "
    }
    return newScramble
}

function translate(moves, i, rotation) {
    if (rotation == "y") {
        
    } else if (rotation == "y'") {
        
    }
}

String.prototype.replaceAt = function(index, replacement) {
    return this.substr(0, index) + replacement + this.substr(index + replacement.length);
}
