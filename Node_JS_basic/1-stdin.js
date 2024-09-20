/* eslint-disable */

const readline = require('readline');

// Create an interface for input and output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Display the welcome message
console.log("Welcome to Holberton School, what is your name?");

// Prompt the user for their name
rl.on('line', (input) => {
    console.log(`Your name is: ${input}`);
    rl.close(); // Close the readline interface
});

// Event listener for closing the interface
rl.on('close', () => {
    console.log("This important software is now closing");
});
