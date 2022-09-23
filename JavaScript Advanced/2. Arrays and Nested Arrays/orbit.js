function fillTheOrbit(coordinates) {
    function createOrbit(row, column) {
        let matrix = []
        for (let r = 0; r < row; r += 1) {
            let currRow = [];
            currRow.length = column;
            matrix.push(currRow);
        }
        return matrix;
    }
    
    function fillEmptyOrbit(filledValue, r, c) {
        let counter = 0;
        // First Row
        if (r == 0) {
            if (c == 0) {
                if (orbit[r][c + 1] == undefined) {
                    orbit[r][c + 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c + 1] == undefined) {
                    orbit[r + 1][c + 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c] == undefined) {
                    orbit[r + 1][c] = filledValue;
                    counter += 1;
                }
            } else if (c == column - 1) {
                if (orbit[r][c - 1] == undefined) {
                    orbit[r][c - 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c - 1] == undefined) {
                    orbit[r + 1][c - 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c] == undefined) {
                    orbit[r + 1][c] = filledValue;
                    counter += 1;
                }
            } else {
                if (orbit[r][c + 1] == undefined) {
                    orbit[r][c + 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c + 1] == undefined) {
                    orbit[r + 1][c + 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c] == undefined) {
                    orbit[r + 1][c] = filledValue;
                    counter += 1;
                }
                if (orbit[r][c - 1] == undefined) {
                    orbit[r][c - 1] = filledValue;
                    counter += 1;
                }
                if (orbit[r + 1][c - 1] == undefined) {
                    orbit[r + 1][c - 1] = filledValue;
                    counter += 1;
                }
            } 
        } else if (r == row - 1) {
            // Last Row
            if (r == row - 1) {
                if (c == 0) {
                    if (orbit[r][c + 1] == undefined) {
                        orbit[r][c + 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c + 1] == undefined) {
                        orbit[r - 1][c + 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c] == undefined) {
                        orbit[r - 1][c] = filledValue;
                        counter += 1;
                    }
                } else if (c == column - 1) {
                    if (orbit[r][c - 1] == undefined) {
                        orbit[r][c - 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c - 1] == undefined) {
                        orbit[r - 1][c - 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c] == undefined) {
                        orbit[r - 1][c] = filledValue;
                        counter += 1;
                    }
                } else {
                    if (orbit[r][c + 1] == undefined) {
                        orbit[r][c + 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c + 1] == undefined) {
                        orbit[r - 1][c + 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c] == undefined) {
                        orbit[r - 1][c] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r][c - 1] == undefined) {
                        orbit[r][c - 1] = filledValue;
                        counter += 1;
                    }
                    if (orbit[r - 1][c - 1] == undefined) {
                        orbit[r - 1][c - 1] = filledValue;
                        counter += 1;
                    }
                }
            }
    
        } else if (c == 0) {
            if (orbit[r][c + 1] == undefined) {
                orbit[r][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c + 1] == undefined) {
                orbit[r - 1][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c] == undefined) {
                orbit[r - 1][c] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c + 1] == undefined) {
                orbit[r + 1][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c] == undefined) {
                orbit[r + 1][c] = filledValue;
                counter += 1;
            }
        } else if (c == column - 1) {
            if (orbit[r][c - 1] == undefined) {
                orbit[r][c - 1] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c - 1] == undefined) {
                orbit[r - 1][c - 1] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c] == undefined) {
                orbit[r - 1][c] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c - 1] == undefined) {
                orbit[r + 1][c - 1] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c] == undefined) {
                orbit[r + 1][c] = filledValue;
                counter += 1;
            }
        } else {
            if (orbit[r - 1][c] == undefined) {
                orbit[r - 1][c] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c + 1] == undefined) {
                orbit[r - 1][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r][c + 1] == undefined) {
                orbit[r][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c + 1] == undefined) {
                orbit[r + 1][c + 1] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c] == undefined) {
                orbit[r + 1][c] = filledValue;
                counter += 1;
            }
            if (orbit[r + 1][c - 1] == undefined) {
                orbit[r + 1][c - 1] = filledValue;
                counter += 1;
            }
            if (orbit[r][c - 1] == undefined) {
                orbit[r][c - 1] = filledValue;
                counter += 1;
            }
            if (orbit[r - 1][c - 1] == undefined) {
                orbit[r - 1][c - 1] = filledValue;
                counter += 1;
            }
        }
        return counter;
    }

    let row = coordinates[0];
    let column = coordinates[1];
    let startRow = coordinates[2];
    let startCol = coordinates[3];
    let emptyPlaces = row * column - 1;
    let valueForFill = 2;
    let orbit = createOrbit(row, column);
    orbit[startRow][startCol] = 1;
    let currentFill = 0;
    currentFill = fillEmptyOrbit(valueForFill, startRow, startCol);
    emptyPlaces -= currentFill;
    
    while (emptyPlaces > 0) {
        let searchedValue = valueForFill;
        valueForFill += 1;
        for (let r = 0; r < row; r += 1) {
            for (let c = 0; c < column; c += 1) {
                if (orbit[r][c] == searchedValue) {
                    currentFill = fillEmptyOrbit(valueForFill, r, c);
                    emptyPlaces -= currentFill;
                }
            }
        }    
    }
    
    for (let currRow of orbit) {
        console.log(currRow.join(' '));
    }
}

fillTheOrbit([4, 4, 0, 0]);