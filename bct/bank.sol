// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {

    uint public balance;           // stores customer's balance
    address public owner;          // owner of the account

    constructor() {
        owner = msg.sender;        // account creator = owner
    }

    // Deposit money into account
    function deposit() public payable {
        balance += msg.value;
    }

    // Withdraw money from account
    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount <= balance, "Insufficient balance");

        balance -= amount;
        payable(owner).transfer(amount);
    }

    // Show current balance
    function getBalance() public view returns(uint) {
        return balance;
    }
}
